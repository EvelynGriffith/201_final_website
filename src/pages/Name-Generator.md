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

<html>
    <head>
      <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
      <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
      <link rel="generated_names" href="https://github.com/EvelynGriffith/201_final_website/blob/master/src/pages/generated_names.txt"/>
      <py-env>
        - paths:
          - /generated_names.txt
      </py-env>
    </head>

  <body>
    <h1>Your Name is:</h1>
    <py-script>
        import random
        with open("generated_names.txt", "r") as file:
            data = file.read()
            words = data.split(",")
            # Generating a random number for word position
            word_pos = random.randint(0, len(words) - 1)
            print("Position:", word_pos)
            print("Word at position:", words[word_pos])
    </py-script>
  </body>
</html>

<!-- <html>
    <body>
        <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
        <script defer src="https://pyscript.net/latest/pyscript.js"></script>
            <py-script>
                files = ["src\_data\random_names.py"]
            </py-script>
    </body>
</html> -->