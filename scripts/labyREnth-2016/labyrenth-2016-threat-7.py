#!/usr/bin/env python



def encrypt(data, key, port):
    AABBCC = len(data)/float(len(key))
    while str(AABBCC).split(".")[1] != "0":
        data += "@"
        AABBCC = len(data)/float(len(key))
    AABBCD = int(str((AABBCC)).split(".")[0]) * 8
    final = []
    data = list(data)
    key = list(key)
    print data
    print key

    while data != []:
        p_data = data[0:8]
        p_key = key[0:8]
        print p_data
        print p_key
        new_key = []
        for i in xrange(0,8):
            if type(p_key[i]) == int:                                       # [+] *** ALERT ALERT *** [+]
                AABBB2 = (ord(chr(p_key[i])) ^ ord(p_data[0]))              # [+] HUMANS HAVE BROKEN THROUGH [+]
            else:                                                           # [+] MODULATE SHIELDS [+]
                AABBB2 = (ord(p_key[i]) ^ ord(p_data[0]))                   # [+] *** ALERT ALERT *** [+]
            final.append(AABBB2)
            new_key.append(AABBB2)
            data.pop(0)
            p_data.pop(0)
            key = new_key
        key.reverse()
    final.reverse()
    AABBB4 = []
    for i in final:
        AABBB3 = hex(i)
        if len(AABBB3) != 4:
            AABBB4.append("0" + hex(i)[2:])
        else:
            AABBB4.append(hex(i)[2:])
    AABBB4 = "".join(AABBB4).upper()
    return AABBB4

def decrypt(data, key):
    data = list(bytearray.fromhex(data))
    newData = [data[x:x+8][::-1] for x in range(0, len(data), 8)][::-1]
    final = ''
    key = bytearray(key)
    for x in range(len(newData)):
        for y in range(len(newData[x])):
            final += chr(newData[x][y] ^ key[y])
        key = newData[x][::-1]
    return final.strip("@")


print encrypt('https://www.youtube.com/watch?v=rTAx8r_090o', 'borgcard', 25)
print decrypt('046E3210462A496D5479450650722E44367A33283E3726641347435D400C0C0B7E6E696E3E2C2A3C4B5D5B1017061B0A', 'borgcard')
print decrypt('374316062B033D0A3E6A746B46560377367A3328393720611641435A400C0C0B7E6E696E392C2C394E5B5B1717061B0A', 'borgdata')
print decrypt('2E0C1C3D047D1563544012447D5C4C6E367A33283E2336651257575D400C0C0B7E6E696E3E383A3D4A4D4F1017061B0A', 'borgcube')
print decrypt('2E0C1C3D047D1563544012447D5C4C6E367A33283E2336651257575D400C0C0B7E6E696E3E383A3D4A4D4F1017061B0A', 'borgcube')
