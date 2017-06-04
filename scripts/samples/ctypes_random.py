#!/usr/bin/env python

from pwn import *
import ctypes

LIBC = ctypes.cdll.LoadLibrary("./libc-2.19.so")

t = LIBC.time(0)
LIBC.srand(t)

randomn = str(LIBC.rand())
print randomn
