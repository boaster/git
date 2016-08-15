#!/usr/bin/env python

import sys

data = 'UEsDBBQACAAIAOFR20gAAAAAAAAAAAAAAAAPABAAdHJvbGxfY2xvdWQucG5nVVgMAEw1cVflNHFXHMFgL927hVeWy/c+/NDdHdIl3V3S3QLS0iUI0h2ChICISElLSUs3KI2UdJd0d8NvHs7nXev7N7ysxXEd1twze/bsfe3r2vfckRpq8hiopKgQCARDUUFGCwKB'
file1 = ['659.bin']
lookup = 'cQe/ZMiI4C/0cPirEAgVRFHmhY6XyX46kh'

for a in range(853):
	found = False
	print
	for i in reversed(range(853)):
		infile1 = open('results-syns/' + str(i) + '.bin', 'r').read()
		if lookup in infile1 and str(i)+'.bin' not in file1:
			print str(i)+'.bin'
			found = True
			file2 = str(i)+'.bin'
			infile2 = open('results-syns/' + file2, 'r').read().strip()
			infile1 = open('results-syns/' + file1[-1], 'r').read().strip()
			l = 10
			for x in range(40):
#				print l
#				print infile1[-l:]
#				print infile2[:l]
#				print "-----"
				if infile1[-l:] != infile2[:l]:
					l += 1
				elif l > 100:
					print "Can't find the overlap of files " + file1[-1] + " " + file2
					sys.exit(-1)
				else:
#					data += ' '
					data += infile2.split( infile2[:l] )[1]
#					print data
					break
			file1.append(file2)
			lookup = infile2[-10:]
			break
	if not found:
		print "File without continuation: " + file1[-1]
#		print lookup
#		sys.exit(1)
	if file1[-1] == '339.bin':
		outfile = open('solved.zip', 'w')
		outfile.write(data)
		outfile.close()
		print "All done, check solved.zip"
#		sys.exit(0)
	