import requests

r = requests.get("https://newsapi.org/v2/everything?qInTitle=space&from=2022-05-27&to=2022-11-04&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c")
content = r.json()
# The type of this is a dictionary
print(type(content))
# So can get text using articles key - print first title
print(content["articles"][0]["title"])
print(content["articles"][0]["description"])

def get_news(topic, from_date, to_date, language="en", api_key="890603a55bfa47048e4490069ebee18c"):
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content["articles"]

    results = []
    for article in articles:
        results.append(f"TITLE\n {article['title']}, \nDESCRIPTION\n, {article['description']}")

print(get_news(topic="space", from_date="2022-08-01", to_date="2022-11-03"))