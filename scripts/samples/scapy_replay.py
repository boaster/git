#!/usr/bin/env python

from scapy.all import *
from pwn import *

packetCount = 0

def customAction(packet):
    global packetCount
    packetCount += 1
    return "Packet #%s: %s ==> %s" % (packetCount, packet[0][1].src, packet[0][1].dst)

sniff(filter="icmp and dst host 127.0.0.1",iface='lo0', prn=customAction)
