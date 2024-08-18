from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city'].lower()
        url = f"https://groww.in/gold-rates/gold-rate-today-in-{city}"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        price_tag = soup.find("table", class_="tb10Table")

        if price_tag:
            gold_price = price_tag.get_text(strip=True)
            return render_template('index.html', gold_price=gold_price, city=city.capitalize())
        else:
            return render_template('index.html', error="Gold price not found on the page.")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
