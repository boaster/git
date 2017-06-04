#!/usr/bin/env python

# The flag is: Yepp, go to the next level! :D

from pwn import *

r = remote('cgc.cykor.kr', 31328)

infile = open('patched', 'rb').read()

r.recvuntil('How many bytes is your patched CB?\n')
r.sendline(str(len(infile)))
r.recvuntil('Ok...send it\n')
r.send(infile)

r.interactive()