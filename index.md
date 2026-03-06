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
      <dl class="centre-meta">
        <div class="centre-meta-item">
          <dt>Head</dt>
          <dd>{{ site.lab.head }}</dd>
        </div>
        <div class="centre-meta-item">
          <dt>Institution</dt>
          <dd>{{ site.lab.university }}</dd>
        </div>
        <div class="centre-meta-item">
          <dt>Contact</dt>
          <dd><a href="mailto:{{ site.contact.email }}">{{ site.contact.email }}</a></dd>
        </div>
        <div class="centre-meta-item">
          <dt>Phone</dt>
          <dd>{{ site.contact.phone }}</dd>
        </div>
      </dl>
      <figure class="centre-image-frame">
        <img src="{{ '/assets/img/grp.png' | relative_url }}" alt="CARISMA group" class="centre-image">
      </figure>
    </div>
  </div>
</section>

<section class="centre-section" markdown="0">
  <div class="container prose-block">
    <h2>Overview</h2>
    {% for paragraph in site.lab.overview.intro %}
    <p>{{ paragraph }}</p>
    {% endfor %}
  </div>
</section>

<section class="centre-section centre-section-alt" markdown="0">
  <div class="container two-column-grid">
    <div class="info-panel">
      <h2>Main Objectives</h2>
      <ul class="plain-list">
        {% for item in site.lab.overview.objectives %}
        <li>{{ item }}</li>
        {% endfor %}
      </ul>
    </div>
    <div class="info-panel">
      <h2>Main Research Activities</h2>
      <ul class="plain-list">
        {% for item in site.lab.overview.activities %}
        <li>{{ item }}</li>
        {% endfor %}
      </ul>
    </div>
  </div>
</section>

<section class="centre-section" markdown="0">
  <div class="container prose-block">
    <h2>Research Areas</h2>
    <div class="editorial-sections">
      {% for area in site.lab.activity_sections %}
      <article class="editorial-item">
        <h3>{{ area.title }}</h3>
        {% for paragraph in area.paragraphs %}
        <p>{{ paragraph }}</p>
        {% endfor %}
      </article>
      {% endfor %}
    </div>
  </div>
</section>

<section class="centre-section centre-section-alt" markdown="0">
  <div class="container">
    <h2>Research Projects</h2>
    <ul class="project-list">
      {% for item in site.lab.projects %}
      <li>{{ item }}</li>
      {% endfor %}
    </ul>
  </div>
</section>

<section class="centre-section" markdown="0">
  <div class="container">
    <h2>People</h2>
    <p class="section-intro">Head of Research Centre: {{ site.lab.head }}</p>
    <div class="name-grid">
      {% for person in site.lab.people.staff %}
      <div class="name-chip">{{ person }}</div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="centre-section centre-section-alt" markdown="0">
  <div class="container two-column-grid">
    <div class="info-panel">
      <h2>National Collaborations</h2>
      <ul class="plain-list">
        {% for item in site.lab.collaborations.national %}
        <li>{{ item }}</li>
        {% endfor %}
      </ul>
    </div>
    <div class="info-panel">
      <h2>International Collaborations</h2>
      <ul class="plain-list">
        {% for item in site.lab.collaborations.international %}
        <li>{{ item }}</li>
        {% endfor %}
      </ul>
    </div>
  </div>
</section>

<section class="centre-section" markdown="0">
  <div class="container two-column-grid">
    <div class="info-panel">
      <h2>Publications</h2>
      <ul class="link-list">
        {% for item in site.lab.publications %}
        <li><a href="{{ item.url }}" target="_blank" rel="noreferrer">{{ item.name }}</a></li>
        {% endfor %}
      </ul>
    </div>
    <div class="info-panel">
      <h2>Contact</h2>
      <p><a href="mailto:{{ site.contact.email }}">{{ site.contact.email }}</a></p>
      <p>{{ site.contact.phone }}</p>
      <p>{{ site.contact.fax }}</p>
      <p>{{ site.contact.address | newline_to_br }}</p>
      <p><a href="{{ site.contact.map_link }}" target="_blank" rel="noreferrer">Open map</a></p>
    </div>
  </div>
</section>
