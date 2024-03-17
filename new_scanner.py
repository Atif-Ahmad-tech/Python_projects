import scapy.all as scapy

# Two functions One for ethernet and other for wireless

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    ans, unans= scapy.srp(arp_request_broadcast, timeout=1)     #  sent packet,add verbose=false for remove extra data
    # print(ans.summary()) #answerd packets 
    for answers in ans:
        print(answers[1].psrc) #the ip of second element in send recieve packet list
        print(answers[1].hwsrc) #the mac of second element in send recieve packet list
       
# def scan(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Dot11(type=2, subtype=4, addr1="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast / arp_request
#     ans, unans = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)

#     for answers in ans:
#         print(answers[1].psrc)  # the IP of the second element in send-receive packet list
#         print(answers[1].hwsrc) 
scan("192.168.43.174/24")