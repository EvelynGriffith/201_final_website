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
<body>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <py-script>
        plugins = [
            "https://pyscript.net/latest/plugins/python/py_tutor.py"
        ]
        [[fetch]]
        files = ["src\_data\random_names.py"]
    </py-script>
</body>
</html>