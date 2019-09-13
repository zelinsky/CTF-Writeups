# coding: utf-8
from pwn import *
r = remote('206.81.24.129', 4441)
r.recv()
r.recv()
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = int(q[q.find('<<') + 2: q.find('>')])
        print i
        h = hex(i)
        print h
        r.sendline(h)
        
go()
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = int(q[q.find('<<') + 2: q.find('>')])
        t = q[q.find('in')+2:q.find('?')]
        print i, t
        if t == 'hex':
            o = hex(i)
        elif t =='ASCII'"
            o = i.decode('hex')
        print o
        r.sendline(o)

        
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = int(q[q.find('<<') + 2: q.find('>')])
        t = q[q.find('in')+2:q.find('?')]
        print i, t
        if t == 'hex':
            o = hex(i)
        elif t =='ASCII'
            o = i.decode('hex')
        print o
        r.sendline(o)

        
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = int(q[q.find('<<') + 2: q.find('>')])
        t = q[q.find('in')+2:q.find('?')]
        print i, t
        if t == 'hex':
            o = hex(i)
        elif t =='ASCII':
            o = i.decode('hex')
        print o
        r.sendline(o)

        
go()
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = int(q[q.find('<<') + 2: q.find('>')])
        t = q[q.find('in')+2:q.find('?')]
        print i, t
        o = ''
        if t == 'hex':
            o = hex(i)
        elif t =='ASCII':
            o = i.decode('hex')
        print o
        r.sendline(o)

        
go()
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = int(q[q.find('<<') + 2: q.find('>')])
        t = q[q.find('in')+2:q.find('?')]
        print i, t
        o = 'A'
        if t == 'hex':
            o = hex(i)
        elif t =='ASCII':
            o = i.decode('hex')
        print o
        r.sendline(o)

        
go()
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = int(q[q.find('<<') + 2: q.find('>')])
        t = q[q.find('in ')+3:q.find('?')]
        print i, t
        o = 'A'
        if t == 'hex':
            o = hex(i)
        elif t =='ASCII':
            o = i.decode('hex')
        print o
        r.sendline(o)

        
go()
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = q[q.find('<<') + 2: q.find('>')]
        t = q[q.find('in ')+3:q.find('?')]
        print i, t
        o = 'A'
        if t == 'hex':
            o = hex(int(i))
        elif t =='ASCII':
            o = i.decode('hex')
        print o
        r.sendline(o)

        
go()
int('123 45')
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = q[q.find('<<') + 2: q.find('>')]
        t = q[q.find('in ')+3:q.find('?')]
        print i, t
        o = 'A'
        if t == 'hex':
            o = hex(int(i))
        elif t =='ASCII':
            try:
                o = i.decode('hex')
            except:
                o = i.split()
                o = map(lambda x: chr(int(x, 8)), o)
                o = o.join("")
        print o
        r.sendline(o)

        
go()
go()
def go():
    r = remote('206.81.24.129', 4441)
    while True:
        q = r.recvline()
        print q
        i = q[q.find('<<') + 2: q.find('>')]
        t = q[q.find('in ')+3:q.find('?')]
        print i, t
        o = 'A'
        if t == 'hex':
            o = hex(int(i))
        elif t =='ASCII':
            try:
                o = i.decode('hex')
            except:
                o = i.split()
                o = map(lambda x: chr(int(x, 8)), o)
                o = "".join(o)
        print o
        r.sendline(o)

        
go()
