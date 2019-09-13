from PIL import Image
import PIL.ImageOps
import imagehash
import subprocess
import os

im3 = Image.open('data/3/0.jpg')
h3_1 = imagehash.average_hash(im3)
im3.close()
im3 = Image.open('data/3/3.jpg')
h3_2 = imagehash.average_hash(im3)
im3.close()
im3 = Image.open('data/3/26.jpg')
h3_3 = imagehash.average_hash(im3)
im3.close()
im3 = Image.open('data/3/54.jpg')
h3_4 = imagehash.average_hash(im3)
im3.close()
im3 = Image.open('data/3/138.jpg')
h3_5 = imagehash.average_hash(im3)
im3.close()
im3 = Image.open('data/3/302.jpg')
h3_6 = imagehash.average_hash(im3)
im3.close()
im3 = Image.open('data/3/2537.jpg')
h3_7 = imagehash.average_hash(im3)
im3.close()
im3 = Image.open('data/6/177.jpg')
h3_8 = imagehash.average_hash(im3)
im3.close()

im6 = Image.open('data/6/1.jpg')
h6_1 = imagehash.average_hash(im6)
im6.close()
im6 = Image.open('data/6/6.jpg')
h6_2 = imagehash.average_hash(im6)
im6.close()
im6 = Image.open('data/6/52.jpg')
h6_3 = imagehash.average_hash(im6)
im6.close()
im6 = Image.open('data/6/99.jpg')
h6_4 = imagehash.average_hash(im6)
im6.close()
im6 = Image.open('data/6/201.jpg')
h6_5 = imagehash.average_hash(im6)
im6.close()
im6 = Image.open('data/6/325.jpg')
h6_6 = imagehash.average_hash(im6)
im6.close()
im6 = Image.open('data/6/432.jpg')
h6_7 = imagehash.average_hash(im6)
im6.close()
im6 = Image.open('data/6/192.jpg')
h6_8 = imagehash.average_hash(im6)
im6.close()
images = subprocess.Popen('ls data/6/*.jpg', stdout=subprocess.PIPE, shell=True).communicate()[0].strip().split('\n')

def go():
    for i in images:
        im = Image.open(i)
	h = imagehash.average_hash(im)
        im.close()
        h3diff = abs(h3_1 - h) + abs(h3_2 - h) + abs(h3_3 - h) + abs(h3_4 - h) + abs(h3_5 - h) + abs(h3_6 - h) + abs(h3_7 - h) + abs(h3_8 - h)
        h3diff = h3diff/8.0
        h6diff = abs(h6_1 - h) + abs(h6_2 - h) + abs(h6_3 - h) + abs(h6_4 - h) + abs(h6_5 - h) + abs(h6_6 - h) + abs(h6_7 - h) + abs(h6_8 - h)
        h6diff = h6diff/8.0

        if h3diff < h6diff:
	    subprocess.Popen('mv '+i+' data/3/', stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
	    print i

