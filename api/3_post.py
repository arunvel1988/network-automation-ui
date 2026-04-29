import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My First API Post",
    "body": "Hello from Python",
    "userId": 1
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:")
print(response.json())
