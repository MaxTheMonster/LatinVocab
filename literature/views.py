from django.shortcuts import render
from django.views import generic

from literature import models

class LiteratureView(generic.ListView):
    template_name = "literature/index.html"
    model = models.Text
    context_object_name = "texts"

class TextView(generic.DetailView):
    template_name = "literature/text.html"
    slug_url_kwarg = "slug"
    model = models.Text

    def get_context_data(self, **kwargs):
        context = super(TextView, self).get_context_data(**kwargs)
        context['annotations'] = models.Annotation.objects.filter(relating_text__title=self.get_object().title)
#        print(context['annotations'])
        print(self.get_object)
        return context
