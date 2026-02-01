# Firecrawl API Reference

Quick reference for using Firecrawl API to scrape brand data.

## Authentication

Set your API key as an environment variable:

```powershell
$env:FIRECRAWL_API_KEY='fc-YOUR-API-KEY'
```

## Branding Format

The `branding` format extracts comprehensive brand identity information:

```python
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')
result = firecrawl.scrape(url='https://example.com', formats=['branding'])
```

### Response Structure

```json
{
  "branding": {
    "colorScheme": "dark" | "light",
    "logo": "https://...",
    "colors": {
      "primary": "#FF6B35",
      "secondary": "#004E89",
      "accent": "#F77F00",
      "background": "#1A1A1A",
      "textPrimary": "#FFFFFF",
      "textSecondary": "#B0B0B0"
    },
    "fonts": [{"family": "Inter"}, {"family": "Roboto Mono"}],
    "typography": {
      "fontFamilies": {"primary": "Inter", "heading": "Inter", "code": "Roboto Mono"},
      "fontSizes": {"h1": "48px", "h2": "36px", "body": "16px"},
      "fontWeights": {"regular": 400, "medium": 500, "bold": 700}
    },
    "spacing": {"baseUnit": 8, "borderRadius": "8px"},
    "components": {
      "buttonPrimary": {
        "background": "#FF6B35",
        "textColor": "#FFFFFF",
        "borderRadius": "8px"
      }
    },
    "images": {
      "logo": "https://...",
      "favicon": "https://...",
      "ogImage": "https://..."
    }
  }
}
```

## Multiple Formats

Combine formats for comprehensive data:

```python
result = firecrawl.scrape(
    url='https://example.com',
    formats=['branding', 'markdown', 'screenshot']
)
```

## Error Handling

Common errors:
- **401 Unauthorized**: Invalid API key
- **429 Rate Limited**: Too many requests
- **500 Server Error**: Firecrawl service issue

## Rate Limits

Default rate limits apply. Use caching with `maxAge` parameter to reduce API calls:

```python
result = firecrawl.scrape(url='https://example.com', maxAge=600000)  # 10 min cache
```
