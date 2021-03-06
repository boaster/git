#!/usr/bin/env python

'''
root@userpc:~# python ./labyrenth-win6-brute.py
0x2d
0x2e
0x2f
0x30
0x31
0x32
0x33
0x34
0x35
0x36
0x37
0x38
Found with key: b00!9kLA@jf
PAN{th0se_puPP3ts_creeped_m3_out_and_I_h4d_NIGHTMARES}

0x39
root@userpc:~#
'''

import sys

buf = [x for x in range(0x100)]
#key = map(ord, "b00!4mWF?ij")
flag = [0xBA, 0xAF, 0x4D, 0x55, 0x3C, 0xE3, 0x03, 0x22, 0xB0, 0xDF, 0xF3, 0xD3, 0x57, 0xD0, 0xE1, 0x40, 0xF9, 0x13, 0x1F, 0xBA, 0x8D, 0x12, 0xF1, 0xFF, 0x48, 0xC2, 0x8E, 0x00, 0xFD, 0x54, 0x97, 0x9D, 0x75, 0x71, 0x30, 0x8F, 0x43, 0x28, 0xFE, 0x69, 0x36, 0x47, 0x8F, 0xA2, 0xEF, 0x49, 0x74, 0x7C, 0xE1, 0x4C, 0x6F, 0x4F, 0xD4, 0x82]

def decrypt(key, buf):
	bl = 0
	nbuf = buf[:]
	for c in range(0x100):
		al = nbuf[c]
		bl = (bl + key[c % len(key)]) & 0xff
		bl = (bl + al) & 0xff
		ah = nbuf[bl]
		nbuf[c] = ah
		nbuf[bl] = al
	return nbuf

def decrypt2(flag, buf):
	al = 0
	nflag = flag[:]
	for f in range(1, len(flag)+1):
		dl = buf[f]
		al = (al + dl) & 0xff
		cl = buf[al]
		buf[f] = cl
		buf[al] = dl
		cl = (cl + dl) & 0xff
		cl = buf[cl]
		nflag[f-1] ^= cl
	return nflag

for z in range(0x2d, 0x3a):
	for a in range(0x5e, 0x7d):
		for b in range(0x20, 0x7d):
			for c in [0x46, 0x42, 0x41]:
				for d in [0x3f, 0x40, 0x41, 0x42]:
					for e in [0x69, 0x6a]:
						for f in [0x6a,0x72,0x5e,0x66,0x6e,0x62]:
							key = [98, 0x30, 0x30, 0x21, z, a, b, c, d, e, f]
							buf1 = decrypt(key, buf)
							final = decrypt2(flag, buf1)
							if final[0] == 80 and final[1] == 0x41 and final[2] == 78:
								print "Found with key: " + ''.join(map(chr, key))
								print ''.join(map(chr, final))
								print
	print hex(z)
#						print map(hex, buf)
#						print
#						if f == 0x23:
#							sys.exit(1)
