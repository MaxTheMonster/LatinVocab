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

from literature.models import Annotation, RelatingLatin
file = open("annotations.txt", "r").readlines()
annotations = []
finalAnnotations = []

for line in file:
    b = line.split("/")
    try:
        print(b)
        latin = b[1]
        device = b[2]
        related_text = Text.objects.filter(title=b[0])[0]
        description = b[3]
 #       a = Annotation(device=device, description=description)

        annotations.append(b)
    except:
        continue

previous_relating_latin = ""

for a in annotations:
    latin = a[1]
    device = a[2]
    related_text = Text.objects.filter(title=a[0])[0]
    description = a[3]

    if latin != previous_relating_latin:
        existing_related_latin = RelatingLatin.objects.filter(latin=latin, relating_text=related_text)
        if len(existing_related_latin) > 0:
            pass
        else:
            relating_latin = RelatingLatin(latin=latin, relating_text=related_text)
            relating_latin.save()
            # except django.db.utils.IntegrityError:
            #     conflicting_latin = RelatingLatin.objects.filter(latin=latin)
            #     for latin in conflicting_latin:
            #         if latin.relating_text == a[0]:
            #             pass
        previous_relating_latin = relating_latin

    relating_latin = RelatingLatin.objects.filter(latin=latin, relating_text=related_text)[0]
    print(relating_latin)
    annotation = Annotation(device=device, description=description)
    annotation.save()

    retrieved_annotation = Annotation.objects.filter(description=description)[0]
    print(retrieved_annotation)
    relating_latin.annotations.add(retrieved_annotation)
    relating_latin.save()
