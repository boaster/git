#!/usr/bin/env python

import sys

infile = open(sys.argv[1], 'r')

one = ['1']
zero = ['0']

for num in infile:
	dic1 = num.strip().split()
	for string in dic1:
		strings = list(string)
		d = []
		while 1:
			if strings == one:
				print '1'
				break
			elif strings == zero:
				print '0'
				break
			else:
				sums = 0
				for digit in strings:
					sqr = int(digit) * int(digit)
					sums += sqr
				d.append(str(sums))
				strings = list(str(sums))
			if ''.join(strings) in d[:-1]:
				print '0'
				break
