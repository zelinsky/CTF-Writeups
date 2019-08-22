# coding: utf-8
with open('1.txt', 'r') as f:
    data = f.read().strip()
    
data.decode('base64')
data = data+'='
data.decode('base64')
text = data.decode('base64')
text.find('saudi')
s = text.find('saudi')
flag = text[s:s+38]
print flag
