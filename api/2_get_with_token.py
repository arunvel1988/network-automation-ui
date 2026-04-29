import requests

url = "https://api.example.com/data"

token = "my_secret_token_123"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

if response.status_code == 200:
    print(response.json())
else:
    print("Request Failed:", response.text)
