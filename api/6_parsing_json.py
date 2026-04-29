import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

for post in data[:5]:
    print("ID:", post["id"])
    print("Title:", post["title"])
    print("-" * 30)
