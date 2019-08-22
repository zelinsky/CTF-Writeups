# coding: utf-8
from Crypto.Util.number import *
with open('5.txt', 'r') as f:
    data = f.read()
    
len(data)
data
1990 % 8
b = data.replace('cheese', '0').replace('pizza', '1').replace(' ', '0').replace('\t', '1')
b
long_to_bytes(int(b, 2))
