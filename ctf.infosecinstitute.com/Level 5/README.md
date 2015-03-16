# ctf.infosecinstitute.com: Level 5
**Bounty:** $50
**Description:**

> 

## Write-up

Upon loading the web page, we get a JavaScript loop with alert event. Instead I used curl to view the site. The source contained a link to an [image](aliens.jpg).
Downloading the [image](aliens.jpg) and running Steganography tool steghide I was able to extract text file [all.txt](all.txt). The file contained representation of binary data. Upon converting the binary digits to ascii we get the flag.

```bash
$ steghide extract -sf aliens.jpg
Enter passphrase:
wrote extracted data to "all.txt".
$ cat all.txt
01101001011011100110011001101111011100110110010101100011010111110110011001101100011000010110011101101001011100110101111101110011011101000110010101100111011000010110110001101001011001010110111001110011
$ python
>>> import binascii
>>> n = int('01101001011011100110011001101111011100110110010101100011010111110110011001101100011000010110011101101001011100110101111101110011011101000110010101100111011000010110110001101001011001010110111001110011', 2)
>>> binascii.unhexlify('%x' % n)
'infosec_flagis_stegaliens'
>>>
```

