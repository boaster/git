#!/usr/bin/env python

def rev(ct):
	pt = ''
	for i in range(1, len(ct)):
		ct[-i-1] = (ct[-i-1] + ct[-i]) & 0xff
	return ct

key = 'golang-or-bust'
ifile = bytearray(open('flag.enc', 'r').read())

open('decrypted.zip', 'w').write(rev(ifile))
print "flag.enc decrypted. Use 7z with password golang-or-bust"