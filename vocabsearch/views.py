import random
from django.shortcuts import render
from django.db.models import Q
from vocabsearch.models import Word
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    args = {}
    args.update(csrf(request))
    return render(request, "vocabsearch/index.html")


def search_words(request):
    if request.method == "POST":
        if request.POST["search_text"] == "":
            search_text = ""
        else:
            search_text = request.POST["search_text"]
    else:
        search_text = ''
#  | Word.objects.filter(english__contains=search_text)
    start_words = Word.objects.filter(latin__startswith=search_text) | Word.objects.filter(english__startswith=search_text)
    words = Word.objects.filter(latin__contains=search_text) | Word.objects.filter(english__contains=search_text)

    return render(request, "ajax_search.html", {"words": words, "startwords": start_words})


def init_test(request):
    types = ["EVERYTHING BABE!", "Noun", "Adjective", "Adverb", "Verb", "Conjunction", "Preposition", "Pronoun"]
    print("BLEH")
    return render(request, "vocabsearch/test.html", {"types": types})


def test(request, type, amount, direction):
    amount = int(amount)

    if type == "everything":
        words = list(Word.objects.all())
    else:
        words = list(Word.objects.all().filter(type__startswith=type))

    random.shuffle(words)
    words = words[:amount]
    answers = []
    for word in words:
        print(word.english)
        if direction == "latin":
            answers.append(word.english)
        elif direction == "english":
            answers.append(word.latin)



    return render(request, "vocabsearch/take_test.html", {"words": words, "direction": direction, "answers": answers, "amount": amount})
