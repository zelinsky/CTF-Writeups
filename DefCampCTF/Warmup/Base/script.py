from pwn import *
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
