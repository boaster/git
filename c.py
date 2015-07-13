#!/usr/bin/env python

import sys

infile = open(sys.argv[1], 'r')

for line in infile:
	l = line.strip().split(' ')
	s = []
	final = []
	for i in range(len(l)):
		if not s:
			s.append(l[i])
		elif l[i] != s[len(s) -1]:
			s.append(l[i])
	for a in s:
		final.append(str(l.count(a)))
		final.append(a)
	print ' '.join(final)
