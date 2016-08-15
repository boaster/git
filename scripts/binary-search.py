#!/usr/bin/env python

def binarySearch(alist, item):
	first = 0
	last = len(alist)-1
	found = False

	while first <= last and not found:
		mid = (first + last) / 2
		if alist[mid] == item:
			found = True
		else:
			if item < alist[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found

l = [1, 3, 6, 13, 15, 17, 21, 24, 26, 31, 33, 37, 41, 46, 47]
print binarySearch(l, 21)