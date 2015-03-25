#!/usr/bin/env python

infile = bytearray(open("enc.enc", 'r').read())

for key in range(0x100):
	decrypted = infile[:]
	for byte in range(len(infile)):
		decrypted[byte] = infile[byte] ^ key   # XOR each byte
		decrypted[byte] = infile[byte] ^ 0xFF  # reverting all bits
	outfile = "out-" + str(key) + ".enc"
	open(outfile, 'wb').write(decrypted)


