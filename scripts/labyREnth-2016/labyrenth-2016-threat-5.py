#!/usr/bin/env python


full = ''

for i in range(0, 19500, 100):
	ifile = open(str(i), 'r').read()
	full += ifile[:-1]


ofile = open('http.pcap', 'w')
ofile.write(full)
ofile.close()