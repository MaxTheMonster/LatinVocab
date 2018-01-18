from django.db import models

class Text(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    
