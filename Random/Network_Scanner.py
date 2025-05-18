import scapy.all as scapy
import socket
import requests
from tabulate import tabulate


def gat_mac_vendor(mac_address):
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return 'Unknown Vendor'


def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return 'Unknown'


def scan_network(network):
    arp_request = scapy.ARP(pdst = network)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=3, verbose=False)[0]

    devices = []
    for element in answered_list:
        ip = element[1].psrc
        mac = element[1].hwsrc
        hostname = get_hostname(ip)
        vendor = gat_mac_vendor(mac)
        devices.append({'IP': ip, 'MAC': mac, 'Hostname': hostname, 'Vendor': vendor})

    return devices


if __name__ == '__main__':
    network = input('Enter the network (e.g. 192.168.178.0/24): ')
    devices = scan_network(network)

    if devices:
        print('Connected devices on the network: \n')
        print(tabulate(devices, headers='keys', tablefmt='grid'))
    else:
        print('No devices found.')
