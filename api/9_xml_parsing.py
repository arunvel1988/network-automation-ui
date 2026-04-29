import xml.etree.ElementTree as ET

xml_data = """
<device>
    <name>router1</name>
    <ip>192.168.1.1</ip>
</device>
"""

root = ET.fromstring(xml_data)

print("Name:", root.find("name").text)
print("IP:", root.find("ip").text)
