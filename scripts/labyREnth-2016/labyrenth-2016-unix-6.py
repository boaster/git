#!/usr/bin/env python

from z3 import *

'''
flag: PAN{th@Nk5_m4r1ha_U_s0_n1c3}

key1: 3at
key2: chInch1ll@z
key3: H1gh
key4: F183r

[0] + [1] = 0xcb
[0] + [2] = 0xac
[0] + [3] = 0xd1
[0] + [4] = 0xc6
[0] + [5] = 0xcb
[0] + [6] = 0x94
[0] + [7] = 0xcf
[0] + [8] = 0xcf
[0] + [9] = 0xa3
[0] + [10] = 0xdd
[0] + [1] = 0xcb
[1] + [2] = 0xb1
[1] + [3] = 0xd6
[1] + [4] = 0xcb
[1] + [5] = 0xd0
[1] + [6] = 0x99
[1] + [7] = 0xd4
[1] + [8] = 0xd4
[1] + [9] = 0xa8
[1] + [10] = 0xe2
[2] + [0] = 0xac
[2] + [1] = 0xb1
[2] + [3] = 0xb7
[2] + [4] = 0xac
[2] + [5] = 0xb1
[2] + [6] = 0x7a
[2] + [7] = 0xb5
[2] + [8] = 0xb5
[2] + [9] = 0x89
[2] + [10] = 0xc3

[0] - [3] == 0xe0
(([0] * [0]) * ([0] * [0])) * 0x2329 == 0x2329
[3] - [2] == 1
0x383d3d44 - [2] == 0x383d3cdd

'''

def key_2():
	s = Solver()

	a_0 = BitVec('a_0', 8)
	a_1 = BitVec('a_1', 8)
	a_2 = BitVec('a_2', 8)
	a_3 = BitVec('a_3', 8)

	s.add(a_0 - a_3 == 0xe0)
#	s.add( (((a_0 * a_0) * (a_0 * a_0)) * 0x2329) == 0x2329)
	s.add(a_3 - a_2 == 1)
	s.add(a_2 == ord('g'))

	print s.check()
	print s.model()	 # this one is incorrect

def key_1():
	s = Solver()
	
	a_0 = BitVec('a_0', 8)
	a_1 = BitVec('a_1', 8)
	a_2 = BitVec('a_2', 8)
	a_3 = BitVec('a_3', 8)
	a_4 = BitVec('a_4', 8)
	a_5 = BitVec('a_5', 8)
	a_6 = BitVec('a_6', 8)
	a_7 = BitVec('a_7', 8)
	a_8 = BitVec('a_8', 8)
	a_9 = BitVec('a_9', 8)
	a_10 = BitVec('a_10', 8)

	s.add(a_0 + a_1 == 0xcb)
	s.add(a_0 + a_2 == 0xac)
	s.add(a_0 + a_3 == 0xd1)
	s.add(a_0 + a_4 == 0xc6)
	s.add(a_0 + a_5 == 0xcb)
	s.add(a_0 + a_6 == 0x94)
	s.add(a_0 + a_7 == 0xcf)
	s.add(a_0 + a_8 == 0xcf)
	s.add(a_0 + a_9 == 0xa3)
	s.add(a_0 + a_10 == 0xdd)
	s.add(a_0 + a_1 == 0xcb)
	s.add(a_1 + a_2 == 0xb1)
	s.add(a_1 + a_3 == 0xd6)
	s.add(a_1 + a_4 == 0xcb)
	s.add(a_1 + a_5 == 0xd0)
	s.add(a_1 + a_6 == 0x99)
	s.add(a_1 + a_7 == 0xd4)
	s.add(a_1 + a_8 == 0xd4)
	s.add(a_1 + a_9 == 0xa8)
	s.add(a_1 + a_10 == 0xe2)
	s.add(a_2 + a_0 == 0xac)
	s.add(a_2 + a_1 == 0xb1)
	s.add(a_2 + a_3 == 0xb7)
	s.add(a_2 + a_4 == 0xac)
	s.add(a_2 + a_5 == 0xb1)
	s.add(a_2 + a_6 == 0x7a)
	s.add(a_2 + a_7 == 0xb5)
	s.add(a_2 + a_8 == 0xb5)
	s.add(a_2 + a_9 == 0x89)
	s.add(a_2 + a_10 == 0xc3)

	s.check()
	print s.model()

