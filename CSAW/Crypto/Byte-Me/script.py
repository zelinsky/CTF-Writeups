from pwn import *
import string
r = remote('crypto.chal.csaw.io', 1003)
enc_flag = r.recvline().strip()
r.recv()


h = string.hexdigits[0:-6]
p = string.printable[:-5]
flag = ''






for i in range(15, -1, -1):
    s = 'A'*i
    print s
    r.sendline(s)
    r.recvline()
    a = r.recvline().strip()[:32]
    print a
    r.recv()
    for c in p:
        guess = 'A'*i + flag + c
        r.sendline(guess)
        r.recvline()
        z = r.recvline().strip()[:32]
	r.recv()
        if z == a:
            flag += c
	    print c
            break

print flag
    

