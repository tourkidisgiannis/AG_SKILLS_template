#!/usr/bin/env python3
"""
Brand Scraper - Extract brand identity from websites using Firecrawl

Usage:
    python scrape_brand.py <url> [--output-dir <dir>]

Examples:
    python scrape_brand.py https://firecrawl.dev
    python scrape_brand.py https://example.com --output-dir ./brand-data
"""

import os
import sys
import json
import requests
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, will try to use environment variables directly
    pass

def scrape_brand(url, output_dir="brand_output"):
    """
    Scrape brand data from a URL using Firecrawl API.
    
    Args:
        url: Website URL to scrape
        output_dir: Directory to save outputs (default: brand_output)
    
    Returns:
        dict: Brand data including colors, fonts, images, etc.
    """
    # Get API key from environment
    api_key = os.getenv('FIRECRAWL_API_KEY')
    if not api_key:
        print("❌ Error: FIRECRAWL_API_KEY environment variable not set")
        print("   Set it with: $env:FIRECRAWL_API_KEY='fc-YOUR-API-KEY'")
        sys.exit(1)
    
    print(f"🔍 Scraping brand data from: {url}")
    
    # Call Firecrawl API with branding format
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'url': url,
        'formats': ['branding', 'markdown', 'screenshot']
    }
    
    try:
        response = requests.post(
            'https://api.firecrawl.dev/v2/scrape',
            headers=headers,
            json=payload,
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        
        if not data.get('success'):
            print(f"❌ API returned error: {data}")
            sys.exit(1)
            
        result = data.get('data', {})
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error calling Firecrawl API: {e}")
        sys.exit(1)
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Extract domain name for file naming
    domain = urlparse(url).netloc.replace('www.', '')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_name = f"{domain}_{timestamp}"
    
    # Save branding data as JSON
    branding_data = result.get('branding', {})
    json_path = output_path / f"{base_name}_brand.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(branding_data, f, indent=2)
    print(f"✅ Saved brand data: {json_path}")
    
    # Download images
    images_dir = output_path / f"{base_name}_images"
    images_dir.mkdir(exist_ok=True)
    
    image_urls = branding_data.get('images', {})
    downloaded_images = {}
    
    for img_type, img_url in image_urls.items():
        if img_url:
            try:
                img_response = requests.get(img_url, timeout=30)
                img_response.raise_for_status()
                
                # Determine file extension
                ext = Path(urlparse(img_url).path).suffix or '.png'
                img_path = images_dir / f"{img_type}{ext}"
                
                with open(img_path, 'wb') as f:
                    f.write(img_response.content)
                
                downloaded_images[img_type] = str(img_path)
                print(f"✅ Downloaded {img_type}: {img_path}")
            except Exception as e:
                print(f"⚠️  Failed to download {img_type}: {e}")
    
    # Save screenshot if available
    screenshot_url = result.get('screenshot')
    if screenshot_url:
        try:
            screenshot_response = requests.get(screenshot_url, timeout=30)
            screenshot_response.raise_for_status()
            screenshot_path = output_path / f"{base_name}_screenshot.png"
            with open(screenshot_path, 'wb') as f:
                f.write(screenshot_response.content)
            print(f"✅ Saved screenshot: {screenshot_path}")
        except Exception as e:
            print(f"⚠️  Failed to download screenshot: {e}")
    
    # Generate markdown report
    markdown_content = result.get('markdown', '')
    report = generate_brand_report(url, branding_data, downloaded_images, markdown_content)
    
    report_path = output_path / f"{base_name}_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"✅ Generated report: {report_path}")
    
    print(f"\n✨ Brand scraping complete! Output saved to: {output_path}")
    return branding_data


def generate_brand_report(url, branding, images, markdown_content):
    """Generate a comprehensive markdown report of brand data."""
    
    report = f"""# Brand Analysis Report

**Website**: {url}  
**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Color Scheme

**Mode**: {branding.get('colorScheme', 'N/A')}

### Brand Colors
"""
    
    colors = branding.get('colors', {})
    if colors:
        report += "\n| Color Type | Hex Value |\n|------------|----------|\n"
        for color_type, hex_value in colors.items():
            report += f"| {color_type} | `{hex_value}` |\n"
    else:
        report += "\nNo color data available.\n"
    
    report += "\n## Typography\n\n"
    
    typography = branding.get('typography', {})
    
    # Font families
    font_families = typography.get('fontFamilies', {})
    if font_families:
        report += "### Font Families\n\n"
        for usage, family in font_families.items():
            report += f"- **{usage}**: {family}\n"
    
    # Font sizes
    font_sizes = typography.get('fontSizes', {})
    if font_sizes:
        report += "\n### Font Sizes\n\n"
        for element, size in font_sizes.items():
            report += f"- **{element}**: {size}\n"
    
    # Font weights
    font_weights = typography.get('fontWeights', {})
    if font_weights:
        report += "\n### Font Weights\n\n"
        for weight_name, weight_value in font_weights.items():
            report += f"- **{weight_name}**: {weight_value}\n"
    
    # Fonts list
    fonts = branding.get('fonts', [])
    if fonts:
        report += "\n### Detected Fonts\n\n"
        for font in fonts:
            family = font.get('family', 'Unknown')
            report += f"- {family}\n"
    
    report += "\n## Spacing & Layout\n\n"
    
    spacing = branding.get('spacing', {})
    if spacing:
        for key, value in spacing.items():
            report += f"- **{key}**: {value}\n"
    
    report += "\n## UI Components\n\n"
    
    components = branding.get('components', {})
    if components:
        for component_name, component_data in components.items():
            report += f"\n### {component_name}\n\n"
            if isinstance(component_data, dict):
                for prop, value in component_data.items():
                    report += f"- **{prop}**: {value}\n"
    
    report += "\n## Brand Images\n\n"
    
    if images:
        for img_type, img_path in images.items():
            report += f"- **{img_type}**: `{img_path}`\n"
    else:
        report += "No images downloaded.\n"
    
    report += "\n## Brand Personality\n\n"
    
    personality = branding.get('personality', {})
    if personality:
        for trait, value in personality.items():
            report += f"- **{trait}**: {value}\n"
    
    report += "\n---\n\n## Page Content Preview\n\n"
    
    if markdown_content:
        # Include first 500 characters of content
        preview = markdown_content[:500]
        if len(markdown_content) > 500:
            preview += "..."
        report += f"{preview}\n"
    
    return report


def main():
    if len(sys.argv) < 2:
        print("Usage: python scrape_brand.py <url> [--output-dir <dir>]")
        print("\nExamples:")
        print("  python scrape_brand.py https://firecrawl.dev")
        print("  python scrape_brand.py https://example.com --output-dir ./brand-data")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Parse optional output directory
    output_dir = "brand_output"
    if len(sys.argv) >= 4 and sys.argv[2] == '--output-dir':
        output_dir = sys.argv[3]
    
    scrape_brand(url, output_dir)


if __name__ == "__main__":
    main()
