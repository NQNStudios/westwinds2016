---
layout: default
title: Prose
pieces:
  - title: Apples Indeed
    author: Michelle Smith
    file: ApplesIndeed.md
  - title: Artistic Hero
    author: Briquelle Schreiter
    file: ArtisticHero.md
  - title: "Driving Age: 14"
    author: Ariane Petersen
    file: DrivingAge14.md
  - title: First Drive into Reality
    author: Jocelin Mateos
    file: FirstDriveIntoReality.md
  - title: Freedom
    author: Audriana Hunter
    file: Freedom.md
  - title: Freedom II
    author: Marcus Webster
    file: FreedomII.md
  - title: It always comes back to you
    author: Sean Deegan
    file: ItAlwaysComesBackToYou.md
  - title: My First Drive
    author: Juyoung Kim
    file: MyFirstDrive.md
  - title: My First Heroes
    author: Sophie Valdez
    file: MyFirstHeroes.md
  - title: My Own Voice
    author: Maisy Phelps
    file: MyOwnVoice.md
  - title: Stories
    author: Audriana Hunter
    file: Stories.md
---

Contents
--------

{% for piece in page.pieces %}

* [{{ piece.title }}](#{{ piece.title }}) by {{ piece.author }}

{% endfor %}

{% for piece in page.pieces %}

### "{{ piece.title }}" by {{ piece.author }} <a name="{{ piece.title }}">&nbsp;</a>

{% include {{ piece.file }} %}

{% endfor %}
