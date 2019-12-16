
"""
Citation:
This script was used verbatim from the watermark package by Ivan Rocha, for use as a demo example:
https://github.com/theitrain/watermark
"""

import os
import sys

from PIL import Image

EXTS = ('.jpg', '.png')

if len(sys.argv) < 3:
    print('Usage: watermark.py \'image folder path\' \'logo path\' [topleft, topright, bottomleft, bottomright, center]')
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

logo = Image.open(lgo)
logoWidth = logo.width
logoHeight = logo.height


for filename in os.listdir(in_path):
    if any([filename.lower().endswith(ext) for ext in EXTS]) and filename != lgo:
        image = Image.open(in_path + '/' + filename)
        imageWidth = image.width
        imageHeight = image.height

        try:
            if pos == 'topleft':
                image.paste(logo, (0, 0), logo)
            elif pos == 'topright':
                image.paste(logo, (imageWidth - logoWidth, 0), logo)
            elif pos == 'bottomleft':
                image.paste(logo, (0, imageHeight - logoHeight), logo)
            elif pos == 'bottomright':
                image.paste(logo, (imageWidth - logoWidth, imageHeight - logoHeight), logo)
            elif pos == 'center':
                image.paste(logo, ((imageWidth - logoWidth)/2, (imageHeight - logoHeight)/2), logo)
            else:
                print('Error: ' + pos + ' is not a valid position')
                print('Usage: watermark.py \'image path\' \'logo path\' [topleft, topright, bottomleft, bottomright, center]')

            image.save(out_path + '/' + filename)
            print('Added watermark to ' + out_path + '/' + filename)

        except:
            image.paste(logo, ((imageWidth - logoWidth)/2, (imageHeight - logoHeight)/2), logo)
            image.save(out_path + '/' + filename)
            print('Added default watermark to ' + out_path + '/' + filename)
