from django.shortcuts import render
from django.views import generic

from literature import models

class LiteratureView(generic.ListView):
    template_name = "literature/index.html"
    model = models.Text
    context_object_name = "texts"
