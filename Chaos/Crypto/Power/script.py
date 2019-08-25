# coding: utf-8
from pwn import *
from Crypto.Util.number import *
import gmpy2

p = 120593028296357385006581162098617812686966375949836034216796460150134082697045081008437566030641114890431946289306441183707778147667917880020449427007546850431679337774919585631877424444491101991966619587074111653863106657606465239416807311748212262947979172244596527049173626190097815972676667969225242064449

            
r = remote('hax.allesctf.net', 1337)
for i in range(10000):
    data = r.recvuntil('Response: ')
    num = [int(s) for s in data.split() if s.isdigit()][0]
    if gmpy2.is_prime(num):
        print i, num
        x = pow(pow(num, num, p), pow(num, num, p), p)
        if x == num:
            r.sendline(str(pow(num, num, p)))

	    print r.recv()
            break
    r.sendline(str(1))
    r.recvuntil('\n')
    
            
        
            
