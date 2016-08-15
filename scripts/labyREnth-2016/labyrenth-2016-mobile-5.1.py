#!/usr/bin/env python

from pwn import *

req  = 'GET / HTTP/1.1\x0d\x0a'
req += 'Host: panspacedungeon.com\x0d\x0a'
req += 'Accept: */*\x0d\x0a'
req += 'Accept-Language: en-us\x0d\x0a'
req += 'Connection: keep-alive\x0d\x0a'
req += 'Accept-Encoding: gzip, deflate\x0d\x0a'
req += 'User-Agent: Labyrinth/1 CFNetwork/758.2.8 Darwin/15.4.0\x0d\x0a'
req += '\x0d\x0a'

r = remote('52.34.144.0', 80)

r.send(req)
r.interactive()