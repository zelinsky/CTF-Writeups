from PIL import Image
import PIL.ImageOps
import imagehash
import subprocess
import os

im3 = Image.open('data/3/0.jpg')
h3 = imagehash.average_hash(im3)
im3.close()
im6 = Image.open('data/6/1.jpg')
h6 = imagehash.average_hash(im6)
im6.close()
images = subprocess.Popen('ls data/*.jpg', stdout=subprocess.PIPE, shell=True).communicate()[0].strip().split('\n')

def go():
    for i in images:
        print i
        im = Image.open(i)
	h = imagehash.average_hash(im)
        im.close()
        if abs(h3 - h) < abs(h6 - h):
	    subprocess.Popen('mv '+i+' data/3', stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
        else:
	    subprocess.Popen('mv '+i+' data/6', stdout=subprocess.PIPE, shell=True).communicate()[0].strip()

