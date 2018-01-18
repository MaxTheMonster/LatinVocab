import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LatinVocab.settings")
import django
django.setup()
from vocabulary import models
file = open("vocab.txt", "r").readlines()

for line in file:
    b = line.split("/")
    try:
        print(b)
        latin = b[0]
        type = b[1]
        english = b[2]
        category = b[3]

        w = models.Word(latin=latin, english=english, type=type, category=category)

        w.save()
    except:
        continue
