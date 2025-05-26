import os, httpx, datetime, urllib.parse

CATEGORIES = [
    "top",
    "business",
    "entertainment",
    "environment",
    "food",
    "health",
    "politics",
    "science",
    "sports",
    "technology",
    "world"
]

def fetch_headlines(max_items: int = 20, category: str = "top") -> list[dict]:
    """Return a list of {title, url, source, description} dicts."""
    API_KEY = os.getenv("NEWSDATA_KEY")
    if not API_KEY:
        raise ValueError(f"NEWSDATA_KEY environment variable is not set. Current value: {API_KEY}")
    
    if category not in CATEGORIES:
        category = "top"
        
    params = {
        "apikey": API_KEY,
        "language": "en",
        "country": "us,gb,in",   # US, UK, and India news
        "category": category,    # Category parameter
    }
    
    try:
        url = "https://newsdata.io/api/1/news"
        resp = httpx.get(url, params=params, timeout=30.0)
        resp.raise_for_status()
        data = resp.json()
        
        if not data.get("results"):
            return []
            
        articles = []
        for article in data["results"][:max_items]:
            articles.append({
                "title": article.get("title", ""),
                "url": article.get("link", ""),
                "source": article.get("creator", ["Unknown Source"])[0] if article.get("creator") else "Unknown Source",
                "description": article.get("description", "No description available")
            })
            
        return articles
        
    except Exception as e:
        raise Exception(f"Failed to fetch news: {str(e)}")
