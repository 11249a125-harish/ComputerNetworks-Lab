# AIM: To simulate ARP and RARP address resolution using Python.

class ARP_RARP_Simulator:
    def __init__(self):
        self.arp = {
            "192.168.1.1": "00:0a:95:9d:68:16",
            "192.168.1.2": "00:0a:95:9d:68:17",
            "192.168.1.3": "00:0a:95:9d:68:18"
        }
        self.rarp = {v: k for k, v in self.arp.items()}

    def arp_request(self, ip):
        mac = self.arp.get(ip)
        print("MAC Address:", mac if mac else "Not found")

    def rarp_request(self, mac):
        ip = self.rarp.get(mac)
        print("IP Address:", ip if ip else "Not found")


if __name__ == "__main__":
    s = ARP_RARP_Simulator()

    s.arp_request("192.168.1.1")
    s.arp_request("192.168.1.100")

    s.rarp_request("00:0a:95:9d:68:16")
    s.rarp_request("00:0a:95:9d:68:99")

