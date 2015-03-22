#!/usr/bin/env python

d = [[] for p in range(12)]
for i in range(12):
	for x in range(1, 13):
		if i == 0:
			d[i].append(x)
		else:
			d[i].append(d[0][i] * x)

for y in range(len(d)):
	print('{0:4}{1:4}{2:4}{3:4}{4:4}{5:4}{6:4}{7:4}{8:4}{9:4}{10:4}{11:4}'.format(*d[y]))

