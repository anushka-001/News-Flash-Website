# 📰 News Flash Website

A simple, static news site that pulls in today’s top headlines and shows them in a clean, card-based layout.

---

## How It Was Built

1. **Set up the repository and file structure**

   * Created a GitHub repo named `News-Flash-Website`.
   * Added these files and folders:

     * `index.html`
     * `css/styles.css`
     * `js/config.js`
     * `js/app.js`
     * `assets/` (images and icons)

2. **Created the HTML layout (`index.html`)**

   * Added a header with the site title and a light/dark toggle.
   * Inserted a category dropdown for selecting news topics.
   * Included a `<div id="news-container">` to host the news cards.

3. **Styled the page (`css/styles.css`)**

   * Defined CSS variables for colors and typography.
   * Designed a grid layout for news cards (image, headline, snippet, link).
   * Implemented light/dark mode using a CSS class switch.

4. **Configured the API key (`js/config.js`)**

   * Created a constant `API_KEY` placeholder:

     ```js
     const API_KEY = 'YOUR_NEWSAPI_KEY_HERE';
     ```

5. **Developed the JavaScript logic (`js/app.js`)**

   * Fetched data from NewsAPI:

     ```js
     fetch(`https://newsapi.org/v2/top-headlines?category=${category}&apiKey=${API_KEY}`)
     ```
   * Parsed the JSON and generated HTML cards for each article.
   * Injected the cards into `#news-container`.

6. **Added interactivity**

   * **Category filter:** Reloads news when the dropdown value changes.
   * **Theme toggle:** Switches CSS classes on `<body>` to change themes.

7. **Committed changes step by step**

   * Initial empty file commit
   * Added HTML layout
   * Added CSS styling
   * Set up config file
   * Implemented fetch and render logic
   * Enhanced interactivity (dropdown and theme switch)

8. **Deployed with GitHub Pages**

   * Configured GitHub Pages to serve from the `master` branch root.
   * Live URL: `https://anushka-001.github.io/News-Flash-Website/`

---

## Getting Started

### Prerequisites

* Any modern web browser
* (Optional) [Python](https://python.org) for a simple local server

### Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/anushka-001/News-Flash-Website.git
   cd News-Flash-Website
   ```

2. **Open** `index.html` in your browser
   *or*, start a local server:

   ```bash
   python -m http.server 8000
   # then visit http://localhost:8000
   ```

### Configuration

1. Sign up at [NewsAPI.org](https://newsapi.org) and get your API key.
2. Open `js/config.js` and replace the placeholder:

   ```js
   const API_KEY = 'YOUR_NEWSAPI_KEY_HERE';
   ```
3. Save and reload the page.

---

## Deployment

1. In the GitHub repo, go to **Settings → Pages**.
2. Under **Source**, select:

   * **Branch:** `master`
   * **Folder:** `/ (root)`
3. Click **Save**. Wait a moment for the site to publish.
4. Your site will be live at:

   ```
   https://anushka-001.github.io/News-Flash-Website/
   ```

---

## File Structure

```plaintext
News-Flash-Website/
├── index.html        ← Main page layout
├── css/
│   └── styles.css    ← Site styling
├── js/
│   ├── app.js        ← News fetching & rendering logic
│   └── config.js     ← API key configuration
└── assets/           ← Images & icons
```

---

## Contributing

1. Fork the repo
2. Create a branch:

   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add YourFeature"
   ```
4. Push to your branch and open a Pull Request.

---



---

*Built by Anushka Mishra*
