#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:13:40 2020

@author: y3
"""
import time
import cv2
import pytesseract
import numpy as np
from PIL import Image
import pyscreenshot

time.sleep(10)
img = pyscreenshot.grab(bbox=(768,398,1181,534))
#cv2.imwrite("/home/y3/Desktop/tes1234t.png", np.array(imgOut.convert('RGB')).astype(np.uint8))
text = pytesseract.image_to_string(img)