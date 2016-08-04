import pcap
import dpkt
a=pcap.pcap() 
a.setfilter('arp') 
for i,j in a: 
    tem=dpkt.ethernet.Ethernet(j) 
    print ("%s %x",i,tem)