import random

from django.shortcuts import render
import json

from django.core import serializers
from django.db.models import Q
from vocabulary import models
from django.template.context_processors import csrf
from django.views import generic
from django.views.decorators.csrf import ensure_csrf_cookie

class IndexView(generic.TemplateView):
    template_name = "vocabulary/index.html"

    def get_context_data(self, **kwargs):
            context = super(IndexView, self).get_context_data(**kwargs)
            categories_queryset = models.Word.objects.all().values("category")
            categories = []
            for category in categories_queryset:
                categories.append(category['category'])

            context['categories'] = sorted(list(set(categories)))
            context['words'] = serializers.serialize('json', models.Word.objects.all(), fields=("latin", "english", "category", "type"))
            return context

def init_test(request):
    types = ["All", "Nounn", "Adjectives", "Adverbs", "Verbs", "Conjunctions", "Prepositions", "Pronouns"]
    return render(request, "vocabulary/test.html", {"types": types})

class TakeTest(generic.TemplateView):
    template_name = "vocabulary/take_test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = []
        words = []
        if self.kwargs["type"] == "everything":
            words = list(models.Word.objects.all())
        else:
            words = list(models.Word.objects.all().filter(type__startswith=self.kwargs["type"]))
            random.shuffle(words)
            words = words[:self.kwargs["amount"]]
            for word in words:
                if direction == "latin":
                    answers.append(word.english)
                elif direction == "english":
                    answers.append(word.latin)
        context['answers'] = answers
        context['words'] = words
        context['direction'] = self.kwargs["direction"]
        context['amount'] = self.kwargs["amount"]
        return context
