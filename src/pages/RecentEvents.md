---
layout: blog.njk
title: Recent Events
date: 2017-01-01
pagination:
  data: collections.post
  size: 20
permalink: "Recent Events{% if pagination.pageNumber > 0 %}/page/{{ pagination.pageNumber }}{% endif %}/index.html"
metaDescription: A sample Blog page listing various posts.
subtitle: A log of our recent events!
eleventyNavigation:
  key: Recent Events
  order: 3
---
