---
title: Name Generator
layout: page.njk
subtitle: ""
metaDescription: name generation AI
date: 2017-01-01T00:00:00.000Z
permalink: /Name-Generator/index.html
eleventyNavigation:
  key: Name Generator
  order: 6
---
 
<py-config>
    plugins = [
        "https://pyscript.net/latest/plugins/python/py_tutor.py"
    ]
</py-config>

<section class="pyscript">
    <py-script>
        import random

        # open file
        with open("generated_names.txt", "r") as file:
        data = file.read()
        words = data.split(",")

        # Generating a random number for word position
        word_pos = random.randint(0, len(words) - 1)
        print("Position:", word_pos)
        print("Word at position:", words[word_pos])
</py-script>
</section>