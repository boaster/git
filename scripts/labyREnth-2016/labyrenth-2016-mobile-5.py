#!/usr/bin/env python

'''
root@snitcher:~# curl -v panspacedungeon.com -H "User-Agent: Labyrinth/1 CFNetwork/758.2.8 Darwin/15.4.0"
* Rebuilt URL to: panspacedungeon.com/
* Hostname was NOT found in DNS cache
*   Trying 52.34.144.0...
* Connected to panspacedungeon.com (52.34.144.0) port 80 (#0)
> GET / HTTP/1.1
> Host: panspacedungeon.com
> Accept: */*
> User-Agent: Labyrinth/1 CFNetwork/758.2.8 Darwin/15.4.0
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 8
< Server: Werkzeug/0.11.10 Python/2.7.6
< Date: Wed, 27 Jul 2016 17:19:45 GMT
<
* Closing connection 0
M4z3Cub3root@snitcher:~#
'''


def check_flag(s):
	v = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$_+=-?{}'
	for i in s:
		if i not in v:
			return False
	if s.count('{') > 1 or s.count('}') > 1 or s.count('_') > 1:
		return False

	return True

def check_key(s):
	v = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	for i in s:
		if i not in v:
			return False
	return True

def cr(kp):
	f = [0x1d, 0x75, 0x34, 0x48, 4, 0x46, 0x16, 0x6c, 0x1e, 0x57, 0x12, 2, 0x25, 0x42, 0x1b, 0x4e]
	if len(kp) == 3:
		k = 'M4z3' + kp + '3'
	else:
		k = kp

	final = ''
	for i in range(len(f)):
		final += chr(f[i] ^ ord(k[i % len(k)]))

	return final, k


'''
for a in range(0x41, 0x7f):
	for b in range(0x30, 0x40):
		for c in range(0x61, 0x7f):
			flag, key = cr( chr(a) + chr(b) + chr(c) )
			if check_flag(flag) and check_key(key):
				print key + " : " + flag
'''


print '\n'.join(cr( 'Cub' ))

#75b
#asB
#A !