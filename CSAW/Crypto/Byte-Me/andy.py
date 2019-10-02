from pwn import *
from Crypto.Util.number import *
from string import printable
p = printable[:-5]

r = remote('crypto.chal.csaw.io', 1003)

ct = r.recvline().strip()
r.recv()

lookup = {}
for c1 in p:
    r.sendline(c) 
    r.recvline()
    temp = r.recvline().strip()
    r.recv()
    lookup[c] = temp


print lookup
