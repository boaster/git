# ctf.infosecinstitute.com: Level 13
**Bounty:** $130
**Description:**

> WHAT THE HECK HAPPENED HERE? IT SEEMS THAT THE CHALLENGE HERE IS GONE? CAN YOU FIND IT? CAN YOU CHECK IF YOU CAN FIND THE BACKUP FILE FOR THIS ONE? I'M SORRY FOR MESSING UP :(

## Write-up

After looking for files with some best practices file extensions like .backup, .bak, _backup... I found file /levelfourteen.php.old to be present. After downloading it, there was a php source code commented out.


	<?php 

	* <img src="img/clippy1.jpg" class="imahe" /> <br /> <br />

	<p>Do you want to download this mysterious file?</p>

	<a href="misc/imadecoy">
	<button class="btn">Yes</button>
	</a>

	<a href="index.php">
	<button class="btn">No</button>
	</a>
	*/

	?>

Now let's download the misc/imadecoy [file](imadecoy).
```bash
$ file imadecoy
imadecoy: tcpdump capture file (little-endian) - version 2.4 (Linux "cooked", capture length 65535)
```

OK, we are dealing with another packet capture. Let's looks at the Protocol Hierarchy.

```bash
$ tshark -nnr imadecoy -qz  io,phs

===================================================================
Protocol Hierarchy Statistics
Filter:

sll                                      frames:713 bytes:143926
  ip                                     frames:710 bytes:143649
    tcp                                  frames:168 bytes:97794
      http                               frames:34 bytes:39046
        data-text-lines                  frames:7 bytes:4497
          tcp.segments                   frames:1 bytes:359
        media                            frames:2 bytes:8900
          tcp.segments                   frames:1 bytes:456
        image-gif                        frames:3 bytes:1750
        png                              frames:1 bytes:1955
      data                               frames:2 bytes:308
    udp                                  frames:542 bytes:45855
      dns                                frames:530 bytes:42023
      data                               frames:12 bytes:3832
  arp                                    frames:2 bytes:106
    vssmonitoring                        frames:1 bytes:62
  ipv6                                   frames:1 bytes:171
    udp                                  frames:1 bytes:171
      dns                                frames:1 bytes:171
===================================================================
$ tshark -nnr imadecoy -qz ip_hosts,tree
===================================================================
IP Addresses           value	        rate	     percent
-------------------------------------------------------------------
IP Addresses            710       0.005819
10.0.2.15                12       0.000098           1.69%
144.76.14.145             3       0.000025           0.42%
127.0.0.1              1396       0.011442         196.62%
193.11.164.243            6       0.000049           0.85%
224.0.0.251               1       0.000008           0.14%
83.149.127.140            2       0.000016           0.28%
===================================================================
$
```

Again, just like Level 6, we see a lot of traffic from 127.0.0.1, this time it's mostly HTTP. We know that abnormal, so let's extract all the HTTP objects from the whole pcap. Open wireshark, load the pcap and select File -> Export Object -> HTTP. Now "Save All" to a new directory. This will save all files transfered via HTTP.

```bash
$ ls imadecoy_extract/
Fixedsys500c.woff back.gif          bootstrap.css     custom.css        honeypy           image2.gif        img(1)
HoneyPY.PNG       blank.gif         bootstrap.min.js  favicon.ico       honeypy(1)        img               jquery.js
$
```
Browsing to the directory and opening the [HoneyPY.PNG](HoneyPY.PNG) file, we see the flag.
infosec_flagis_morepackets
## Links
* <http://ctf.infosecinstitute.com/levelthirteen.php>

