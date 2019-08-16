# coding: utf-8
from PIL import Image
import PIL.ImageOps
import pytesseract
import subprocess
import os

def open_image(im_name):
    size = (400, 600)
    with open(im_name, 'r') as f:
    	values = f.read().strip()
    values = values.split()
    new_values = []
    for v in values:
        t = []
        for c in v[1:-1].split(','):
            t.append(int(c))
        new_values.append(tuple(t))
    im = Image.new('RGB', size)
    im.putdata(new_values)
    im = im.transpose(Image.ROTATE_90)
    im = im.transpose(Image.FLIP_TOP_BOTTOM)
    im = PIL.ImageOps.invert(im)
    return im

def get_password(im):
    return pytesseract.image_to_string(im, config='--psm 6 --dpi 71 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz').lower()

def unzip(zip_name, password):
    s = subprocess.Popen(('unzip -P '+password+' '+zip_name).split(), stdout=subprocess.PIPE)
    return s.communicate()

def get_dir():
    return subprocess.Popen('ls -d */', stdout=subprocess.PIPE, shell=True).communicate()[0].strip()

def get_zip():
    return subprocess.Popen('ls *.zip', stdout=subprocess.PIPE, shell=True).communicate()[0].strip()

def get_png():
    return subprocess.Popen('ls *.png', stdout=subprocess.PIPE, shell=True).communicate()[0].strip()

def rm_dir():
    return subprocess.Popen('rmdir */', stdout=subprocess.PIPE, shell=True).communicate()

def go():
    i = 0
    while True:
        try:
            i = 1
            im = open_image(get_png())
            i = 0
            p = get_password(im)
            print unzip(get_zip(), p)
            os.chdir(get_dir())
        except:
            if i == 1:
                os.chdir('../')
            im.show()
            p = raw_input("Password: ")
            print unzip(get_zip(), p)
            os.chdir(get_dir())

