from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

# Function to use x-rates.com to convert currencies
def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[0:-4])
    
    return rate


app = Flask(__name__)

# Endpoints
@app.route("/")
def home():
    return "<h1>Currency Rate API</hi> <p>Example URL: /api/v1/usd-euro</p>"

# Endpoint to get currency conversion rate
@app.route("/api/v1/<in_cur>-<out_cur>")
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    result_dictionary = {"input_currency": in_cur, "output_currency": out_cur, "rate": rate}
    return jsonify(result_dictionary)

app.run()