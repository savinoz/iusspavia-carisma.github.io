---
layout: default
title: CARISMA
---

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
      <div class="hero-actions">
        <a href="{{ '/research/' | relative_url }}" class="btn btn-primary">Research Areas</a>
        <a href="{{ '/people/' | relative_url }}" class="btn btn-outline">People</a>
        <a href="{{ '/contact/' | relative_url }}" class="btn btn-outline">Contact</a>
      </div>
      <div class="hero-facts">
        <div class="hero-fact">
          <p class="hero-fact-label">Focus</p>
          <p class="hero-fact-text">Climate change, impacts, risk management and sustainable development.</p>
        </div>
        <div class="hero-fact">
          <p class="hero-fact-label">Approach</p>
          <p class="hero-fact-text">Earth-system science, engineering, economics and policy in one research centre.</p>
        </div>
        <div class="hero-fact">
          <p class="hero-fact-label">Training</p>
          <p class="hero-fact-text">Connected to IUSS Pavia and the National PhD in Sustainable Development and Climate Change.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="centre-section" markdown="0">
  <div class="container prose-block">
    <h2>Overview</h2>
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
