# main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from App.tools.news_fetcher import fetch_headlines, CATEGORIES

# ── Bootstrap ────────────────────────────────────────────────────
os.environ["NEWSDATA_KEY"] = "pub_db16bad9cd534491b7936a5270478989"  # Set API key directly
app = FastAPI(title="News Flash API")

# ── Template setup ────────────────────────────────────────────────
templates = Jinja2Templates(directory="App/templates")

# ── Routes ────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, category: str = "top"):
    """
    Render the homepage with top headlines.
    """
    try:
        articles = fetch_headlines(max_items=10, category=category)
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request, 
                "headlines": articles,
                "categories": CATEGORIES,
                "current_category": category
            }
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"News API error: {str(e)}")

# ── Health check ─────────────────────────────────────────────────
@app.get("/ping")
async def ping():
    return {"status": "ok"}
