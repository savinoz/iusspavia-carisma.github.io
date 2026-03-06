---
layout: page
title: People
permalink: /people/
---

<div class="prose-block">
  <h2>Head of Research Centre</h2>
  {% assign head = site.people | where: "slug", "marco-gaetani" | first %}
  {% if head %}
  <div class="people-directory">
    <article class="directory-card">
      <h3 class="directory-name"><a href="{{ head.url | relative_url }}">{{ head.name }}</a></h3>
      <p class="directory-role">{{ head.position }}</p>
    </article>
  </div>
  {% endif %}
</div>

<div class="prose-block">
  <h2>Professors</h2>
  <div class="people-directory">
    {% assign professors = site.people | where: "group", "Professor" | sort: "sort_order" %}
    {% for person in professors %}
    <article class="directory-card">
      <h3 class="directory-name"><a href="{{ person.url | relative_url }}">{{ person.name }}</a></h3>
      <p class="directory-role">{{ person.position }}</p>
    </article>
    {% endfor %}
  </div>
</div>

<div class="prose-block">
  <h2>Associate Professor</h2>
  <div class="people-directory">
    {% assign associates = site.people | where: "group", "Associate Professor" | sort: "sort_order" %}
    {% for person in associates %}
    <article class="directory-card">
      <h3 class="directory-name"><a href="{{ person.url | relative_url }}">{{ person.name }}</a></h3>
      <p class="directory-role">{{ person.position }}</p>
    </article>
    {% endfor %}
  </div>
</div>

<div class="prose-block">
  <h2>Postdocs</h2>
  <div class="people-directory">
    {% assign postdocs = site.people | where: "group", "Postdoc" | sort: "sort_order" %}
    {% for person in postdocs %}
    <article class="directory-card">
      <h3 class="directory-name"><a href="{{ person.url | relative_url }}">{{ person.name }}</a></h3>
      <p class="directory-role">{{ person.position }}</p>
    </article>
    {% endfor %}
  </div>
</div>

<div class="prose-block">
  <h2>PhD Students</h2>
  <p>
    Several members are part of the
    <a href="https://www.phd-sdc.it/" target="_blank" rel="noreferrer">National PhD in Sustainable Development and Climate Change (PhD SDC)</a>.
  </p>
  <div class="people-directory">
    {% assign phd_students = site.people | where: "group", "PhD Student" | sort: "sort_order" %}
    {% for person in phd_students %}
    <article class="directory-card">
      <h3 class="directory-name"><a href="{{ person.url | relative_url }}">{{ person.name }}</a></h3>
      <p class="directory-role">{{ person.position }}</p>
      {% if person.phd_program %}
      <p class="directory-meta">{{ person.phd_program }}</p>
      {% endif %}
    </article>
    {% endfor %}
  </div>
</div>

<div class="prose-block">
  <h2>Former Members</h2>
  <ul class="plain-list former-list">
    {% for person in site.lab.people.former_members %}
    <li>
      <span>{{ person.name }}</span>
      {% if person.orcid and person.orcid != "" %}
      <a href="{{ person.orcid }}" target="_blank" rel="noreferrer" class="former-link">ORCID</a>
      {% endif %}
    </li>
    {% endfor %}
  </ul>
</div>
