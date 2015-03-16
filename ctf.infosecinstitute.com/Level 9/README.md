# ctf.infosecinstitute.com: Level 9
**Bounty:** $90
**Description:**

> CISCO IDS WEB LOGIN SYSTEM

## Write-up

Here we are presented with login page. Performing any SQL Injections or trying to trigger PHP Exception errors was not working. I googled CISCO default credentials and stumbled on the following page <http://portforward.com/default_username_password/CISCO.htm>, trying all credentials one by one I found a working one.
Username: root
Password: attack

After successfully logon we are presented with the following JavaScript alert message "alert('ssaptluafed_sigalf_cesofni')". Reading it backwards is the flag string.

```bash
$ python -c "print 'ssaptluafed_sigalf_cesofni' [::-1]"
infosec_flagis_defaultpass
```

