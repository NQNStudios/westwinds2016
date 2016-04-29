---
layout: poetry
title: Poetry
poems:
  - title: Four Years
    author: Kelly Mai
    file: FourYears.md
  - title: Freedom
    author: Ariane Petersen
    file: FreedomPoem.md
  - title: Grandma
    author: Karuna Spaulding
    file: Grandma.md
  - title: Radiating
    author: Maggie Olvera
    file: Radiating.md
  - title: Untitled
    author: Karla Diaz
    file: Untitled1.md
  - title: Untitled
    author: Akesa Fehoko
    file: UntitledPoem1.md
  - title: Untitled
    author: Anonymous
    file: UntitledPoem2.md
  - title: Just a Crush
    author: Anya Weylarz
    file: UntitledDoc.md
  - title: Untitled
    author: Anya Weylarz
    file: UntitledPoemAnya.md
  - title: What Freedom Means
    author: Josie Messersmith
    file: WhatFreedomMeans.md
  - title: Romantic Nathy Brain
    author: Nathaniel Nelson
    file: NathyBrain.md
---

Contents
--------

{% for poem in page.poems %}

* [{{ poem.title}}](#{{ poem.file }}) by {{ poem.author }}

{% endfor %}

{% for poem in page.poems %}

### {{ poem.title }} <a name="{{poem.file}}">&nbsp;</a>

{% include {{ poem.file }} %}

<br />

&mdash;*{{ poem.author }}*

<br />

{% endfor %}
