#!/usr/bin/python

import fnmatch

import os

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

#for root, dirnames, filenames in os.walk("C:\\Users\\Jessicah Princess\\Desktop\\UAT\\"):

for root, dirnames, filenames in os.walk("/Users/keshavkummari/KK/"):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))
            print(matches)

