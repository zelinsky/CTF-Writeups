# coding: utf-8
from pwn import *
def calc_sum(pset, b):
    s = 0
    for subset in pset:
        for i in range(len(subset)):
           s = (s + (subset[i] ^ b[i])) % 10**10
    return s
def calc_pset(a):
    subsets = []
    for i in range(1, 2**len(a)):
        i = '0'*(len(a)-(len(bin(i))-2)) + bin(i)[2:]
        subset = [a[j] for j in range(len(i)) if i[j]=='1']
        subsets.append(subset)
    return subsets

def go():
    r = remote('chall2.2019.redpwn.net', 6005)
    for i in range(100):
        n = int(r.recvline().strip())
        a = r.recvline().strip()
	b = r.recvline().strip()
	print n, a, b
        a = a.split(' ')
	b = b.split(' ')
	a = map(int, a)
	b = map(int, b)
	pset = calc_pset(a)
	s = calc_sum(pset, b)
	print s
	r.sendline(str(s))

go()

