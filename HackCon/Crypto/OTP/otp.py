# coding: utf-8
c1 = '\x05F\x17\x12\x14\x18\x01\x0c\x0b4'
c2 = '>\x1f\x00\x14\n\x08\x07Q\n\x0e'
len(c1)
len(c2)
from pwn import xor
xor(c1, c2)
xor('d4rk', c1)
xor('arey', c2)
xor('d4rk{', c1)
key = 'areyo'
xor('areyou', c1)
key = 'areyou'
xor(c2, 'aaaaa}c0de')
key = 'areyoudank'
xor(c1, dank)
xor(c1, key)
xor(c2, key)
__ + _
