#!/usr/bin/env python

def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n+1, p)))
	return primes

for i in range(10000):
	if len(get_primes(i)) == 1000:
		print sum(get_primes(i))
		break
