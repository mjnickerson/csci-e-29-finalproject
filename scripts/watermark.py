"""
Citation:
This script was modified from the watermark package by Ivan Rocha, for use as a demo example:
https://github.com/theitrain/watermark
It has been modified to work with luigi LocalTarget and luiGUI
(inherited code does not allow specifying an input file, or an output; This code has added that)
"""

import os
import sys

from PIL import Image

EXTS = ('.jpg', '.png')

if len(sys.argv) < 3:
    print('Usage: watermark.py \'input image folder path\' \'logo path\' \'output folder path\' [topleft, topright, bottomleft, bottomright, center]')
    sys.exit()
elif len(sys.argv) == 5:
    #sys.argv[0] is calling the script
    in_path = sys.argv[1]
    lgo = sys.argv[2]
    out_path = sys.argv[3]
    pos = sys.argv[4]
else:
    in_path = sys.argv[1]
    lgo = sys.argv[2]
    out_path = sys.argv[3]
    pos = 'center'


def add_watermark(in_path,lgo,out_path,pos):
    input_filename = os.path.basename(in_path)
    logo = Image.open(lgo)
    lgo_filename = os.path.basename(lgo)
    logoWidth = logo.width
    logoHeight = logo.height

    with Image.open(in_path) as image:
        imageWidth = image.width
        imageHeight = image.height
        try:
            if input_filename != lgo_filename:
                if pos == 'topleft':
                    image.paste(logo, (0, 0), logo)
                elif pos == 'topright':
                    image.paste(logo, (imageWidth - logoWidth, 0), logo)
                elif pos == 'bottomleft':
                    image.paste(logo, (0, imageHeight - logoHeight), logo)
                elif pos == 'bottomright':
                    image.paste(logo, (imageWidth - logoWidth, imageHeight - logoHeight), logo)
                elif pos == 'center':
                    image.paste(logo, (round((imageWidth - logoWidth)/2), round((imageHeight - logoHeight)/2)), logo)
                else:
                    print('Error: ' + pos + ' is not a valid position')
                    print('Usage: watermark.py \'image path\' \'logo path\' [topleft, topright, bottomleft, bottomright, center]')
                image.save(out_path)
                print('Added watermark to ' + out_path)
        except:
            image.paste(logo, (round((imageWidth - logoWidth)/2), round((imageHeight - logoHeight)/2)), logo)
            image.save(out_path)
            print('Added default watermark to ' + out_path)

#Run function
add_watermark(in_path,lgo,out_path,pos)