import requests
import yaml

requests.packages.urllib3.disable_warnings()

with open("devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]

for dev in devices:
    print(f"\n==== {dev['name']} ====")

    url = f"https://{dev['ip']}:443/restconf/data/ietf-interfaces:interfaces"

    headers = {
        "Accept": "application/yang-data+json"
    }

    response = requests.get(
        url,
        headers=headers,
        auth=(dev["username"], dev["password"]),
        verify=False
    )

    print(response.json())
