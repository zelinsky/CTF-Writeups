from PIL import Image
import PIL.ImageOps
import imagehash
import subprocess
import os



def f(n):
    im3 = Image.open('data/6/'+str(n)+'.jpg')
    h3 = imagehash.dhash(im3)
    im3.close()
    images = subprocess.Popen('ls data/6/*.jpg', stdout=subprocess.PIPE, shell=True).communicate()[0].strip().split('\n')

    for i in images:
        im = Image.open(i)
	h = imagehash.dhash(im)
        im.close()
 

        if h == h3:
	    subprocess.Popen('mv '+i+' data/3/', stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
	    print i

def g(n):
    for x in n:
	f(x)
