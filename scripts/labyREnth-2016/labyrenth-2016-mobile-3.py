#!/usr/bin/env python

# Flag: PAN{Th4t's_My_S3cr3t_N0boDy_Def34ts_th3_HOUNDS}

'''
B A d P u z z l 3 r  !  \x1e  N  o 
B A d P u z z l 3 r  !  \x1e  o  k 
1 2 3 4 5 6 7 8 9 10 11 12   13 14
                              o  N
BAdPuzzl3f!lok
BAdPuzzl3f!loN
'''

def do_xor(k, ct):
	pt = ''
	for i in range(len(ct)):
		pt += chr( (ct[i] ^ ord(k[i % len(k)]) ) & 0xff )
	return pt

def decrypt_2(k, ct):
	num = 171
	pt = ''
	for i in range(len(ct)):
		pt += chr( (ct[i] ^ ord(k[i % len(k)]) +num) & 0xff )
		num = (num + 1) % 256
	return pt

#print do_xor("kt@Jf", "3f1c2533460815352d0e1f543925134b4e3c".decode('hex')) 
#print do_xor("SECRET_key", '0a2a367533317f0c0a0d73312c7224207f07001820316326372d71'.decode('hex'))
#v = decrypt('%lka$', '670d190a04670d190a'.decode('hex'))
#v = decrypt('a', '43290843414c2b0e1209'.decode('hex'))
#print do_xor('$@#^%!', '7028467e4d4e512e472d05445723422e404505'.decode('hex'))
#print do_xor('xka1lrjf', '2b040c54181a03081f4b125e01171e0e11050611151d1f461e0a085d4c01050b1d1f095802154a1517060445041b0401'.decode('hex'))
#print do_xor('ioak', '210014050d1c41190c03040a1a0a054a'.decode('hex'))
'''
for a in range(0x100):
	for b in range(0x100):
		for c in range(0x30, 0x7b):
			if do_xor(chr(a) + chr(b) + chr(c), "052d15".decode('hex')) == 'DIE':
				print "Found: " + chr(a) + chr(b) + chr(c)
'''

infile = bytearray(open('labyrenth-mobile-3.jpg', 'r').read())
outfile = open('labyrenth-mobile-3-flag.jpg', 'w')
key = 'BAdPuzzl3r!?aNoJ'
#                 ?

outfile.write(decrypt_2(key, infile))

#print decrypt_2(key, infile)

#for i in range(0x100):
#	data = decrypt_2('BAdPuzzl3r!?aNo' + chr(i), infile)
#	if 'Exif\x00\x00\x4d\x4d' in data:
#		print chr(i)







