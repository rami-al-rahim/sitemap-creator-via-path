# Sitemap Generator

This is a Python script that generates a valid `sitemap.xml` file for a given website. The script crawls the website, extracts all URLs, and creates a properly formatted sitemap according to the [Sitemap Protocol](http://www.sitemaps.org/schemas/sitemap/0.9).

---

## Features

- **Recursive Crawling**: Crawls the website starting from a given URL and discovers all linked pages.
- **Valid Sitemap**: Generates a valid `sitemap.xml` file that can be submitted to search engines.
- **Customizable**: Easily modify the script to include additional tags like `<lastmod>`, `<changefreq>`, or `<priority>`.

---

## Requirements

- Python 3.x
- Libraries: `requests`, `beautifulsoup4`

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4

```

# Usage

1.  Clone the repository:

```bash
git clone https://github.com/rami-al-rahim/sitemap-generator.git
cd sitemap-generator
```

2.  Run the script:

```bash
python sitemap_generator.py
```

# Credits
[Rami Mustafa](https://github.com/rami-al-rahim).
