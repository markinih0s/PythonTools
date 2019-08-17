#!/usr/bin/env python

#made_by markinih0s

import scapy.all as scapy
import optparse

#options function
def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--range", dest="range", help="Target IP / IP range")
    parser.add_option("--example", help='Ex : python network_scanner.py -r 192.168.1.0/24')
    (options, arguments) = parser.parse_args()    
    if not options.range:
        parser.error("[-] - Please specify an ip Range to scan, or use -h, --help for more info and EXAMPLE.")
    return options


#scanning function
def scan(ip):
    #create ARP Request directed to broadcast MAC asking for IP    
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    #Broadcast Response
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1.5, verbose=False)[0]

    #Iterating over lists & Analazing packet    
    clients_list = []
    for element in answered_list:
        clients_dictionary = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        #Adding client_dict as an element into client list
        clients_list.append(clients_dictionary)
    return clients_list

#printing result function
def print_result(results_list):
    print("IP:\t\t\t\t MAC Address:")
    print("-------------------------------------------------")  
    for client in results_list:
        print(client["ip"] + "\t\t\t" + client["mac"])
        print("-------------------------------------------------")    

#calling the functions
options = get_options()
scan_result = scan(options.range)
print_result(scan_result)