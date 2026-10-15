# Flask Gold Rate Scraper

A simple Python web application built with Flask and BeautifulSoup that fetches today's gold rates for specific Indian cities from Groww.in.

## Folder Structure

To ensure the application runs correctly, organize your files like this:

```text
project-folder/
│
├── app.py                 # The main Python script (Flask backend)
├── README.md              # This documentation file
└── templates/
    └── index.html         # The frontend HTML interface
```

## Prerequisites

Before running the application, make sure you have Python installed on your system. You will also need to install the required Python libraries. Open your terminal or command prompt and run:

```bash
pip install Flask requests beautifulsoup4
```

## How to Run the App

1. Open your terminal or command prompt.
2. Navigate to your main `project-folder` where `app.py` is located.
3. Start the Flask development server by running:

```bash
python app.py
```

4. Once the server is running, open your web browser and navigate to: `http://127.0.0.1:5000/`
5. Type a city name (for example: `mumbai`, `delhi`, `chennai`) into the search box and click "Check Price".

## Important Notes on Web Scraping

* **Website Changes:** This application relies on the specific HTML structure of the target website (`class_="tb10Table"`). If the website updates its design or class names, the scraper might break and return a "Gold price not found" error. You will need to inspect the webpage and update the `app.py` script accordingly.
* **Data Formatting:** Currently, the script extracts all text from the table using `.get_text(strip=True)`. This might result in the text being clumped together. For a more structured output in the future, you can modify the BeautifulSoup code to iterate through individual table rows (`<tr>`) and data cells (`<td>`).
