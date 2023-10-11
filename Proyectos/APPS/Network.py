from scapy.all import *

target_ip = '172.22.0.1/24'

arp = ARP(pdst= target_ip)

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

paquete = ether/arp

respuesta = srp(paquete,timeout=2,verbose =0)[0]

clients = []

for sent, recieved in respuesta:
    clients+=[[recieved.psrc,recieved.hwsrc]]

total_ips = len(clients)
for i in range(total_ips):
    print("IP: {}    MAC:{}".format(clients[i][0].clients[i][1]))
