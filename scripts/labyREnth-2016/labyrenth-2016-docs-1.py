#!/usr/bin/env python

def func_2(message_1, int_key):
	final_str = '9ne8SXEB4h6VPDXEGvF5XQ6nmqo1cMzgwesrlQmwv1bk56AvtH0G0Muu8PWERNkayAzoUy7wm73NsyJJQdPGfGi8eISOlYDBvgd8uILCLLzkb6LEEn1seLsnPyYMPBu0QZOPYuBSuxanrqkoqttFIxE1ZHplAquJjJ8gjTLN6iD3AzPVNDOQ'
	final = ""
	final_counter = 1
	while final_counter < len(message_1) + 1:
		final_len = final_counter % len(final_str)
		print final_len
		break
		if final_len == 0:
			final_len = len(final_str)
		if (final_len + int_key) > len(final_str):
			c = 0
		else:
			c = ord(final_str[final_len + int_key-1])
		final += chr( c ^ message_1[final_counter - 1])
		final_counter = final_counter + 1
	return final

#print func_2([5, 5, 27, 65, 89, 98, 85, 86, 71, 75, 66, 92, 95, 98, 67, 64, 89, 83, 84, 95, 26, 78, 116, 78, 91, 5, 116, 32, 72, 2, 33, 48, 10, 29, 61, 8, 37, 20, 63, 44, 1, 12, 62, 38, 47, 52, 99, 57, 5, 121, 89, 37, 65, 32, 32, 11, 98, 42, 58, 32, 28, 9, 3, 117, 85, 4, 57, 10, 94, 0, 16, 8, 28, 42, 30, 121, 71, 6, 8, 9, 37, 2, 23, 34, 21, 120, 54, 7, 40, 35, 75, 50, 87, 3, 55, 47, 99, 52, 13, 0, 42, 30, 27, 126, 59, 3, 123, 29, 52, 44, 53, 29, 15, 50, 12, 35, 8, 48, 89, 54, 27, 62, 28, 8, 36, 49, 119, 104, 14, 5, 64, 34, 43, 22, 71, 5, 46, 7, 66, 42, 0, 1, 113, 97, 83, 31, 45, 95, 111, 31, 40, 51], 24)
#print func_2([42, 115, 2], 188)
#print func_2([116, 7, 6, 74, 60, 43, 42, 36, 64, 70, 110, 27, 28, 12, 12, 17, 23], 0)
#print func_2([15, 32, 32, 53, 35, 89, 22, 25, 65, 53, 51, 26], 176)
#print func_2([20, 39, 81, 118, 52, 78, 11], 17)

flag = '081916230e3102313a696b07683634216a2c30682b6b070f3068071336682f072f306b2a6b6a3468683325'
f = ''
for i in range(0, len(flag), 2):
	f += chr( int(flag[i:i+2], 16) ^ 0x58 )

print f

# PAN{ViZib13_0nly2th0s3_Wh0_Kn0w_wh3r32l00k}