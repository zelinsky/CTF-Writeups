from PIL import Image
import PIL.ImageOps
import pytesseract
import subprocess
import os

os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/4.00/tessdata"

def go():
    for i in range(0, 34023):
	imname = str(i)+'.jpg'
        im = Image.open('data/'+imname)
        n = pytesseract.image_to_string(im, config='--psm 10 -c tessedit_char_whitelist=36 --oem 0 --tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"')
        im.close()
        if n == '3':
	    subprocess.Popen('mv data/'+imname+' data/3', stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
        elif n == '6':
	    subprocess.Popen('mv data/'+imname+' data/6', stdout=subprocess.PIPE, shell=True).communicate()[0].strip()
	print i, n
