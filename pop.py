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

from literature.models import Annotation
file = open("annotations.txt", "r").readlines()

for line in file:
    b = line.split("/")
    try:
        print(b)
        latin = b[0]
        device = b[1]
        related_text = Text.objects.filter(title=b[2])[0]
        description = b[3]

        print(related_text)
        w = Annotation(latin=latin, device=device, description=description, relating_text=related_text)

        w.save()
    except:
        continue
