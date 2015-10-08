#!/usr/bin/env python

from string import maketrans

key = "UDYs1D7bNmdE1o3g5ms1V6RrYCVvODJF1DpxKTxAJ9xuZW=="
test = "P62IS6AJPQkZTlwIS6ANRAkZPQoMORo0TAkZPQETORoMO6AIS7s1ORoM"

base64fixTable = maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/");

def correctbase64(str):
	    return str.translate(base64fixTable)

print correctbase64(test)
