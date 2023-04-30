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
<script defer src="https://pyscript.net/latest/pyscript.js"></script>
<link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
</head>
<body>
<py-script>
    def give_name():
        with open("generated_names.txt", "r") as file:
            alltext = file.read():
            words = list(map(str, alltext.split(,)))
        print(random.choice(words))

    give_name()
</py-script>
</body>
</html>