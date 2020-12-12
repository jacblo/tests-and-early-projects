#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:32:15 2020

@author: y3
"""

import os
import PIL
import numpy
from PIL import Image 
import cv2
import numpy as np
from skimage import io

texturePackDir = input("texturePack directry: ")
imageDir = input("image directry: ")

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

texs = {}
for x in get_filepaths(texturePackDir):
    if x[-3:].lower() == "png":
        texture = io.imread(x)
        texs[tuple(texture.mean(axis=0).mean(axis=0)[:3])] = x[len(texturePackDir)+1:]

out = []
im = Image.open(imageDir)
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
for y in pixels:
    row = []
    for x in y:
        row.append(x[:3])
    out.append(row)