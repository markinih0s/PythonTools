#!/usr/bin/env python

#made_by markinih0s

import subprocess
import optparse

#options function
def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change his MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="NEW MAC Address")
    parser.add_option("--example", help='Ex : python mac_changer.py -i eth0 -m 22:33:44:55:66:77')
    (options, arguments) = parser.parse_args()    
    if not options.interface:
        parser.error("[-] - Please specify INTERFACE by -i [interface], or use -h, --help for more info and EXAMPLE.")
    elif not options.new_mac:
        parser.error("[-] - Please specify MAC Address by -m [mac_address], or use -h, --help for more info and EXAMPLE.")     
    return options


#MAC Address commands changer executing by function
def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] - INTERFACE : " + interface + " AND " + "MAC Address : " + new_mac + " was successfully changed!")

#calling functions
options = get_options()
change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
