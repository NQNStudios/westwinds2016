---
layout: poetry
title: Poetry
poems:
  - title: Four Years
    author: Kelly Mai
    file: FourYears.md
---

{% for poem in page.poems %}

### {{ poem.title }}

{% include {{ poem.file }} %}

&mdash;*{{ poem.author }}*

{% endfor %}
