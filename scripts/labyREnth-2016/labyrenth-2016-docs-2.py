#!/usr/bin/env python

x = [171,184,42,184,88,26,47,154,20,219,203,130,52,19,180,214,156,94,186,74,30,248,119,235,139,130,175,141,179,197,8,204,252]

def suchcrypto(sMessage, strKey):
	s = [0] * 256
	k = [0] * 256
	final = []
	kLen = len(strKey)
	for i in range(256):
		s[i] = i
		k[i] = ord(strKey[i % kLen])

	j = 0
	for i in range(256):
		j = (j + k[i] + s[i]) % 256
		temp = s[i]
		s[i] = s[j]
		s[j] = temp

	x = 0
	y = 0
	for i in range(1, 3073):
		x = (x + 1) % 256
		y = (y + s[x]) % 256
		temp = s[x]
		s[x] = s[y]
		s[y] = temp

	for i in range(1, len(sMessage)+1):
		x = (x + 1) % 256
		y = (y + s[x]) % 256
		temp = s[x]
		s[x] = s[y]
		s[y] = temp
 
		final.append(s[ (s[x] + s[y] ) % 256] ^ ord(sMessage[i-1]))
	return final

flag = 'PAN{'

for i in range(4, len(x)):
	for y in range(0x20, 0x7b):
		a = suchcrypto( (flag + chr(y)).ljust(32, 'A') + '}', "General Vidal")
		if a[i] == x[i]:
			flag += chr(y)
			break

print flag + '}'

#print x
#print suchcrypto( ('PAN{L').ljust(32, 'A') + '}', "General Vidal")