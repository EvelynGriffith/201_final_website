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
    [[fetch]]
    files = ["src\_data\random_names.py"]
</py-config>
<div style="margin-right: 3rem">
    <py-repl id="my-repl" auto-generate="true"> </py-repl>
</div>