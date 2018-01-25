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
    latin = models.CharField(max_length=120)
    device = models.CharField(max_length=120)
    description = models.TextField()
    relating_text = models.ForeignKey(Text, on_delete=models.CASCADE)

    def __str__(self):
        return self.device + ": " + self.latin
