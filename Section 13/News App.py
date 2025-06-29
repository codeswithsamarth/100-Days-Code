import requests

query = "Msbte 2025 Summer Result"  # Corrected spelling
api = "7770345e018241ef86a1889ef11b613e"
from_date = "2025-06-24"  # Correct format: YYYY-MM-DD

url = f"https://newsapi.org/v2/everything?q={query}&from={from_date}&sortBy=publishedAt&apiKey={api}"
print(url)

response = requests.get(url)

# Check HTTP status
if response.status_code != 200:
    print(f"Error: Received status code {response.status_code}")
    print(response.text)
else:
    data = response.json()
    if "articles" in data:
        articles = data["articles"]
        for article in articles:
            print(article.get('title'))
            print(article.get('url'))
    else:
        print("No 'articles' key in response.")
        print("Full response:", data)
