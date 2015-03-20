# ctf.infosecinstitute.com: Level 4
**Bounty:** $40
**Description:**

> HTTP means Hypertext Transfer Protocol

## Write-up

Website sets the following HTTP Cookie:

```bash
$ curl -I http://ctf.infosecinstitute.com/levelfour.php
HTTP/1.1 200 OK
Date: Mon, 16 Mar 2015 04:10:59 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.6
Set-Cookie: fusrodah=vasbfrp_syntvf_jrybirpbbxvrf
Content-Type: text/html
```

If we decrypt it using a simple substitution cipher ROT13, we get the flag.

```bash
$ echo 'vasbfrp_syntvf_jrybirpbbxvrf' | tr '[abcdefghijklmnopqrstuvwxyz]' '[nopqrstuvwxyzabcdefghijklm]'
infosec_flagis_welovecookies
```
## Links
* <http://ctf.infosecinstitute.com/levelfour.php>
