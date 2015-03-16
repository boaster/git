# ctf.infosecinstitute.com: Level 1
**Bounty:** $10
**Description:**

> May the source be with you!

## Write-up

Simple enough, the flag is within a HTML comment tag in the source code.

```bash
$ curl http://ctf.infosecinstitute.com/levelone.php | grep flag
<!-- infosec_flagis_welcome -->
```

