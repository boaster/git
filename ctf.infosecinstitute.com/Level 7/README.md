# ctf.infosecinstitute.com: Level 7
**Bounty:** $70
**Description:**

> f00 not found 
> Something is not right here???
> btw...bounty $70

## Write-up

The link for "Level 7" takes us to 404.php, which returns HTTP Response Code 404 Not Found. However if we follow the URI scheme from the previous levels we know that the page for each level is located at /level<one/two/three/four/five/six/...>.php. So let's not follow the link to 404.php but instead let's request /levelseven.php.

```bash
$ curl -v http://ctf.infosecinstitute.com/levelseven.php
* Hostname was NOT found in DNS cache
*   Trying 52.10.161.229...
* Connected to ctf.infosecinstitute.com (52.10.161.229) port 80 (#0)
> GET /levelseven.php HTTP/1.1
> User-Agent: curl/7.38.0
> Host: ctf.infosecinstitute.com
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 aW5mb3NlY19mbGFnaXNfeW91Zm91bmRpdA==
< Date: Mon, 16 Mar 2015 16:49:03 GMT
< Server: Apache/2.4.7 (Ubuntu)
< X-Powered-By: PHP/5.5.9-1ubuntu4.6
< Content-Length: 0
< Connection: close
< Content-Type: text/html
<
* Closing connection 0
```
Now we see HTTP Response Code 200 OK and in place of the Error code's message "OK", we are presented with a base64 encoded string.
Decoding the string gives us the flag.

```bash
$ echo -n 'aW5mb3NlY19mbGFnaXNfeW91Zm91bmRpdA==' | base64 -d
infosec_flagis_youfoundit
```
