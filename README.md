


# 🌐 Link Collector

**Link Collector** is a Django-powered web application that lets users scrape and collect all the hyperlinks from any given website URL. It displays the links in a structured table format, with options to delete them easily. Designed with Bootstrap 5, the app is fully responsive and user-friendly.

---

## ✨ Features

- 🔍 **URL Scraper** – Input any website URL to extract all related hyperlinks.
- 📄 **Tabular Display** – View the scraped links in a clean, organized table.
- 🗑️ **Delete All** – Remove all scraped links with one click.
- 📱 **Mobile Friendly** – Built with Bootstrap 5 for responsive design.

---

## 📸 Screenshot

<p align="center">
  <img src="https://github.com/Shani871/Link-Collector/blob/main/templates/Screenshot%202025-01-21%20at%2011.20.12%E2%80%AFPM.png" alt="Dashboard Screenshot" width="80%">
</p>

---

## ⚙️ Installation & Setup

Follow these steps to set up the project on your local machine:

```bash
# 1. Clone the repository
git clone https://github.com/Shani871/Link-Collector.git
cd Link-Collector

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver

🌐 Visit http://127.0.0.1:8000 in your browser.

⸻

🧑‍💻 How to Use
	1.	Paste a valid website URL in the input box.
	2.	Click the Scrape button to fetch all related links.
	3.	View the links displayed in a scrollable table.
	4.	Use the Delete All button to clear them from the database.

⸻

🛠️ Tech Stack

Layer	Technologies
Backend	Django (Python)
Scraping	BeautifulSoup (for HTML parsing)
Frontend	HTML, CSS, Bootstrap 5


⸻

🤝 Contributing

We welcome contributions from the community!
Follow these steps to contribute:

# Fork the repository
# Create your feature branch
git checkout -b feature/your-feature

# Commit your changes
git commit -m "Add feature"

# Push to your branch
git push origin feature/your-feature

# Open a pull request


⸻

📜 License

Licensed under the MIT License — free to use, modify, and distribute.

⸻

👤 Author

Shani Chauhan
📧 chauhanshani145@gmail.com

