from PIL import Image
import PIL.ImageOps
import imagehash
import subprocess
import os
import hashlib




images3 = subprocess.Popen('ls data/3/*.jpg', stdout=subprocess.PIPE, shell=True).communicate()[0].strip().split('\n')
images6 = subprocess.Popen('ls data/6/*.jpg', stdout=subprocess.PIPE, shell=True).communicate()[0].strip().split('\n')
hash3 = []
hash6 = []
 
for i in images3:
    with open(i, 'rb') as f:
        data = f.read()
	hash3.append(hashlib.md5(data).hexdigest())


for i in images6:
    with open(i, 'rb') as f:
        data = f.read()
	hash6.append(hashlib.md5(data).hexdigest())

print len(set(hash3)), len(set(hash6))
