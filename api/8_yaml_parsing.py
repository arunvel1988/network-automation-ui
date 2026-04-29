import yaml

yaml_data = """
device:
  name: router1
  ip: 192.168.1.1
"""

data = yaml.safe_load(yaml_data)

print("Device Name:", data["device"]["name"])
print("IP:", data["device"]["ip"])
