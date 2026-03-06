---
layout: default
title: Home
---

<!-- Hero Section -->
<section class="hero" markdown="0">
  <div class="hero-content">
    <span class="hero-tag">{{ site.lab.department }}</span>
    <h1 class="hero-title">{{ site.lab.name }}</h1>
    <p class="hero-subtitle">{{ site.lab.tagline }}</p>
    <div class="hero-description">
      {% for paragraph in site.lab.overview.intro %}
      <p>{{ paragraph }}</p>
      {% endfor %}
    </div>
    <div class="hero-highlights">
      <div class="hero-panel">
        <h2 class="hero-panel-title">Main Objectives</h2>
        <ul class="hero-list">
          {% for item in site.lab.overview.objectives %}
          <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
      <div class="hero-panel">
        <h2 class="hero-panel-title">Main Research Activities</h2>
        <ul class="hero-list">
          {% for item in site.lab.overview.activities %}
          <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
    </div>
    <div class="hero-actions">
      <a href="{{ '/research/' | relative_url }}" class="btn btn-primary">Explore Our Research</a>
      <a href="{{ '/contact/' | relative_url }}" class="btn btn-secondary">Get in Touch</a>
    </div>
  </div>
  <div class="hero-visual">
    <div class="hero-image-placeholder">
      <!-- Add your hero image to assets/images/hero.jpg -->
      <span>🌱</span>
    </div>
  </div>
</section>

<!-- Research Highlights -->
<section class="section section-research" markdown="0">
  <div class="container">
    <header class="section-header">
      <span class="section-tag">Research Areas</span>
      <h2 class="section-title">What We Do</h2>
      <p class="section-desc">Our lab focuses on sustainable agricultural systems through interdisciplinary research.</p>
    </header>

    <div class="research-grid">
      {% for project in site.research limit:3 %}
      <article class="research-card">
        <div class="research-icon">{{ project.icon | default: "🔬" }}</div>
        <h3 class="research-title">{{ project.title }}</h3>
        <p class="research-excerpt">{{ project.excerpt | strip_html | truncatewords: 20 }}</p>
        <a href="{{ project.url | relative_url }}" class="research-link">Learn more →</a>
      </article>
      {% endfor %}
    </div>

    <div class="section-cta">
      <a href="{{ '/research/' | relative_url }}" class="btn btn-outline">View All Research</a>
    </div>
  </div>
</section>

<!-- Stats Section -->
<section class="section section-stats" markdown="0">
  <div class="container">
    <div class="stats-grid">
      <div class="stat-item">
        <span class="stat-number">{{ "now" | date: "%Y" | minus: site.lab.founded }}</span>
        <span class="stat-label">Years Active</span>
      </div>
      <div class="stat-item">
        <span class="stat-number">{{ site.people | size }}</span>
        <span class="stat-label">Team Members</span>
      </div>
      <div class="stat-item">
        <span class="stat-number">{{ site.publications | size }}</span>
        <span class="stat-label">Publications</span>
      </div>
      <div class="stat-item">
        <span class="stat-number">12</span>
        <span class="stat-label">Active Projects</span>
      </div>
    </div>
  </div>
</section>

<!-- Team Preview -->
<section class="section section-team" markdown="0">
  <div class="container">
    <header class="section-header">
      <span class="section-tag">Our Team</span>
      <h2 class="section-title">Meet the Researchers</h2>
      <p class="section-desc">A diverse group of scientists, engineers, and thinkers.</p>
    </header>

    <div class="team-grid">
      {% assign leaders = site.people | where: "role", "PI" %}
      {% for person in leaders limit:2 %}
      <article class="team-card team-card-featured">
        <div class="team-photo">
          {% if person.photo and person.photo != "" %}
          <img src="{{ person.photo | relative_url }}" alt="{{ person.name }}">
          {% else %}
          <div class="team-photo-placeholder">{{ person.name | slice: 0 }}</div>
          {% endif %}
        </div>
        <div class="team-info">
          <h3 class="team-name">{{ person.name }}</h3>
          <p class="team-role">{{ person.position }}</p>
          <p class="team-bio">{{ person.content | strip_html | truncatewords: 15 }}</p>
          <a href="{{ person.url | relative_url }}" class="team-link">View Profile →</a>
        </div>
      </article>
      {% endfor %}
    </div>

    <div class="section-cta">
      <a href="{{ '/people/' | relative_url }}" class="btn btn-outline">Meet the Full Team</a>
    </div>
  </div>
</section>

<!-- Latest News -->
<section class="section section-news" markdown="0">
  <div class="container">
    <header class="section-header">
      <span class="section-tag">Latest Updates</span>
      <h2 class="section-title">News & Events</h2>
    </header>

    <div class="news-list">
      {% for post in site.news limit:3 %}
      <article class="news-item">
        <time class="news-date" datetime="{{ post.date | date_to_xmlschema }}">
          {{ post.date | date: "%b %d, %Y" }}
        </time>
        <div class="news-content">
          <h3 class="news-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
          <p class="news-excerpt">{{ post.excerpt | strip_html | truncatewords: 20 }}</p>
        </div>
      </article>
      {% endfor %}
    </div>

    <div class="section-cta">
      <a href="{{ '/news/' | relative_url }}" class="btn btn-outline">All News</a>
    </div>
  </div>
</section>

<!-- Contact CTA -->
<section class="section section-cta" markdown="0">
  <div class="container">
    <div class="cta-box">
      <h2 class="cta-title">Interested in Collaboration?</h2>
      <p class="cta-text">We're always looking for passionate researchers, students, and partners to join our mission.</p>
      <div class="cta-actions">
        <a href="{{ '/contact/' | relative_url }}" class="btn btn-primary">Contact Us</a>
        <a href="mailto:{{ site.contact.email }}" class="btn btn-ghost">{{ site.contact.email }}</a>
      </div>
    </div>
  </div>
</section>
