# coding: utf-8
with open('3.txt', 'r') as f:
    data = f.read().strip()
    
s = 'PIZZAwithCheese'
        
for i, c in enumerate(data):
    if c not in s:
        print i, c
        
print data[62527:62548]
