# ctf.infosecinstitute.com: Level 8
**Bounty:** $80
**Description:**

> Do you want to download the [app.exe](app.exe) file?

## Write-up

Simply extracting any printable characters from the binary with "strings" does the trick for this one.

```bash
$ strings app.exe  | grep flagis
infosec_flagis_0x1a
```
## Links
* <http://ctf.infosecinstitute.com/leveleight.php>

