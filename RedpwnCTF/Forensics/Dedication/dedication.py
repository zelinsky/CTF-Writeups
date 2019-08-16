# coding: utf-8
from PIL import Image
with open('jjofpbwvgk.png', 'r') as f:
    values = f.read().strip()
    
values = values.split(' ')

count = 0
for i in range(len(values)):
    if values[i][0] == '\n':
        print i
        count += 1
print count
for i in range(len(values)):
    if values[i][0] == '\n':
        values[i] = values[i][1:]
        
new_values = []

for v in values:
    t = []
    for c in v[1:-1].split(','):
        t.append(int(c))
    new_values.append(tuple(t))
    

size = 400, 600
im = Image.new('RGB', size)


new_values
im.putdata(new_values)
im.save('1.png')
