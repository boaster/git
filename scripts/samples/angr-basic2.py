#!/usr/bin/env python

import angr, claripy, logging


p = angr.Project('/vagrant/scripts/angr/stage3.bin')

def func(p, blankState, findAddr, avoidAddr):
	s = p.factory.blank_state(addr = blankState)
	c = s.se.BVS('c', 1*8)
	s.regs.rax = c
	
	pg = p.factory.path_group(s)
	pg.explore(find=(findAddr,), avoid=(avoidAddr,))
	state = pg.found[0].state
	return state.se.any_str(c)

password = ""

password += func(p, 0x40080f, 0x40084a, 0x400848)
password += func(p, 0x400875, 0x4008b5, 0x4008b3)
password += func(p, 0x4008d9, 0x400914, 0x400912)
password += func(p, 0x400938, 0x400978, 0x400976)
password += func(p, 0x40099c, 0x4009d6, 0x4009d4)
password += func(p, 0x4009fa, 0x400a3a, 0x400a38)
password += func(p, 0x400a5e, 0x400a9e, 0x400a9c)
password += func(p, 0x400ac2, 0x400b02, 0x400b00)
password += func(p, 0x400b26, 0x400b61, 0x400b5f)
password += func(p, 0x400b85, 0x400bc5, 0x400bc3)
password += func(p, 0x400be9, 0x400c24, 0x400c22)
password += func(p, 0x400c48, 0x400c83, 0x400c81)
password += func(p, 0x400ca7, 0x400cfa, 0x400cf8)
password += func(p, 0x400d1e, 0x400d59, 0x400d57)
password += func(p, 0x400d7d, 0x400dbd, 0x400dbb)
password += func(p, 0x400de1, 0x400e1c, 0x400e1a)
password += func(p, 0x400e40, 0x400e7b, 0x400e79)
password += func(p, 0x400e9f, 0x400eda, 0x400ed8)
password += func(p, 0x400efe, 0x400f39, 0x400f37)
password += func(p, 0x400f5d, 0x400f98, 0x400f96)
password += func(p, 0x400fbc, 0x400ffc, 0x400ffa)
#password += func(p, 0x401023, 0x400ffc, 0x400ffa)


print password