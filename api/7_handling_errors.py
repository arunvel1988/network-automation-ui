import requests

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()
    print("Success:", len(data), "records")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.ConnectionError:
    print("Connection Error")

except requests.exceptions.Timeout:
    print("Request Timed Out")

except Exception as e:
    print("Other Error:", e)
