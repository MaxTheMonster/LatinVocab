from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Text(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    slug = models.SlugField(editable=False)
    content = models.TextField()
    translation = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        return super(Text, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("text_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Annotation(models.Model):
    device = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.device + ": " + self.description[:5]

class RelatingLatin(models.Model):
    latin = models.CharField(max_length=120, unique=True)
    relating_text = models.ForeignKey(Text, on_delete=models.CASCADE)
    annotations = models.ManyToManyField(Annotation, related_query_name="annotation")
    slug = models.SlugField(editable=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.latin)
        return super(RelatingLatin, self).save(*args, **kwargs)

    def __str__(self):
        return self.latin
