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

print(get_currency("CAD", "USD"))