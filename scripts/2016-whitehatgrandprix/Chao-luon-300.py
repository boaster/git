#!/usr/bin/env python

from pwn import *
import sys

def find_char(x, c):
	ks = []
	for i in range(x, 0x100):
		ks.append(i)
	for i in range(0, x):
		ks.append(i)

#	print map(hex, ks)

	edx = 0
	for i in range(0x100):
		esi = ks[i]
		edi = esi + c
		edx += edi
		edi = (edx & 0xff)
		r8 = ks[edi]
		ks[i] = r8
		ks[edi] = (esi & 0xff)

#	print map(hex, ks)

	edi = 0
	esi = 0
	final = 0
	name = 'GrandPrix'
	for i in range(9):
		edi += 1
		r9 = edi
		r10 = ks[edi]
		esi += r10
		r11 = (esi & 0xff)
		r12 = ks[r11]
		ks[r9] = r12
		ks[r11] = r10
		r12 = ord(name[i])
		r9 = ks[r9]
		r9 = (r9 + r10) & 0xff
		r9 = ks[r9]
		r12 ^= r9
		r9 = r12
		final += r9
#		print hex(final)
#	print map(hex, ks)
	return final


def local():

	key = [1324, 961, 1171, 1209, 943, 1157, 770, 957, 1003, 1392, 1120, 1167, 938, 1093, 1097, 1168, 1321, 1397, 1377, 892, 1379, 1394, 783, 832, 748, 1269, 1284, 867, 1059, 1288, 1288, 1370, 1461, 1267, 1074, 1193, 997, 1261, 1299, 1504, 1469, 1397, 1434, 986, 684, 1118, 1060, 1492, 918, 1046]

#	for i in range(0x100):
#		if find_char(key.index(1120), i) == 1120:
#			print "Found: " + chr(i)
	
	flag = ''
	alphabet = 'WhieHat0123456789bcdf\{\}'
	for i in range(len(key)):
		for c in range(len(alphabet)):
			if find_char(i, ord(alphabet[c])) == key[i]:
				flag += alphabet[c]
				print "Found: " + alphabet[c]
#				break
		print "Not Found: " + str(key[i])

	print flag
	
	# collisions
	# WhiteHat{6f2d70c4ab2b19e314cee34ffc98d81e48e84c26}
	# WhiteHat{6f2d70c4ab2b197314cee34ffc98d81e48e84c26}
	# WhiteHat{6f2d70c4ab2b19e314c2e34ffc98d81e48e84c26}
	# WhiteHat{6f2d70c4ab2b197314c2e34ffc98d81e48e84c26}
	# 



	


def exploit(r):
	r.recvuntil('Name: ')

	payload = "GrandPrix\nsecret"
	r.sendline(payload)

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        local()