import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LatinVocab.settings")

import django
django.setup()

from vocabulary.models import Word
file = open("vocab.txt", "r").readlines()

for line in file:
    b = line.split("/")
    try:
        print(b)
        latin = b[0]
        type = b[1]
        english = b[2]
        category = b[3]

        w = Word(latin=latin, english=english, type=type, category=category)

        w.save()
    except:
        continue

from literature.models import Text
file = open("literature.txt", "r").readlines()

for line in file:
    b = line.split("/")
    try:
        print(b)
        title = b[0]
        author = b[1]
        content = b[2]
        translation = b[3]

        w = Text(title=title, author=author, content=content, translation=translation)

        w.save()
    except:
        continue
