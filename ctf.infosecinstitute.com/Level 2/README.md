# ctf.infosecinstitute.com: Level 2
**Bounty:** $20
**Description:**

> < It seems like the image is broken..Can you check the file ? >

## Write-up

Upon loading the web page, we see the link in the middle of the page is broken. By downloading the jpg image, we see that the web server returns a base64 encoded string instead of a jpg image. Decoding the base64 encoded string, provides us with the flag.

```bash
$ curl http://ctf.infosecinstitute.com/img/leveltwo.jpeg
aW5mb3NlY19mbGFnaXNfd2VhcmVqdXN0c3RhcnRpbmc=
$ curl http://ctf.infosecinstitute.com/img/leveltwo.jpeg | base64 -d
infosec_flagis_wearejuststarting
```
## Links
* <http://ctf.infosecinstitute.com/leveltwo.php>
