#!/usr/bin/env python3
"""
Update existing _people/*.md files from Google Form CSV responses

Usage:
    python scripts/csv_to_people_md.py path/to/responses.csv

The CSV should have these columns (in any order):
    - Full name with title (required - used to match existing file)
    - Position (optional)
    - Email (optional)
    - Biography (optional)
    - PhD Program (optional)
    - ResearchGate URL (optional)
    - LinkedIn URL (optional)
    - ORCID URL (optional)
    - Personal Website (optional)

Only non-empty fields in the CSV will update the existing file.
"""

import csv
import re
import sys
from pathlib import Path


def generate_slug(name: str) -> str:
    """Convert name to URL-friendly slug.

    'Elisa Nobile, MSc' -> 'elisa-nobile'
    """
    name = name.split(',')[0].strip()
    slug = name.lower()
    slug = re.sub(r'[^a-z\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug


def parse_md_file(filepath: Path) -> tuple[dict, str]:
    """Parse a markdown file with YAML front matter.

    Returns (front_matter_dict, body_content)
    """
    content = filepath.read_text(encoding='utf-8')

    # Split front matter and body
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    front_matter_text = parts[1].strip()
    body = parts[2].strip()

    # Parse YAML front matter (simple key: value parsing)
    front_matter = {}
    for line in front_matter_text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            front_matter[key] = value

    return front_matter, body


def write_md_file(filepath: Path, front_matter: dict, body: str):
    """Write markdown file with YAML front matter."""
    lines = ['---']

    # Write front matter in a logical order
    field_order = [
        'name', 'slug', 'position', 'phd_program',
        'email', 'researchgate', 'linkedin', 'orcid',
        'iuss_page', 'iuss_research', 'website', 'photo'
    ]

    # Write known fields in order
    for key in field_order:
        if key in front_matter:
            lines.append(f'{key}: "{front_matter[key]}"')

    # Write any remaining fields
    for key, value in front_matter.items():
        if key not in field_order:
            lines.append(f'{key}: "{value}"')

    lines.append('---')
    lines.append('')
    lines.append(body)
    lines.append('')

    filepath.write_text('\n'.join(lines), encoding='utf-8')


# Mapping from CSV column names to front matter keys
CSV_TO_FIELD = {
    'Full name with title': 'name',
    'Position': 'position',
    'Email': 'email',
    'Biography': '_biography',  # Special handling
    'PhD Program': 'phd_program',
    'ResearchGate URL': 'researchgate',
    'LinkedIn URL': 'linkedin',
    'ORCID URL': 'orcid',
    'Personal Website': 'website',
}


def update_from_row(row: dict, front_matter: dict, body: str) -> tuple[dict, str, list]:
    """Update front matter and body from CSV row.

    Returns (updated_front_matter, updated_body, list_of_changes)
    """
    changes = []

    for csv_col, field_key in CSV_TO_FIELD.items():
        new_value = row.get(csv_col, '').strip()
        if not new_value:
            continue

        if field_key == '_biography':
            if new_value != body:
                body = new_value
                changes.append('biography')
        else:
            old_value = front_matter.get(field_key, '')
            if new_value != old_value:
                front_matter[field_key] = new_value
                changes.append(field_key)

    return front_matter, body, changes


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/csv_to_people_md.py path/to/responses.csv")
        sys.exit(1)

    csv_path = Path(sys.argv[1])
    if not csv_path.exists():
        print(f"Error: File not found: {csv_path}")
        sys.exit(1)

    # Output directory
    script_dir = Path(__file__).parent
    people_dir = script_dir.parent / '_people'

    if not people_dir.exists():
        print(f"Error: _people directory not found at {people_dir}")
        sys.exit(1)

    # Read CSV and update files
    updated = []
    not_found = []
    no_changes = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row.get('Full name with title', '').strip()
            if not name:
                continue

            slug = generate_slug(name)
            filename = f"{slug}.md"
            filepath = people_dir / filename

            if not filepath.exists():
                not_found.append((name, filename))
                continue

            # Parse existing file
            front_matter, body = parse_md_file(filepath)

            # Update with CSV data
            front_matter, body, changes = update_from_row(row, front_matter, body)

            if not changes:
                no_changes.append(filename)
                continue

            # Write updated file
            write_md_file(filepath, front_matter, body)
            updated.append((filename, changes))
            print(f"Updated: {filename} ({', '.join(changes)})")

    # Summary
    print(f"\n{'='*50}")
    print(f"Updated: {len(updated)} file(s)")
    for filename, changes in updated:
        print(f"  + {filename}: {', '.join(changes)}")

    if no_changes:
        print(f"\nNo changes needed: {len(no_changes)} file(s)")

    if not_found:
        print(f"\nNot found: {len(not_found)} file(s)")
        for name, filename in not_found:
            print(f"  ? {name} -> expected {filename}")


if __name__ == '__main__':
    main()
