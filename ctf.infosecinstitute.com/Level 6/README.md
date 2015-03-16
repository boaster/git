# ctf.infosecinstitute.com: Level 6
**Bounty:** $60
**Description:**

> Do you want to download [sharkfin.pcap](sharkfin.pcap) file?

## Write-up

Looking at the content of the pcap, most of the traffic is HTTP, HTTPS and the rest is noise. However one packet that doesn't seem right is UDP from 127.0.0.1 to 127.0.0.1.
We know that this is not normal traffic but instead it's crafted.

```bash
$ tcpdump -nnr sharkfin.pcap -As0 udp and host 127.0.0.1
reading from file sharkfin.pcap, link-type EN10MB (Ethernet)
14:59:54.303760 IP 127.0.0.1.32769 > 127.0.0.1.139: UDP, length 44
E..H..@.@.<..............4..696e666f7365635f666c616769735f736e6966666564
$ 
```
This doesn't look like NETBIOS traffic at all, right ? Let's convert from hex to ascii.

```bash
$ python -c 'print("\x69\x6e\x66\x6f\x73\x65\x63\x5f\x66\x6c\x61\x67\x69\x73\x5f\x73\x6e\x69\x66\x66\x65\x64")'
infosec_flagis_sniffed
```
