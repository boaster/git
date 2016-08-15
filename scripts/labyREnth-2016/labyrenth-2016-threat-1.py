#!/usr/bin/env python

import sys

infile = open('labyrenth-2016-threat-1.txt', 'r').read().strip().split('\n')

final = ''
nums = []

mapp = []
flag = {}

for i in infile:
	n = i.split('.php?')[0][1:]
	n = n.decode('base64').strip()
	msg = i.split('?')[2].split('-')[0][::-1]
	msg += i.split('?')[1].split('&')[0][::-1]
	msg = msg.decode('base64').strip().replace('317', '')
	mapp.append(msg)
	flag[n] = msg[int(n)+8]
	nums.append(int(n))


print '\n'.join(mapp)

for i in range(40):
	if str(i) in flag:
		sys.stdout.write(flag[str(i)])
print
