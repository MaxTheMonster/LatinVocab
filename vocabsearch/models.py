from django.db import models


class Word(models.Model):
    english = models.CharField(max_length=128)
    latin = models.CharField(max_length=128, unique=True)
    type = models.CharField(max_length=128)
    category = models.CharField(max_length=128)

    def __str__(self):
        return self.latin
