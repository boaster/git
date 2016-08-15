#!/usr/bin/env python

# flag: PAN{L3ts_533_h0W_U_deal_w_th1s_little_511CE}

infile = open('bowie.pl', 'r').read().split("\n")
outfile = open('solution.txt', 'w')


def find_flag(data):
	try:
		for l in data:
			if '$input eq' in l:
				l = l.split('eq ')[1].split(' {')[0].replace('.', '+')[:-1]
				answer = eval(l)
				outfile.write(answer + "\n")
#				continue
			elif 'eval' in l:
				l = l.split('"')[1].decode('base64').split('\n')
				find_flag(l)
	except:
		print 'Done'

find_flag(infile)