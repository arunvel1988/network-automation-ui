import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("First Post:")
print(data[0])
