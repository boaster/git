# ctf.infosecinstitute.com: Level 14
**Bounty:** $140
**Description:**

> Do you want to download [level14](level14) file?

## Write-up

The file provided for this level seems to be phpMyAdmin SQL Database Dump in ASCII. After some looking around I noticed the "friends" table had a stange entry under the name field for id 104. It's Unicode encoded string. To convert it to ASCII, I used an online tool after googling for "Unicode to ASCII online".

	'\\u0069\\u006e\\u0066\\u006f\\u0073\\u0065\\u0063\\u005f\\u0066\\u006c\\u0061\\u0067\\u0069\\u0073\\u005f\\u0077\\u0068\\u0061\\u0074\\u0073\\u006f\\u0072\\u0063\\u0065\\u0072\\u0079\\u0069\\u0073\\u0074\\u0068\\u0069\\u0073'

First let's remove one of the backslashes.
```bash
$ echo '\\u0069\\u006e\\u0066\\u006f\\u0073\\u0065\\u0063\\u005f\\u0066\\u006c\\u0061\\u0067\\u0069\\u0073\\u005f\\u0077\\u0068\\u0061\\u0074\\u0073\\u006f\\u0072\\u0063\\u0065\\u0072\\u0079\\u0069\\u0073\\u0074\\u0068\\u0069\\u0073' | sed 's/\\u/\u/g'
\u0069\u006e\u0066\u006f\u0073\u0065\u0063\u005f\u0066\u006c\u0061\u0067\u0069\u0073\u005f\u0077\u0068\u0061\u0074\u0073\u006f\u0072\u0063\u0065\u0072\u0079\u0069\u0073\u0074\u0068\u0069\u0073
```
And this is how you convert unicode to ASCII using Python.
```bash
$ python -c "print u'\u0069\u006e\u0066\u006f\u0073\u0065\u0063\u005f\u0066\u006c\u0061\u0067\u0069\u0073\u005f\u0077\u0068\u0061\u0074\u0073\u006f\u0072\u0063\u0065\u0072\u0079\u0069\u0073\u0074\u0068\u0069\u0073'"
infosec_flagis_whatsorceryisthis
```
## Links
* <http://ctf.infosecinstitute.com/leveltwo.php>

