#!/usr/bin/env python

import sys

file_enum = open(sys.argv[1], 'r')
words = []
for line in file_enum:
	words = list(line)
	for i in range(len(words)):
		if words[i].istitle():
			words[i] = words[i].lower()
		elif words[i].istitle() == False:
			words[i] = words[i].upper()
	print ''.join(map(str, words)).strip()
