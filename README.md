# IPL Web App

A Flask web application displaying IPL statistics for the 2008–2022 seasons. Built on top of the [IPL API](https://ipl-api-t4ek.onrender.com) with a dark-themed UI, real-time data rendering, and modular Flask routing.

**Live App:** https://ipl-webapp.onrender.com

## Tech Stack

- Python, Flask, Jinja2
- Pandas (via IPL API)
- HTML, CSS (custom dark theme)

## Pages

| Route | Description |
|-------|-------------|
| `/` | Home — IPL champions history |
| `/teamvteam` | Head-to-head record between any two teams |
| `/team` | Full team record + win/loss vs every opponent |
| `/batsman` | Batsman career stats + performance vs each team |
| `/bowler` | Bowler career stats + performance vs each team |
| `/season` | Season overview — runs, wickets, top performers |

## Setup (Local)

This app depends on the IPL API running locally. Start the API first:

```bash
# Terminal 1 — API (port 5000)
cd IPL_API
python app.py

# Terminal 2 — Web app (port 8080)
cd ipl_webapp
python app.py
```

Then open `http://localhost:8080` in your browser.

## Project Structure

```
ipl_webapp/
├── app.py                  # Flask routes, API calls
└── templates/
    ├── base.html           # Shared layout, nav, CSS
    ├── index.html          # Home page
    ├── teamvteam.html      # Head-to-head page
    ├── team.html           # Team record page
    ├── batsman.html        # Batsman stats page
    ├── bowler.html         # Bowler stats page
    └── season.html         # Season stats + top performers
```

## Key Design Decisions

- **Modular routing** — each page is a separate Flask route with its own template, making it easy to add new pages independently.
- **API-first architecture** — the web app never touches the data directly. All data comes through the IPL API, keeping the two repos fully decoupled.
- **Graceful error handling** — if the API is down or returns no data, pages show an empty state instead of crashing.
