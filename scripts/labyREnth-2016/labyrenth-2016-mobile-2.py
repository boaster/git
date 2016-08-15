#!/usr/bin/env python

def solve(ac):
    ai = [0] * 37
    ai[0] = 453     # = > ? @
    ai[1] = 431     # e f g h
    ai[2] = 409     # i j k l
    ai[3] = 342     # u v w x
    ai[4] = 318
    ai[5] = 293
    ai[6] = 460
    ai[7] = 273
    ai[8] = 383
    ai[9] = 369
    ai[10] = 374
    ai[11] = 466
    ai[12] = 261
    ai[13] = 380
    ai[14] = 513
    ai[15] = 267
    ai[16] = 301
    ai[17] = 266
    ai[18] = 310
    ai[19] = 437
    ai[20] = 260
    ai[21] = 325
    ai[22] = 379
    ai[23] = 333
    ai[24] = 454
    ai[25] = 350
    ai[26] = 345
    ai[27] = 460
    ai[28] = 293
    ai[29] = 303
    ai[30] = 289
    ai[31] = 290
    ai[32] = 438
    ai[33] = 373
    ai[34] = 264
    ai[35] = 309
    ai[36] = 351    # e f g h

    for i in range(len(ai)):
        ai[i] = chr( (ai[i] - 2 ^ (ord(ac[i % len(ac)]) - 19) + 86) >> 2)

    return ''.join(ai)
'''
for a in range(0x30, 0x7b):
    for b in range(0x30, 0x7b):
        print solve('@eiue' + chr(a) + chr(b))
'''

print solve('@eiuiaq')   # bruteforced all values