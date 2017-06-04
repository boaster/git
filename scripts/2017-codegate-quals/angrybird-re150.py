#!/usr/bin/env python

from z3 import *

def show(c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19):
	a = ''
	a += chr(c0.as_long())
	a += chr(c1.as_long())
	a += chr(c2.as_long())
	a += chr(c3.as_long())
	a += chr(c4.as_long())
	a += chr(c5.as_long())
	a += chr(c6.as_long())
	a += chr(c7.as_long())
	a += chr(c8.as_long())
	a += chr(c9.as_long())
	a += chr(c10.as_long())
	a += chr(c11.as_long())
	a += chr(c12.as_long())
	a += chr(c13.as_long())
	a += chr(c14.as_long())
	a += chr(c15.as_long())
	a += chr(c16.as_long())
	a += chr(c17.as_long())
	a += chr(c18.as_long())
	a += chr(c19.as_long())
	return a

if True:
	c_0 = BitVec('c_0', 8)
	c_1 = BitVec('c_1', 8)
	c_2 = BitVec('c_2', 8)
	c_3 = BitVec('c_3', 8)
	c_4 = BitVec('c_4', 8)
	c_5 = BitVec('c_5', 8)
	c_6 = BitVec('c_6', 8)
	c_7 = BitVec('c_7', 8)
	c_8 = BitVec('c_8', 8)
	c_9 = BitVec('c_9', 8)
	c_10 = BitVec('c_10', 8)
	c_11 = BitVec('c_11', 8)
	c_12 = BitVec('c_12', 8)
	c_13 = BitVec('c_13', 8)
	c_14 = BitVec('c_14', 8)
	c_15 = BitVec('c_15', 8)
	c_16 = BitVec('c_16', 8)
	c_17 = BitVec('c_17', 8)
	c_18 = BitVec('c_18', 8)
	c_19 = BitVec('c_19', 8)
	s = Solver()
	s.add(c_0 > 0x20)
	s.add(c_0 < 0x7f)
	s.add(c_1 > 0x20)
	s.add(c_1 < 0x7f)
	s.add(c_2 > 0x20)
	s.add(c_2 < 0x7f)
	s.add(c_3 > 0x20)
	s.add(c_3 < 0x7f)
	s.add(c_4 > 0x20)
	s.add(c_4 < 0x7f)
	s.add(c_5 > 0x20)
	s.add(c_5 < 0x7f)
	s.add(c_6 > 0x20)
	s.add(c_6 < 0x7f)
	s.add(c_7 > 0x20)
	s.add(c_7 < 0x7f)
	s.add(c_8 > 0x20)
	s.add(c_8 < 0x7f)
	s.add(c_9 > 0x20)
	s.add(c_9 < 0x7f)
	s.add(c_10 > 0x20)
	s.add(c_10 < 0x7f)
	s.add(c_11 > 0x20)
	s.add(c_11 < 0x7f)
	s.add(c_12 > 0x20)
	s.add(c_12 < 0x7f)
	s.add(c_13 > 0x20)
	s.add(c_13 < 0x7f)
	s.add(c_14 > 0x20)
	s.add(c_14 < 0x7f)
	s.add(c_15 > 0x20)
	s.add(c_15 < 0x7f)
	s.add(c_16 > 0x20)
	s.add(c_16 < 0x7f)
	s.add(c_17 > 0x20)
	s.add(c_17 < 0x7f)
	s.add(c_18 > 0x20)
	s.add(c_18 < 0x7f)
	s.add(c_19 > 0x20)
	s.add(c_19 < 0x7f)
	s.add(c_0 == ord('I'))
	s.add(c_1 == ord('m'))


# Extra 
s.add( (c_3 ^ c_7) | c_17 > 0x5e)


s.add( (c_0 ^ c_1) > 15 )
s.add( (c_18 & c_1) < 49 )

