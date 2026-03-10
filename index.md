---
layout: default
title: CARISMA
---

{% include hero-slider.html %}

<section class="centre-hero" markdown="0">
  <div class="container centre-hero-shell">
    <div class="centre-hero-main">
      <p class="centre-kicker">Research Centre</p>
      <h1 class="centre-title">{{ site.lab.full_name }}</h1>
      <p class="centre-acronym">{{ site.lab.name }}</p>
      <p class="centre-summary">{{ site.lab.tagline }}</p>
      <p class="centre-affiliation">
        Part of <a href="https://www.iusspavia.it/en" target="_blank" rel="noreferrer">IUSS Pavia</a>.
      </p>
    </div>
  </div>
</section>

<section class="centre-section" markdown="0">
  <div class="container prose-block">
    {% for paragraph in site.lab.overview.intro %}
    <p>{{ paragraph }}</p>
    {% endfor %}
    <h2>Main Objectives</h2>
    <ul class="plain-list">
      {% for item in site.lab.overview.objectives %}
      <li>{{ item }}</li>
      {% endfor %}
    </ul>
  </div>
</section>
