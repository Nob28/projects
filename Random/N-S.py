import scapy.all as scapy

def scan_network(network):
    arp_request = scapy.ARP(pdst=network)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices = []
    for element in answered_list:
        devices.append({"IP": element[1].psrc, "MAC": element[1].hwsrc})

    return devices

network = input(": 192.168.178.0/24): ")
devices = scan_network(network)

print("das sind end_device : ")
for device in devices:
    print(f"IP: {device['IP']}, MAC: {device['MAC']}")
