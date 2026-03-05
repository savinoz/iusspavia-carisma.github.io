# 🌱 AgroSystems Lab Website

A modern, clean, and easy-to-edit lab website built with **Jekyll** and **Markdown**. Designed to be approachable, not clinical.

## ✨ Features

- **Pure Markdown** - Edit everything in simple Markdown files
- **Easy Data Management** - People, publications, and research are all data-driven
- **Modern Design** - Clean, accessible, and professional without being stuffy
- **Responsive** - Looks great on desktop, tablet, and mobile
- **Fast & SEO-friendly** - Static site with optimized performance
- **Works with** - Jekyll, Hugo, MkDocs (with minor adaptations)

## 🚀 Quick Start

### Prerequisites

- Ruby 2.7+ (for Jekyll)
- Bundler gem

### Installation

```bash
# Clone or navigate to the lab-website folder
cd lab-website

# Install dependencies
bundle install

# Run the development server
bundle exec jekyll serve

# Visit http://localhost:4000
```

## 📝 How to Edit Content

All content is stored in Markdown files. No HTML knowledge required!

### 1. Site Configuration

Edit `_config.yml` to update:
- Lab name and description
- Contact information
- Social media links
- Navigation menu

```yaml
lab:
  name: "Your Lab Name"
  tagline: "Your catchy tagline"
  
contact:
  email: "your@email.edu"
  
social:
  twitter: "https://twitter.com/yourlab"
```

### 2. Homepage

Edit `index.md` to customize the hero section and page layout.

### 3. Research Areas

Add or edit research projects in `_research/` folder:

```markdown
---
title: "Your Research Title"
subtitle: "Brief description"
icon: 🌾
status: Active
funding: "NSF Grant #12345"
team:
  - Dr. Jane Smith
  - Alex Johnson
---

Write your research description here using **Markdown**.
```

### 4. People/Team Members

Add team members in `_people/` folder:

```markdown
---
name: "Dr. Jane Smith"
position: "Associate Professor"
role: PI  # Options: PI, Researcher, PhD Student, MSc Student, Alumni
email: "jane@university.edu"
photo: "/assets/images/team/jane.jpg"
---

Bio goes here...
```

### 5. Publications

Add publications in `_publications/` folder:

```markdown
---
title: "Your Paper Title"
authors: "Smith, J., & Doe, A."
journal: "Nature"
year: 2024
doi: "10.1038/..."
type: article  # Options: article, conference, book, report
---
```

### 6. News/Updates

Add news posts in `_news/` folder with date prefix:

```markdown
---
title: "Exciting News!"
date: 2024-03-15
author: "Dr. Jane Smith"
---

Your news content here...
```

### 7. Pages

Edit pages in `_pages/` folder:
- `research.md` - Research overview
- `people.md` - Team listing
- `publications.md` - Publication list
- `contact.md` - Contact form and info

## 🎨 Customization

### Colors

Edit CSS variables in `assets/css/main.css`:

```css
:root {
  --color-primary: #2563eb;    /* Blue */
  --color-secondary: #059669;  /* Green */
  --color-accent: #dc2626;     /* Red */
}
```

### Fonts

The site uses Google Fonts (Inter + Playfair Display). Change in `_layouts/default.html`:

```html
<link href="https://fonts.googleapis.com/css2?family=Your+Font&display=swap" rel="stylesheet">
```

Then update in `main.css`:

```css
:root {
  --font-sans: 'Your Font', sans-serif;
}
```

### Images

1. Add images to `assets/images/`
2. Reference them with: `/assets/images/your-image.jpg`

For team photos, recommended size is 400x400px (square).

For hero background, recommended size is 1920x1080px.

## 📁 Folder Structure

```
lab-website/
├── _config.yml              # Site configuration
├── _data/                   # Data files (optional)
├── _includes/               # Reusable components
│   ├── navigation.html
│   └── footer.html
├── _layouts/                # Page templates
│   ├── default.html
│   ├── page.html
│   ├── post.html
│   ├── person.html
│   └── research.html
├── _pages/                  # Content pages
│   ├── research.md
│   ├── people.md
│   ├── publications.md
│   └── contact.md
├── _people/                 # Team member profiles
├── _publications/           # Publication entries
├── _research/               # Research project pages
├── _news/                   # News/blog posts
├── assets/
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── index.md                 # Homepage
├── Gemfile                  # Ruby dependencies
└── README.md                # This file
```

## 🔧 Deployment

### GitHub Pages (Free)

1. Push to a GitHub repository
2. Enable GitHub Pages in repository settings
3. Select source: Deploy from a branch → `main` branch → `/ (root)`
4. Your site will be at `https://yourusername.github.io/lab-website`

### Netlify (Free with more features)

1. Connect your GitHub repository to Netlify
2. Build command: `bundle exec jekyll build`
3. Publish directory: `_site`

### Custom Server

```bash
# Build the site
bundle exec jekyll build

# Upload contents of `_site` folder to your server
```

## 🌐 Converting to Hugo or MkDocs

This site uses standard Markdown with YAML frontmatter, which works across static site generators:

### Hugo
- Move content to `content/` folder
- Convert `_layouts/` to `layouts/` with Go templates
- Frontmatter remains the same

### MkDocs
- Move pages to `docs/` folder
- Use `mkdocs.yml` for navigation
- Frontmatter works with `mkdocs-markdownextradata` plugin

## 🛠️ Troubleshooting

**Build errors?**
- Run `bundle update` to update dependencies
- Check `_config.yml` for syntax errors (use spaces, not tabs)

**Changes not showing?**
- Jekyll caches content - stop and restart the server
- Check file names for typos

**Images not loading?**
- Ensure paths start with `/` for absolute paths
- Check file extensions match exactly

## 📄 License

This template is released under the MIT License. Feel free to use and modify for your lab.

## 💡 Tips

1. **Keep it simple** - Focus on content, not fancy features
2. **Update regularly** - Add news items and publications as they happen
3. **Use emojis** - They make the site feel more approachable 🌱
4. **Add photos** - Real team photos make a big difference
5. **Link to resources** - Code, data, and publications should be accessible

## 🆘 Need Help?

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Markdown Guide](https://www.markdownguide.org/)
- [YAML Syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)

---

Built with ♥ for research labs everywhere.
