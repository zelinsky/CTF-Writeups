# coding: utf-8
with open('2.txt', 'r') as f:    data = f.read().strip()
import string
for c in data:
    if c not in string.ascii_uppercase:
        print repr(c)
        
