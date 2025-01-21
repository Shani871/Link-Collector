# 🌐 Link Collector

Link Collector is a Django-based web application that allows users to enter a website URL and scrape all the related links from that website. The collected links are displayed in a table, making it easy to view and access them.

---

## ✨ Features

- 🔗 **Input URL:** Enter a website URL to scrape related links.
- 📋 **Link Display:** View all the links in a table format.
- 🗑️ **Delete Functionality:** Clear all the stored links with a single click.
- 📱 **Responsive Design:** Fully responsive UI built with Bootstrap 5.

---

## ⚙️ Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Shani871/Link-Collector.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Link-Collector
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

---

## 🛠️ Usage

1. 🌍 Enter the URL of the website you want to scrape in the input field.
2. 🖱️ Click the **Scrape** button to fetch all related links.
3. 📄 View the links displayed in the table.
4. 🗑️ Use the **Delete All** button to clear all the stored links.

---

## 🧰 Technologies Used

- **Backend:** Django 🐍
- **Frontend:** HTML, CSS, Bootstrap 5 🎨
- **Scraping:** BeautifulSoup (if used for scraping links) 🕵️‍♂️

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. 🍴 Fork the repository.
2. 🌱 Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. 💾 Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. 🚀 Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. 📝 Open a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📞 Contact

For any inquiries or feedback, please contact:

- **Name:** Shani871
- **GitHub:** [https://github.com/Shani871](https://github.com/Shani871)



<img src="https://github.com/Shani871/Link-Collector/blob/main/templates/Screenshot%202025-01-21%20at%2011.20.12%E2%80%AFPM.png" alt="Dashboard Screenshot" width="600">
