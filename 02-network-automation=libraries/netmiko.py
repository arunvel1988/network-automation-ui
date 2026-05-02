from netmiko import ConnectHandler
import yaml

# Load devices
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]

for dev in devices:
    print(f"\n==== Connecting to {dev['name']} ====")

    device = {
        "device_type": "cisco_ios",
        "host": dev["ip"],
        "username": dev["username"],
        "password": dev["password"],
    }

    conn = ConnectHandler(**device)

    # 1. Show command
    output = conn.send_command("show ip interface brief")
    print("\n--- Interfaces ---")
    print(output)

    # 2. Push config
    config = [
        "interface loopback10",
        f"ip address 10.10.{1 if dev['name']=='R1' else 2}.1 255.255.255.255"
    ]

    result = conn.send_config_set(config)
    print("\n--- Config Applied ---")
    print(result)

    conn.disconnect()
