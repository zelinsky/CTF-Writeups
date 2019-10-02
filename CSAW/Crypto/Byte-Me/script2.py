from pwn import *
import string
r = remote('crypto.chal.csaw.io', 1003)
enc_flag = r.recvline().strip()
r.recv()


h = string.hexdigits[0:-6]
p = string.printable[:-5]
flag = ''

flag_len = 0
overflow = 0
for i in range(1, 17):
    s = 'A'*i
    r.sendline(s)
    r.recvline()
    a = r.recvline().strip()
    if len(a) > len(enc_flag):
        flag_len = len(enc_flag)/2-i+1
        overflow = i

print flag_len
print overflow


for i in range(15, -1, -1):
    s = 'A'*i
    r.sendline(s)
    r.recvline()
    a = r.recvline().strip()[:32]
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

print len(flag), flag
    

