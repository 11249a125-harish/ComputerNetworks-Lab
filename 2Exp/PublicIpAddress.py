import json
import socket
from urllib.request import urlopen

# Get hostname
hostname = socket.gethostname()

# Get local IP address
try:
    local_ip = socket.gethostbyname(hostname)
except Exception:
    local_ip = "Unable to fetch local IP"

# Get public IP address
try:
    with urlopen("https://api.ipify.org?format=json", timeout=5) as response:
        data = json.load(response)
        public_ip = data.get("ip", "Unknown")
except Exception as e:
    public_ip = f"Unable to fetch public IP: {e}"

# Display the results
print("Hostname:", hostname)
print("Local IP:", local_ip)
print("Public IP:", public_ip)