#!/usr/bin/env python

# flag: PAN{l4byr1n7h_s4yz_x0r1s_4m4z1ng}

from z3 import *

'''
			int value = this.sbR.Value;
			int value2 = this.sbG.Value;
			int value3 = this.sbB.Value;
			int num = value2 * value3;
			int num2 = value * 3;
			if (value + num - value2 + value * value * value2 - value3 == value2 * (value3 * 34 + (num2 - value)) + 3744 && value > 60)
'''

s = Solver()

value = BitVec('value', 32)
value2 = BitVec('value2', 32)
value3 = BitVec('value3', 32)

for v in value, value2, value3:
	s.add(v > 0)
	s.add(v < 256)

s.add(value > 60)
s.add((value + (value2 * value3) - value2 + value * value * value2 - value3 == value2 * (value3 * 34 + ((value * 3) - value)) + 3744))

print s.check()
print s.model()

'''
win-5 python ./solution.py
sat
[value2 = 168, value3 = 203, value = 83]
'''
