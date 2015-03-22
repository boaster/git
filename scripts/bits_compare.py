#!/usr/bin/env python

import sys

file_ = open(sys.argv[1], 'r')

for lines in file_:
	digits = list(map(int, lines.split(',')))
	digits[0] = list('{0:08b}'.format(digits[0]))[::-1]
	p1 = digits[1] - 1
	p2 = digits[2] - 1
	if digits[0][p1] == digits[0][p2]:
		print 'true'
	else:
		print 'false'
