import requests
import json


query = input("What type of news are you instered in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-07-02&sortBy=publishedAt&apiKey=dbe57b028aeb41e285a226a94865f7a7"

r = requests.get(url)
news = json.loads(r.text)
print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------")