#!/usr/bin/env python

from string import maketrans, translate
import base64
from pwn import *

ifile = bytearray(open('1.doc', 'r').read())
xfile = bytearray(open('2.doc', 'r').read())
yfile = bytearray(open('4.doc', 'r').read())
key = '\x4d\x1e\x47\x63'



def correctbase64(str):
	    return str.translate(base64fixTable)

def caesar(plainText, shift): 
    cipherText = ""
    for ch in plainText:
#        if ch.isalpha():
        stayInAlphabet = ord(ch) + shift 
        if stayInAlphabet > ord('z'):
            stayInAlphabet -= 26
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    print "Your ciphertext is: ", cipherText
    return cipherText

def rot(x):
	pt = ''
	for i in range(len(x)):
		pt += chr( (ord(x[i]) + 0x26) % 255 )
	return pt

def xor(x):
		pt = ''
		for i in range(len(x)):
			pt += chr( ord(x[i]) ^ 0x26)
		return pt
#		print correctbase64(pt)

b64Table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
#newBase64Table = b64Table
base64fixTable = maketrans(b64Table, b64Table[0x26:] + b64Table[:0x26]);


one = xor(''.join(map(chr, ifile)))
#two = xor(yfile).strip("ROTXOR\x00\x00")
#thr = xor(xfile).strip("ROTXOR\x00\x00")

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

print correctbase64(one.replace('-', '+'))[:-7].decode('base64')


'''Write a YARA rule to detect all variations of this encoded data.
Using the template below replace each "**" pair with the first 12 bytes:

rule enc_doc : enc_doc
{
        strings:

                        $first = { ** ** ** ** ** ** ** ** ** ** ** ** }
                        $second = { ** ** ** ** ** ** ** ** ** ** ** ** }
                        $third = { ** ** ** ** ** ** ** ** ** ** ** ** }

        condition:
                        1 of them
}'''


yara = '''rule enc_doc : enc_doc
{
        strings:

                        $first = { 50 74 4C 62 15 41 53 10 5F 55 44 5C }
                        $second = { 4F 40 15 6B 16 5E 54 09 4F 41 43 10 }
                        $third = { 4F 45 44 5E 14 67 09 69 5C 55 44 11 }

        condition:
                        1 of them
}'''

r = remote('52.37.130.153', 2600)
#r.recv()
r.send(yara)
r.interactive()

# PAN{7H1r7EEn-hOuR_71me_l1M17}