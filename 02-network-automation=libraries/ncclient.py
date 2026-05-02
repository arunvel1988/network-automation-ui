from ncclient import manager
import yaml

with open("devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]

for dev in devices:
    print(f"\n==== {dev['name']} ====")

    with manager.connect(
        host=dev["ip"],
        port=830,
        username=dev["username"],
        password=dev["password"],
        hostkey_verify=False
    ) as m:

        filter = """
        <filter>
          <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
        </filter>
        """

        response = m.get(filter)
        print(response.xml)
