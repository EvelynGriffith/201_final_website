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
      <py-env>
        - paths:
          - /generated_names.txt
      </py-env>
    </head>

  <body>
    <h1>Let's print random numbers</h1>
    <b>Doe's lucky number is <label id="lucky"></label></b>
    <py-script>
      from example import generate_random_number
      pyscript.write('lucky', generate_random_number())
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