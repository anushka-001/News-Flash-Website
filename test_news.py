import os
import httpx
import json
from datetime import datetime

# Set API key directly
API_KEY = "pub_db16bad9cd534491b7936a5270478989"

def test_news_api():
    print("\nFetching top 5 headlines from NewsData.io...\n")
    
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": API_KEY,
        "language": "en",
        "country": "us,gb,in",  # US, UK, and India news
        "category": "top",      # Top headlines
        "size": "5"            # Request 5 articles
    }
    
    try:
        print("Making API request...")
        client = httpx.Client(timeout=30.0)
        response = client.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error: API returned status code {response.status_code}")
            print(f"Response: {response.text}")
            return
            
        data = response.json()
        results = data.get("results", [])
        
        if not results:
            print("No headlines found!")
            return
            
        print("\n📰 TOP 5 HEADLINES 📰")
        print("=" * 80)
        
        for i, article in enumerate(results[:5], 1):
            print(f"\n{i}. {article['title']}")
            print(f"   Source: {article.get('source_id', 'Unknown').upper()}")
            
            if article.get('description'):
                desc = article['description']
                if len(desc) > 200:
                    desc = desc[:197] + "..."
                print(f"   {desc}")
            
            if article.get('link'):
                print(f"   Link: {article['link']}")
                
            if article.get('pubDate'):
                print(f"   Published: {article['pubDate']}")
                
            print("-" * 80)
            
    except httpx.TimeoutException:
        print("Error: Request timed out. Please try again.")
    except httpx.RequestError as e:
        print(f"Error making request: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    test_news_api() 