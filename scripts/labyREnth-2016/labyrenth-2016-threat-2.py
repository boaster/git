#!/usr/bin/env python

'''
The rest of us, we died with our honor. @m1kachu_
#!/usr/bin/env python

infile = bytearray(open('all_data.hex', 'r').read().strip().decode('hex'))

for i in range(0x100):
	if i == 0xaa:
		new = ''
		ofile = open('xor-' + str(i) + '.raw', 'w')
		for x in infile:
			new += chr(x ^ i)
		ofile.write(new)
		ofile.close()

Write a YARA rule to find normal valid GIF files.

Write a YARA rule to detect all variations of this encoded data.
Using the template below:
1. replace each "**" pair in $header with the appropriate 6 bytes.
2. replace each "*" in $trailer with the appropriate regex.
3. replace the "*" in condition with the appropriate digit.

rule valid_gif : valid_gif
{
        strings:

                        $header = { ** ** ** ** ** ** }
                        $trailer = *******

        condition:
                        $header at * and $trailer
}

'''


from pwn import *

rule = '''rule valid_gif : valid_gif
{
        strings:

                        $header = { 47 49 46 38 39 61 }
                        $trailer = /\x3b$/

        condition:
                        $header at 0 and $trailer
}'''

# PAN{848Y_wIsh3D_4w4y}

r = remote('52.41.90.65', 2600)
r.send(rule)
r.interactive()


