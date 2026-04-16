import socket

services = [
    {"name": "flask",    "port": 5000, "critical": True},
    {"name": "postgres", "port": 5432, "critical": True},
    {"name": "redis",    "port": 6379, "critical": False},
    {"name": "nginx",    "port": 80,   "critical": False},
]

for service in services:
    s = socket.socket()
    try:
        s.connect(("localhost", service["port"]))
        print(f"service {service['name']} : OK")
    except:
        if service["critical"] == True:
            print(f"service {service['name']} : CRITICAL")
        else:
            print(f"service {service['name']} : WARNING")