s.add((c_0 & c_1) < 0x51)
s.add((c_1 & c_18) < 0x31)
s.add(((c_4 & c_7) ^ c_0) < 0x2d)
s.add( (c_0 & c_2) > 72 )
s.add( (c_11 & c_17) > 72 )
s.add( (c_0 ^ c_13) > 43 )
s.add( (c_13 ^ c_10) > 0x42 )
s.add( (c_11 ^ c_16) < 17 )
s.add( (c_10 ^ c_8) < 84 )
s.add( (c_19 ^ c_5) > 117 )
s.add( (c_0 | c_1) > 16 )
s.add( (c_17 & c_3) > 80 )
s.add( (c_13 | c_15) > 116 )
s.add( (c_1 ^ c_11) > 28 )


s.add( (c_12 ^ c_15) < 19 )
s.add( (c_13 & c_1) > 47 )
s.add( (c_1 ^ c_9) > 7 )
s.add( (c_16 >> 1) > 25 )
s.add( (c_4 & c_12) > 41 )
s.add( (c_16 >> 1) > 14 )
s.add( (c_0 >> 5) < 49 )
s.add( (c_0 ^ c_1) < 46 )
s.add( (c_0 & c_1) > 0 )
s.add( (c_0 ^ c_19) > 95 )
s.add( (c_16 | c_7) > 121 )
s.add( (c_7 ^ c_17) < 43 )

s.add( (c_15 & c_3) > 61 )
s.add( (c_19 ^ c_15) < 95 )

s.add( (c_0 ^ c_1) < 126 )
s.add( (c_18 & c_1) > 0 )

s.add( (c_4 ^ c_19) < 107 )
s.add( (c_8 & c_7) > 33 )
s.add( (c_6 | c_7) > 118 )
s.add( (c_18 & c_1) < 59 )
s.add( (c_2 ^ c_8) > 42 )
s.add( (c_2 ^ c_13) > 46 )
s.add( (c_3 & c_8) > 94 )
s.add( (c_16 ^ c_18) > 66 )
s.add( (c_10 ^ c_9) > 23 )
s.add( (c_18 & c_1) > 17 )

'''
if s.check() == sat:
	m = s.model()
	print show(m[c_0], m[c_1], m[c_2], m[c_3], m[c_4], m[c_5], 
		m[c_6], m[c_7], m[c_8], m[c_9], m[c_10], m[c_11], m[c_12], 
		m[c_13], m[c_14], m[c_15], m[c_16], m[c_17], m[c_18], m[c_19])
'''

s.add( (c_0 & c_1) < 91 )
s.add( (c_16 ^ c_1) < 64 )
s.add( (c_18 & c_1) < 103 )
s.add( (c_18 & c_3) > 49 )
s.add( (c_9 ^ c_1) < 27 )
s.add( (c_0 ^ c_1) < 56 )
s.add( (c_13 & c_1) < 104 )
s.add( (c_18 & c_1) > 0 )
s.add( (c_0 ^ c_1) > 34 )
s.add( (c_0 & c_1) < 91 )
s.add( (c_11 ^ c_14) < 5 )
s.add( (c_5 ^ c_11) < 51 )
s.add( (c_18 & c_1) > 37 )
s.add( (c_0 ^ c_6) < 49 )

s.add( (c_0 | c_1) > 85 )
s.add( (c_9 ^ c_10) > 66 )
s.add( (c_10 & c_8) > 30 )
s.add( (c_19 ^ c_17) < 119 )
s.add( (c_17 ^ c_18) > 94 )
s.add( (c_18 & c_9) > 30 )
s.add( (c_3 ^ c_6) < 33 )
s.add( (c_0 | c_1) < 121 )
s.add( (c_10 & c_18) < 82 )
s.add( (c_6 | c_7) < 120 )
s.add( (c_0 ^ c_6) > 16 )
s.add( (c_0 | c_1) > 66 )
s.add( (c_6 & c_1) > 84 )

