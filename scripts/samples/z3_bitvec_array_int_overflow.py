#!/usr/bin/python
import sys
import string
from z3 import *

ceiling = string.atoi(sys.argv[1])
array = [ BitVec('a%i'%i,32) for i in range(0,ceiling)]
m = BitVec('m',32)
s = Solver()
s.add(m == 0xffffffff)

y = BitVec('y',32)


for i in range(0,ceiling):
    print i
    s.add(array[i] <= 126)
    s.add(array[i] >= 32)

s.add(y==(33*(5381)+array[0]))
for i in range(1,ceiling):
  y = 33*y+array[i]
s.add((y*33)&m==0xd386d1ff)

print s.check()
print s.model()