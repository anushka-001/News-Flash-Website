# Attention-Span News Flash

**Generate a custom “30 s / 2 min / 5 min” news digest on demand.**

A tiny FastAPI + CrewAI service that pulls today’s top headlines, then uses an LLM agent to craft a length-constrained summary you can read in seconds.

---

## 📦 Features

- Fetch top headlines from NewsData.io  
- Summarize with a configurable reading time (0.5, 2, or 5 minutes)  
- Orchestrated by lightweight AI agents (CrewAI + OpenAI)  
- One endpoint: `/flash?minutes={0.5|2|5}`

---

## 🚀 Quickstart

1. **Clone**  
   ```bash
   git clone https://github.com/you/attention-span-news-flash.git
   cd attention-span-news-flash
