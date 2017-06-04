#!/usr/bin/env python

# The flag is: Wh000oo0o yo0ou, you talking m3!!

from pwn import *

r = remote('cgc.cykor.kr', 34632)

infile = open('CGC_2_patched', 'rb').read()

r.recvuntil('How many bytes is your patched CB?\n')
r.sendline(str(len(infile)))
r.recvuntil('Ok...send it\n')
r.send(infile)

r.interactive()