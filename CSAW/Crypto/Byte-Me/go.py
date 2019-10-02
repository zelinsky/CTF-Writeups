from pwn import *
from Crypto.Util.number import *
from string import printable
p = printable[:-5]

flag = 'flag{'

def go():
    global flag
    i = 5
    while True:
        r = remote('crypto.chal.csaw.io', 1003)
        ct = r.recvline().strip()
        r.recv()
        
	    r.sendline(flag+c)
            r.recvline()
            z = r.recvline().strip()
            r.recv()
            if z[32*(i-1):32*i] == ct[:32]:
                i+=1
		flag+=c
                print flag
		return 
	r.close()       
    


