from napalm import get_network_driver
import yaml

with open("devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]

driver = get_network_driver("ios")

for dev in devices:
    print(f"\n==== {dev['name']} ====")

    device = driver(dev["ip"], dev["username"], dev["password"])
    device.open()

    facts = device.get_facts()
    interfaces = device.get_interfaces()

    print("\n--- Facts ---")
    print(facts)

    print("\n--- Interfaces ---")
    print(interfaces)

    device.close()
