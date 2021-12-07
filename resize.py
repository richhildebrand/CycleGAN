#!/usr/bin/python
from PIL import Image
import os, sys

input_path = "./faces/input/"
output_path = "./faces/output/"
dirs = os.listdir(input_path)

def resize():
    for item in dirs:
        if os.path.isfile(input_path+item):
            im = Image.open(input_path+item)
            im = im.convert('RGB')
            f, e = os.path.splitext(input_path+item)
            imResize = im.resize((300, 300), Image.ANTIALIAS)
            imResize.save(output_path+item, 'JPEG', quality=90)
            #imResize.save(f + '_300.jpg', 'JPEG', quality=90)

resize()