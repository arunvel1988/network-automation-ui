import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

updated_data = {
    "title": "Updated Title",
    "body": "Updated content",
    "userId": 1
}

response = requests.put(url, json=updated_data)

print("Status:", response.status_code)
print(response.json())
