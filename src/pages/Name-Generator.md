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
    Hello world! <br>
    This is the current date and time, as computed by Python:
    <py-script>
        from datetime import datetime
        now = datetime.now()
        display(now.strftime("%m/%d/%Y, %H:%M:%S"))
    </py-script>
</section>