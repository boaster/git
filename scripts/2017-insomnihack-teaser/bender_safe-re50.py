#!/usr/bin/env python

import angr, logging, claripy
from pwn import *

logging.getLogger('angr.path_group').setLevel(logging.DEBUG)
p = angr.Project('./challenge/bender_safe')

#r = remote(sys.argv[1], int(sys.argv[2]))
#r.recvuntil(' : \n')
#rotp = r.recvline().strip()
#print "OTP: " + rotp

print p.arch

s = p.factory.blank_state(addr = 0x0401C50)
c = s.se.BVS('c', 8*8)
s.regs.a1 = c
otp = claripy.BVV('A6C4AYMYJ1PJ7LFI', 8*16)
s.memory.store(0x04A7AB0, otp)
s.regs.a0 = 0x04A7AB0

for b in c.chop(8):
	s.add_constraints(b > 0x31)
	s.add_constraints(b < ord('z'))
	
pg = p.factory.path_group(s)
pg.explore(find=(0x0402D0C,), avoid=(0x0401DDC,0x0401F2C,0x04020C4,0x0402264,0x0402418,0x04024B0,0x0402650,0x04026E8,0x04028B4,0x0402A84,0x0402C44,0x0402CDC))
state = pg.found[0].state
print state.se.any_str(c)

#r.interactive()