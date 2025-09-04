# IPL-WEB-APP
A web interface for IPL statistics built with Flask, Jinja2, and HTML, powered by the IPL_API.
🏏 IPL-WEB-APP

A web interface for IPL statistics built with Flask, Jinja2, and HTML, powered by the IPL_API.

📌 Project Overview

IPL-WEB-APP is a web application that provides a user-friendly interface to query IPL statistics.
It connects with the IPL_API (from the previous project) to fetch records and display them on a webpage.

The app uses Flask with Jinja2 templating and HTML to create an interactive interface where users can select two IPL teams from dropdown menus. On clicking the “Find the Record” button, the app makes a request to the teamVsteam API and displays the head-to-head result directly on the webpage.

⚡ Features

Dropdown menu to select Team 1 and Team 2.

Button to fetch and display head-to-head records.

Integration with IPL_API for real-time data.

Clean UI with Jinja2 templating for dynamic rendering.

🛠️ Tech Stack

Flask (Backend Framework)

Jinja2 (Templating Engine)

HTML / CSS (Frontend UI)

IPL_API (Data Source)

📂 Project Structure
IPL-WEB-APP/
│── app.py              # Flask app
│── templates/
│   └── index.html      # Main page with dropdowns (Jinja2 templating)
│── static/             # (Optional) CSS, JS, images
│── README.md           # Project documentation

✨ Future Improvements

Add team-wise batting & bowling stats to the UI.

Display charts/graphs for better visualization.

Deploy the app with both API + UI on the cloud.
