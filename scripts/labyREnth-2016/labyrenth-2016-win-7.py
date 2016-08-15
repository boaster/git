#!/usr/bin/env python

# flag: PAN{did_1_mention_th0se_pupp3ts_fr34ked_m3_out_recent1y?}

from string import maketrans
from pwn import *

key = "UDYs1D7bNmdE1o3g5ms1V6RrYCVvODJF1DpxKTxAJ9xuZW=="
data = ("423658474c414359595564776f647570557446306765614"
	"5354e4b6e66356754694b7867776657434a64693849712f6233"
	"36536864592f677331386d325677706b544a506d67303346447"
	"06176764a4633456341583853556b72627049315436315a474b6"
	"e72624439676b6637396571693467694134754b594576394f2f4"
	"97733476f646b68643074423965316f6a516757343330372f4f5"
	"3547457497a794556684862716b563639342b66535a4c4437465"
	"94d61383051594a51354a52562f423658474c414359595564776"
	"f6475705574463067656145354e4b6e663567542f59637a2f507"
	"4742f713d3d").decode('hex')

base64fixTable = maketrans("qtgJYKa8y5L4flzMQ/BsGpSkHIjhVrm3NCAi9cbeXvuwDx+R6dO7ZPEno21T0UFW", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");

def correctbase64(str):
	    return str.translate(base64fixTable)

def enkrypt(fset, sset):
	k = [u32('AWil'), u32('dKey'), u32('Appe'), u32('ars!')]
	kc = 0
	var_1 = 0x9E3769B9
	f_four = fset
	s_four = sset

	for _ in range(32):
		esi = kc + k[kc & 3]
		eax = ( ((s_four << 4) ^ (s_four >> 5)) + s_four ) & 0xffffffff

		f_four = ((eax ^ esi) + f_four) & 0xffffffff

		eax = ( ((f_four << 4) ^ (f_four >> 5)) + f_four ) & 0xffffffff

		kc = (kc + var_1 + 0x1000) & 0xffffffff
		edx = ((kc >> 0xb) & 3)
		esi = (kc + k[edx])
		s_four = ((eax ^ esi) + s_four) & 0xffffffff

	return f_four, s_four

def decrypt(fset, sset):
	k = [u32('AWil'), u32('dKey'), u32('Appe'), u32('ars!')]
	kc = 0xc6ef3720			# restored
	var_1 = 0x9E3769B9		# constant
	f_four = fset
	s_four = sset

	for _ in range(32):
		a = f_four
		b = s_four
		edx = (kc >> 0xb) & 3
		esi = (kc + k[edx])
		kc = (kc - var_1 - 0x1000) & 0xffffffff

		eax = ( ((f_four << 4) ^ (f_four >> 5)) + f_four ) & 0xffffffff

		s_four = (b - (eax ^ esi)) & 0xffffffff

		esi = kc + k[kc & 3]
		eax = ( ((s_four << 4) ^ (s_four >> 5)) + s_four ) & 0xffffffff
		f_four = (a - (eax ^ esi)) & 0xffffffff

	return f_four, s_four


data = correctbase64(data).decode('base64').strip('DINGPAD')
assert(len(data) % 8 == 0)
d = []

for i in range(0, len(data), 8):
	d.append( [data[i:i+8][:4], data[i:i+8][4:]] )

final = ""

for i in d:
	a, b = decrypt(u32(i[0]), u32(i[1]))
	final += p32(a)
	final += p32(b)

print final