s.add( (c_18 & c_1) < 119 )
s.add( (c_0 ^ c_6) < 48 )
s.add( (c_0 | c_1) > 60 )
s.add( (c_18 & c_1) > 13 )
s.add( (c_0 ^ c_6) > 38 )
s.add( (c_13 ^ c_10) < 68 )
s.add( (c_0 | c_1) > 94 )
s.add( (c_0 & c_11) < 68 )
s.add( (c_18 & c_1) < 49 )
s.add( (c_0 ^ c_6) < 103 )
s.add( (c_0 ^ c_19) < 97 )




s.add( (c_6 | c_1) > 43 )
s.add( (c_5 & c_1) < 96 )
s.add( (c_18 & c_1) < 66 )
s.add( (c_0 ^ c_6) > 24 )

s.add( (c_9 ^ c_10) < 68 )

s.add( (c_9 & c_17) < 102 )
s.add( (c_0 ^ c_16) > 40 )
s.add( (c_18 & c_3) < 51 )

s.add( (c_0 | c_1) > 12 )


s.add( (c_0 ^ c_6) < 45 )
s.add( (c_0 | c_1) > 93 )
s.add( (c_12 | c_4) > 40 )



s.add( (c_1 ^ c_9) < 9 )

s.add( (c_11 ^ c_14) > 3 )
s.add( (c_11 | c_9) > 102 )
s.add( (c_12 ^ c_15) < 69 )
s.add( (c_0 & c_2) < 74 )
s.add( (c_13 & c_1) > 68 )

s.add( (c_13 ^ c_5) < 80 )
s.add( (c_12 ^ c_14) < 7 )
s.add( (c_9 & c_4) > 16 )

s.add( (c_11 | c_9) > 89 )
s.add( (c_12 ^ c_15) < 47 )
s.add( (c_19 | c_7) > 77 )
s.add( (c_4 ^ c_6) < 13 )



s.add( (c_11 | c_9) < 123 )
s.add( (c_12 ^ c_15) > 3 )
s.add( (c_13 & c_1) > 56 )

s.add( (c_2 ^ c_8) < 44 )
s.add( (c_13 ^ c_5) > 16 )


s.add( (c_12 ^ c_15) < 47 )

s.add( (c_13 ^ c_5) < 97 )


s.add( (c_11 | c_9) > 32 )
s.add( (c_9 & c_11) > 32 )

s.add( (c_11 | c_9) > 90 )
s.add( (c_12 ^ c_15) < 33 )
s.add( (16 * c_7) > 61 )
s.add( (c_13 ^ c_5) > 33 )
s.add( (c_0 >> 5) < 17 )

s.add( (c_11 | c_9) > 95 )
s.add( (c_12 ^ c_15) < 49 )
s.add( (c_13 & c_1) < 114 )
s.add( (c_7 ^ c_17) > 41 )
s.add( (16 * c_7) > 63 )

s.add( (c_4 & c_12) > 94 )
s.add( (c_2 ^ c_8) < 44 )
s.add( (c_16 >> 1) > 57 )

s.add( (c_4 & c_12) < 104 )
s.add( (c_16 >> 1) < 93 )

s.add( (c_11 | c_9) > 20 )
s.add( (c_12 ^ c_15) < 83 )
s.add( (c_13 | c_15) < 118 )
s.add( (c_13 & c_1) > 51 )
s.add( (c_19 ^ c_5) < 119 )




s.add( (c_4 & c_12) > 67 )
s.add( (c_5 & c_17) > 56 )


s.add( (c_4 & c_12) > 78 )


s.add( (c_11 | c_9) > 101 )
s.add( (c_13 & c_1) > 61 )

s.add( (c_13 ^ c_5) > 34 )

s.add( (c_4 & c_12) > 5 )

s.add( (c_4 & c_12) < 114 )


s.add( (c_0 ^ c_1) < 85 )
s.add( (c_0 & c_1) < 82 )

s.add( (c_18 ^ c_14) | c_3 == 0x7f)

if s.check() == sat:
	m = s.model()
	print show(m[c_0], m[c_1], m[c_2], m[c_3], m[c_4], m[c_5], 
		m[c_6], m[c_7], m[c_8], m[c_9], m[c_10], m[c_11], m[c_12], 
		m[c_13], m[c_14], m[c_15], m[c_16], m[c_17], m[c_18], m[c_19])



