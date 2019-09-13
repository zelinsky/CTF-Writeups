from PIL import Image
import PIL.ImageOps
import imagehash
import subprocess
import os
import hashlib


images3 = subprocess.Popen('ls data/6/*.jpg', stdout=subprocess.PIPE, shell=True).communicate()[0].strip().split('\n')
#images6 = subprocess.Popen('ls data/6/*.jpg', stdout=subprocess.PIPE, shell=True).communicate()[0].strip().split('\n')
hash3 = {}
#hash6 = []
 
for i in images3:
    im = Image.open(i)
    h = imagehash.dhash(im)
    im.close()
    hash3[i] = int(str(h), 16)


v = hash3.values()
s = 0.0
for i in v:
    s += i

s = s/len(v)

a = v[0]
m = abs(v[0] - s)
for i in v:
    if abs(i - s) > m and i != 17632265907812790788:
        m = abs(i-s)
	a = i

keys = [ key for key,value in hash3.items() if value==a]
print keys, a
