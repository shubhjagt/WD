from scapy.all import *
def handler(packet):
	print(packet.summary())
sniff(iface='ens33',prn=handler,store=0)
