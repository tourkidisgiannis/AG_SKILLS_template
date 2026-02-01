---
name: brand-scraper
description: Extract comprehensive brand identity and design system data from websites using Firecrawl API. Use when you need to analyze a website's branding, colors, typography, fonts, logos, images, UI components, or styling for design inspiration, competitive analysis, or building similar websites. Triggers on requests to scrape/extract/analyze brand data, design systems, color schemes, typography, or visual identity from websites.
---

# Brand Scraper

Extract comprehensive brand identity and design system information from any website using the Firecrawl API.

## Quick Start

Use the `scrape_brand.py` script to extract brand data:

```bash
python scripts/scrape_brand.py https://example.com
```

This will:
1. Scrape the website using Firecrawl's branding format
2. Download brand images (logo, favicon, og:image)
3. Capture a screenshot
4. Generate a comprehensive brand report (JSON + Markdown)

## What Gets Extracted

### Brand Colors
- Primary, secondary, accent colors
- Background and text colors
- Link, success, warning, error colors
- Color scheme (light/dark mode)

### Typography
- Font families (primary, heading, code)
- Font sizes (h1-h6, body)
- Font weights (light, regular, medium, bold)
- Line heights

### Visual Assets
- Logo (primary brand mark)
- Favicon
- Open Graph image
- Hero images
- Header graphics

### UI Components
- Button styles (primary, secondary)
- Input field styles
- Border radius, padding, margins
- Component-specific colors and spacing

### Layout & Spacing
- Base spacing unit
- Grid configuration
- Header/footer heights
- Padding and margin values

### Brand Personality
- Tone (professional, playful, etc.)
- Energy level
- Target audience

## Usage Examples

### Basic scraping
```bash
python scripts/scrape_brand.py https://firecrawl.dev
```

### Custom output directory
```bash
python scripts/scrape_brand.py https://example.com --output-dir ./my-brand-data
```

### Using in Python code
```python
from scripts.scrape_brand import scrape_brand

brand_data = scrape_brand('https://example.com', output_dir='./output')
print(brand_data['colors'])
print(brand_data['typography'])
```

## Output Structure

The script creates:
- `{domain}_{timestamp}_brand.json` - Raw brand data
- `{domain}_{timestamp}_report.md` - Human-readable report
- `{domain}_{timestamp}_screenshot.png` - Full page screenshot
- `{domain}_{timestamp}_images/` - Downloaded brand images
  - `logo.{ext}` - Primary logo
  - `favicon.{ext}` - Favicon
  - `ogImage.{ext}` - Social media preview image

## Setup

1. Install dependencies:
```bash
pip install requests
```

2. Set Firecrawl API key:
```powershell
$env:FIRECRAWL_API_KEY='fc-YOUR-API-KEY'
```

Get your API key at: https://firecrawl.dev

## Advanced Usage

### Analyzing Multiple Sites

Create a batch script to analyze competitors:

```python
sites = [
    'https://competitor1.com',
    'https://competitor2.com',
    'https://competitor3.com'
]

for site in sites:
    scrape_brand(site, output_dir=f'./analysis/{site.split("//")[1]}')
```

### Extracting Specific Data

Access specific brand elements from the JSON output:

```python
import json

with open('example.com_20260129_brand.json') as f:
    brand = json.load(f)

# Get color palette
colors = brand['colors']
primary = colors['primary']
secondary = colors['secondary']

# Get typography
fonts = brand['typography']['fontFamilies']
heading_font = fonts['heading']
```

## API Reference

For detailed Firecrawl API information, see [references/firecrawl_api.md](references/firecrawl_api.md).

## Troubleshooting

**Error: FIRECRAWL_API_KEY not set**
- Set the environment variable with your API key

**Error: 401 Unauthorized**
- Check that your API key is valid
- Ensure the key starts with `fc-`

**Error: Rate limited**
- Wait before making more requests
- Consider using the `maxAge` parameter for caching

**Images not downloading**
- Some sites may block direct image downloads
- Check the JSON output for image URLs and download manually if needed
