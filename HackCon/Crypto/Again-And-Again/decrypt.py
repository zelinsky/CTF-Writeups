c = 196353764385075548782571270052469419021844481625366305056739966550926484027148967165867708531585849658610359148759560853

p = 5411451825594838998340467286736301586172550389366579819551237
q = 5190863621109915362542582192103708448607732254433829935869841
n = p * q
from Crypto.Util.number import * 
from string import printable
from gmpy2 import iroot
def modular_sqrt(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)

        Returns 1 if a has a square root modulo
        p, -1 otherwise.
    """
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls
def egcd(a,b):   
    s1, s2 = 1, 0   
    t1, t2 = 0, 1   
    while b!=0:   
        q = a//b    
        r = a%b   
        a, b = b, r     
        s = s1-q*s2    
        s1, s2 = s2, s      
        t = t1-q*t2    
        t1, t2 = t2, t    
    return (s1, t1)

def decrypt_rabin(c): 
    mp = modular_sqrt(c, p)
    mq = modular_sqrt(c, q) 
    #print(mp, mq) 
    yp, yq = egcd(p, q) 
    
    r1 = (yp*p*mq + yq*q*mp) % n 

    r2 = n - r1 

    r3 = (yp*p*mq - yq*q*mp) % n 

    r4 = n - r3 

    return r1, r2, r3, r4 


r1, r2, r3, r4 = decrypt_rabin(c) 
def isprintable(string): 
    return all(map(lambda x: x in printable, string))  
totient = (p - 1)*(q -1) 

x = list(decrypt_rabin(c)) 


def decrypt(cipher,count): 
    for boi in list(decrypt_rabin(cipher)): 
        if isprintable(long_to_bytes(boi)): 
            print(long_to_bytes(boi)) 
        elif (count > 15):
            return 
        else: 
            decrypt(boi, count + 1)

decrypt(c, 0) 
'''
def decrypt_recur(cipher, count): 
    if (isprintable(long_to_bytes(cipher))): 
        print(long_to_bytes(cipher)) 
        return
    elif (count > 10): 
        return 
    else: 
        r1, r2, r3, r4 = decrypt_rabin(c) 
        decrypt_recur(r1, count + 1) 
        decrypt_recur(r2, count + 1) 
        decrypt_recur(r3, count + 1) 
        decrypt_recur(r4, count + 1) 
        return
decrypt_recur(c, 0) 
'''
"""
hm = 3948272944438794908086979061048684029846766654391354173615908574371760300121872926068323428117422567939667803260281957 

x = list(decrypt_rabin(c)) 

for boi in x: 
    lad = boi 
    for i in range(10000): 
        hms = list(decrypt_rabin(lad))
        found = False
        for bitch in hms: 
            if (isprintable(long_to_bytes(bitch))): 
                print(long_to_bytes(bitch)) 
            if bitch > hm:
                print(i, boi) 
                lad = bitch 
                found = True
        if not(found): 
            break

     
""" 


