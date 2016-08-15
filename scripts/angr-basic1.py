#!/usr/bin/env python

import angr, claripy

#0x400993

p = angr.Project('/vagrant/scripts/angr/stage2.bin')

# if i comment this line input can be set to other comment
s = p.factory.entry_state()

#i = claripy.BVS('i', 11*8)
i = s.se.BVS('i', 11*8)

state = p.factory.entry_state(args=['/vagrant/scripts/angr/stage2.bin', i])

pg = p.factory.path_group(state)

pg.explore(find=(0x40097f,), avoid=(0x400784, 0x4007a9, 0x4007e0, 0x400826, 0x400855, 0x400884,0x4008b8,0x4008e7,0x400904,0x40093e,0x400978, ))

state = pg.found[0].state

#print(state.simplify())

print("Password is: " + state.se.any_str(i))