s.add( (c_0 ^ c_1) < 67 )
s.add( (c_0 & c_1) < 82 )
s.add( (c_18 & c_1) < 42 )
s.add( (c_0 ^ c_1) < 83 )
s.add( (c_17 & c_3) < 85 )
s.add( (c_0 & c_1) > 34 )
s.add( (c_18 & c_1) < 67 )
s.add( (c_0 & c_1) < 91 )
s.add( (c_18 & c_4) < 74 )
s.add( (c_18 & c_1) > 12 )
s.add( (c_0 ^ c_1) > 9 )
s.add( (c_2 ^ c_8) > 42 )
s.add( (c_13 ^ c_0) < 45 )
s.add( (c_0 & c_1) > 14 )
s.add( (c_0 & c_1) > 16 )
s.add( (c_18 & c_1) < 75 )
s.add( (c_0 ^ c_6) < 103 )
s.add( (4 * c_2) > 16 )
s.add( (c_0 | c_1) > 87 )
s.add( (c_1 ^ c_11) < 30 )
s.add( (c_18 & c_1) < 52 )
s.add( (c_0 ^ c_6) < 75 )
s.add( (4 * c_2) > 103 )
s.add( (c_0 | c_1) > 56 )
s.add( (c_4 ^ c_6) > 11 )
s.add( (c_0 & c_1) > 16 )
s.add( (c_18 & c_1) > 22 )
s.add( (c_0 ^ c_6) < 75 )


'''
if s.check() == sat:
	m = s.model()
	print show(m[c_0], m[c_1], m[c_2], m[c_3], m[c_4], m[c_5], 
		m[c_6], m[c_7], m[c_8], m[c_9], m[c_10], m[c_11], m[c_12], 
		m[c_13], m[c_14], m[c_15], m[c_16], m[c_17], m[c_18], m[c_19])
'''



s.add( (4 * c_2) > 16 )
s.add( (c_16 ^ c_18) > 66 )
s.add( (c_0 & c_1) < 103 )
s.add( (c_0 ^ c_6) < 75 )
s.add( (c_9 | c_13) > 27 )
s.add( (4 * c_2) > 58 )
s.add( (4 * c_2) > 77 )
s.add( (c_0 | c_1) > 3 )
s.add( (c_0 & c_1) > 13 )
s.add( (c_0 ^ c_6) < 48 )
s.add( (c_7 & c_4) > 39 )
s.add( (c_0 | c_1) > 66 )
s.add( (c_0 & c_1) > 47 )
s.add( (c_18 & c_1) < 64 )
s.add( (c_13 & c_3) < 123 )
s.add( (4 * c_2) > 65 )
s.add( (c_0 & c_1) < 121 )
s.add( (4 * c_2) > 83 )
s.add( (c_0 | c_1) > 99 )




s.add( (c_0 ^ c_6) < 111 )
s.add( (4 * c_2) > 92 )
s.add( (c_0 | c_1) > 59 )
s.add( (c_8 | c_0) > 1 )

s.add( (c_11 | c_9) > 78 )
s.add( (c_12 ^ c_15) < 48 )
s.add( (c_13 & c_1) > 90 )
s.add( (16 * c_7) > 78 )
s.add( (c_13 ^ c_5) > 30 )

s.add( (c_11 | c_9) > 17 )
s.add( (c_12 ^ c_15) < 87 )
s.add( (c_12 & c_4) < 121 )
s.add( (16 * c_7) > 46 )
s.add( (c_13 ^ c_5) < 64 )
s.add( (c_12 ^ c_14) > 5 )

s.add( (c_11 | c_9) > 73 )
s.add( (c_12 ^ c_15) < 61 )
s.add( (c_13 & c_1) < 120 )

s.add( (c_12 ^ c_15) < 45 )
s.add( (c_13 & c_1) > 58 )
s.add( (c_13 ^ c_5) < 60 )

s.add( (c_0 >> 5) < 59 )

