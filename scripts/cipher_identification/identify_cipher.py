#!/usr/bin/env python

import sys

infile = bytearray(open(sys.argv[1], 'r').read())
l = 0

# Identify Stream Cipher, likely RC4.
if len(infile) % 8 != 0:
	l = 1
	print("%s") % "Ciphertext is not evenly divisible by 8. Very high chances STREAM CIPHER used. Most common RC4."

# Identify Block Cipher, AES
if len(infile) % 16 == 0:
	l = 1
	print("%s") % "Ciphertext is evenly divisibly by 16. Very high chances BLOCK CIPHER with block size of 16 bytes. Most common AES."

# Identify Block Cipher, DES/3DES
if (len(infile) % 16 == 0) and (len(infile) % 8 == 0):
	l = 1
	print("%s") % "Ciphertext is divisible by 16 and 8. Most likely it's DES/3DES."
elif (len(infile) % 16 != 0) and (len(infile) % 8 == 0):
	l = 1
	print("%s") % "Ciphertext is divisible by 8 but not by 16. Most likely it's DES/3DES."
if l == 0:
	print("%s") % "I have no idea. Have you tried Substitution cipher or XOR ?"
