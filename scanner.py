import scapy.all as scapy
import requests

def get_vendor(mac):
    url = f"https://api.macvendors.com/{mac}"
    try:
        res = requests.get(url, timeout=2)
        return res.text if res.status_code == 200 else "N/A"
    except:
        return "Error"

def run_scan(ip):
    print(f"[!] Escaneando: {ip}")
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    answered = scapy.srp(broadcast/arp_req, timeout=2, verbose=False)[0]
    
    data = [["IP", "MAC Address", "Fabricante"]]
    for el in answered:
        vendor = get_vendor(el[1].hwsrc)
        data.append([el[1].psrc, el[1].hwsrc, vendor])
    return data