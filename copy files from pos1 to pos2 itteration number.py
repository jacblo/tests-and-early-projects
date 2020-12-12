#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:10:32 2020

@author: y3
"""

from os import listdir
import shutil
from os.path import isfile, join

mypath = r"/home/y3/Pictures/photoscan/01"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for x in onlyfiles[:196:4]:
    original = r'/home/y3/Pictures/photoscan/01/'+x
    target = r'/home/y3/Desktop/photoscanFiles50/'+x
    shutil.copyfile(original, target)