#!/usr/bin/env python

# flag: PAN{th4t5_4_pr311y_dum8_w4y_10_us3_r3g3x}

from pwn import *

regx = open('labyrenth-2016-random-2.regx', 'r').read().strip()[39:].replace('.{', '').replace('}', ' ').split('|')

regx_d = {}

for i in range(191):
	regx_d[str(i)] = 'Z'

for i in regx:
	regx_d[i.split(' ')[0]] += i.split(' ')[1]


good_chars = '0mglo8sc1enC3'

final = ''

for i in range(191):
	for g in good_chars:
		if g not in regx_d[str(i)]:
			final += g

r = remote('52.27.101.106', 2600)
r.recvuntil('Enter your key:\n')
r.sendline(final)
print
print r.recv()
