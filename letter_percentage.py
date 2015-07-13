#!/usr/bin/env python

import sys

infile = open(sys.argv[1], 'r')

for line in infile:
	l = list(line.strip())
	lower = 0
	upper = 0
	for letter in l:
		if letter.islower():
			lower += 1
		elif letter.isupper():
			upper += 1
	lower_percentage = 0
	upper_percentage = 0
	if lower == 0:
		lower_percentage = 0
	if upper == 0:
		upper_percentage = 0
	lower_percentage = (float(lower) / len(l)) * 100
	upper_percentage = (float(upper) / len(l)) * 100
	print("lowercase: %.2f uppercase: %.2f") % (lower_percentage, upper_percentage)