s.add( (c_11 | c_9) > 101 )
s.add( (c_13 & c_1) > 99 )
s.add( (16 * c_7) > 78 )
s.add( (c_13 ^ c_4) < 17 )

s.add( (c_11 | c_9) < 119 )

s.add( (c_12 ^ c_15) > 1 )
s.add( (16 * c_7) > 0 )
s.add( (c_13 ^ c_5) < 102 )
s.add( (c_0 >> 5) < 19 )


s.add( (c_11 | c_9) > 0 )
s.add( (c_12 ^ c_15) < 68 )
s.add( (c_13 & c_1) < 104 )
s.add( (16 * c_4) < 1 )
s.add( (c_13 ^ c_5) > 38 )

s.add( (c_4 & c_12) > 94 )



s.add( (c_11 | c_9) < 119 )
s.add( (c_12 ^ c_15) < 59 )
s.add( (c_13 & c_1) > 91 )
s.add( (16 * c_7) > 72 )
s.add( (c_13 ^ c_5) < 64 )

s.add( (c_4 & c_12) > 94 )

s.add( (c_4 & c_12) < 100 )
s.add( (c_16 >> 1) < 64 )
s.add( (c_0 >> 5) < 82 )

s.add( (c_11 | c_9) < 119 )
s.add( (c_8 ^ c_15) < 2 )
s.add( (c_7 & c_1) > 72 )
s.add( (16 * c_17) < 2 )
s.add( (c_3 ^ c_5) < 111 )

s.add( (c_4 & c_12) > 68 )

s.add( (c_4 & c_12) < 100 )

s.add( (c_3 ^ c_1) < 43 )
s.add( (c_4 & c_1) < 119 )

s.add( (c_0 ^ c_1) < 65 )
s.add( (c_0 & c_1) < 111 )
s.add( (4 * c_2) > 104 )
s.add( (c_0 | c_1) < 113 )
s.add( (c_0 & c_1) > 62 )
s.add( (c_18 & c_1) < 49 )
s.add( (c_0 ^ c_6) < 59 )
s.add( (4 * c_2) > 104 )
s.add( (c_8 | c_1) > 50 )
s.add( (c_5 & c_1) > 38 )
s.add( (c_18 & c_1) < 86 )
s.add( (c_0 ^ c_6) > 18 )
s.add( (4 * c_2) > 97 )
s.add( (c_0 | c_1) > 94 )
s.add( (c_18 & c_1) > 26 )

# Extra

if s.check() == sat:
	m = s.model()
	print show(m[c_0], m[c_1], m[c_2], m[c_3], m[c_4], m[c_5], 
		m[c_6], m[c_7], m[c_8], m[c_9], m[c_10], m[c_11], m[c_12], 
		m[c_13], m[c_14], m[c_15], m[c_16], m[c_17], m[c_18], m[c_19])


s.add( (c_0 ^ c_6) < 68 )
s.add( (4 * c_2) > 104 )
s.add( (c_18 & c_1) < 51 )
s.add( (c_0 ^ c_6) > 22 )
s.add( (4 * c_2) > 103 )

s.add( (c_0 | c_1) > 38 )
s.add( (c_0 & c_1) > 52 )
s.add( (c_18 & c_1) > 17 )
s.add( (4 * c_9) < 2 )

s.add( (c_0 | c_1) > 92 )
s.add( (c_0 & c_1) > 55 )
s.add( (c_8 ^ c_6) < 82 )
s.add( (4 * c_12) < 2 )
s.add( (c_0 | c_1) > 94 )

s.add( (c_0 ^ c_6) > 102 )

if s.check() == sat:
	m = s.model()
	print show(m[c_0], m[c_1], m[c_2], m[c_3], m[c_4], m[c_5], 
		m[c_6], m[c_7], m[c_8], m[c_9], m[c_10], m[c_11], m[c_12], 
		m[c_13], m[c_14], m[c_15], m[c_16], m[c_17], m[c_18], m[c_19])

s.add( (4 * c_4) < 2 )
s.add( (c_0 | c_1) > 44 )


