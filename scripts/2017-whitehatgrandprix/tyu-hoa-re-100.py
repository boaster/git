#!/usr/bin/env python

import angr, claripy, logging


p = angr.Project('./re100')

def func(p, blankState, findAddr, avoidAddr):
	s = p.factory.blank_state(addr = blankState)
	c = s.se.BVS('c', 40*8)
	s.memory.store(0x6021C0, c)
#	s.regs.rdi = 0x6021C0
	
	pg = p.factory.path_group(s)
	pg.explore(find=(findAddr,), avoid=avoidAddr)
	state = pg.found[0].state
	return state.se.any_str(c)


avoid = (0x4009E6, 0x400A44, 0x400AB2, 0x400B2C, 0x400B96, 0x400C00, 0x400C9A, 0x400CF8, 0x400D76, 0x400DEF, 0x400E3F)
print func(p, 0x400E71, 0x400EA8, avoid) + '0'	# Got this '0' from Admin
