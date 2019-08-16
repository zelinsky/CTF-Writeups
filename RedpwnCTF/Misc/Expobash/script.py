from pwn import * 

r = remote('chall2.2019.redpwn.net', 6005) 

print(r.recv())

print(r.recv())

r.sendline('15') 


print(r.recv())

data = r.recv() 

def calc_pset(a): 
    subsets = [] 
    for i in range(1, 2**len(a)): 
        binary = "0"*(len(a) - len(bin(i)[2:])) + bin(i)[2:]
        subset = [] 
        for j in range(len(binary)): 
            if binary[j] == "1": 
               subset.append(a[j]) 
        subsets.append(subset) 
    return subsets
def calc_sum(pset, b): 
    summed = 0 
    for p in pset: 
        for i in range(len(p)): 
            summed = (summed + (p[i] ^ b[i])) % 10**10
    return summed
from math import factorial
def nCr(n, k): 
    return factorial(n) / (factorial(n - k)*factorial(k)) 
def quick_sum(a, b): 
    summed = 0 
    for i in range(len(a)): 
        for j in range(i + 1): 
            summed = (summed + (a[i] ^ b[j])*(2**(len(a) - 1 - i)*nCr(i, j))) % 10**10
    
    return summed
a, b = data.strip().split('\n')  

a = map(int, a.split(" ")) 
b = map(int, b.split(" ")) 

pset = calc_pset(a) 
#print(pset) 
summed = calc_sum(pset, b) 

r.sendline(str(summed) ) 

while True: 

    print(r.recv()) 

    data = r.recv() 
    a, b = data.strip().split('\n') 
    print(data) 
    a = map(int, a.split(" ")) 
    b = map(int, b.split(" ")) 

    #pset = calc_pset(a) 

    summed = quick_sum(a, b) 
    #print(summed, quick_sum(a, b)) 
    r.sendline(str(summed)) 
