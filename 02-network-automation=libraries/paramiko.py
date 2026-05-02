import paramiko
import yaml

with open("devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]

for dev in devices:
    print(f"\n==== {dev['name']} ====")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(dev["ip"],
                username=dev["username"],
                password=dev["password"])

    shell = ssh.invoke_shell()

    shell.send("terminal length 0\n")
    shell.send("show ip route\n")

    import time
    time.sleep(2)

    output = shell.recv(5000).decode()
    print(output)

    ssh.close()
