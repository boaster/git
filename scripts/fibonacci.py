#!/usr/bin/env python

import sys

infile = open(sys.argv[1], 'r')

def fib(n):
	if n < 2:
		return n
	return fib(n-2) + fib(n-1)


for line in infile:
	num = int(line)
	print fib(num)

