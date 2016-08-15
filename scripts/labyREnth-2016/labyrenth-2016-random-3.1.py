#!/usr/bin/env python

from struct import pack

def combine():

	infile = open('labyrenth-2016-random-3.2.sequence-syns.txt', 'r')
	outfile = open('result-syns.zip', 'w')

	for l in infile:
		outfile.write( pack(">I", int(l.strip())) )
	
	infile.close()
	outfile.close()


def split_zips():
	infile = bytearray(open('result.zip', 'r').read())
	print infile[0]

combine()
