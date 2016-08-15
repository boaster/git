#!/usr/bin/env python

import zlib, marshal

# flag: PAN{l1Ke_n0_oN3_ev3r_Wa5}

infile = open('rc4.payload', 'r').read()
data = infile.decode('base64')
key = '1_W4nnA_b3_Th3_vERy_b3ST!'

S = range(256)
j = 0
out = []

#KSA Phase
for i in range(256):
    j = (j + S[i] + ord( key[i % len(key)] )) % 256
    S[i] , S[j] = S[j] , S[i]

#PRGA Phase
i = j = 0
for char in data:
    i = ( i + 1 ) % 256
    j = ( j + S[i] ) % 256
    S[i] , S[j] = S[j] , S[i]
    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

co = marshal.loads(''.join(out))
print type(co)