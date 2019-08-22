# coding: utf-8
with open('4.txt', 'r') as f:
    data = f.read()

from Crypto.Util.number import *

b = data.replace(' ', '0').replace('\t', '1')
print long_to_bytes(int(b, 2))
