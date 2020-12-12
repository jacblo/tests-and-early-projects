#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:38:19 2020

@author: y3
"""

import numpy as np
import PIL
from PIL import *
def blackPix(lists):    
    positionBlackPixels = []
    counterY = 0
    counterX = 0
    for x in lists:
        for z in x:
            if z == [0,0,0,255]:
                positionBlackPixels.append((counterX,counterY))
            counterX += 1
        counterY += 1
    return positionBlackPixels

def blackSquare(lists):
    positionBlackSquare = []
    counterY = 0
    counterX = 0
    for x in lists:
        counterX=0
        for z in x:
            if z == [0,0,0,255] and x[counterX+1] == [0,0,0,255] and lists[counterY+1][counterX] == [0,0,0,255] and lists[counterY+1][counterX+1] == [0,0,0,255]:
                positionBlackSquare.append((counterX,counterY))
            counterX += 1
        counterY += 1
    
    return positionBlackSquare

def searchImage(image,search):
    out = []
    counterY = 0
    for y in image:
        counterX = 0
        for x in y:
            break_ = False
            #counter search y
            csy = 0
            for searchY in search:
                if break_:
                    break
                #counter search x
                csx = 0
                for searchX in searchY:
                    try:
                        image[counterY+csy][counterX+csx]
                    except:
                        break_ = True
                        break
                    if searchX != image[counterY+csy][counterX+csx]:
                        break_ = True
                        break
                    csx += 1
                csy += 1
            if not(break_):
                out.append((counterX,counterY))
            
            counterX += 1
        counterY += 1
        
    return out


x = input("path to image sequence ")
if x[-1] != "/":
    x = x+"/"
y = input("path to image to search for ")
image = np.asarray(Image.open(y)) 
searchVal = image.tolist()
name = 0
digits = 0
while True:
    try:
        np.asarray(Image.open((x+"0"*digits+'1.png'),mode = "r"))
    except:
        digits += 1
    else:
        try:
            np.asarray(Image.open((x+"0"*(digits-len(str(name))+1)+str(name)+'.png'),mode = "r"))
        except:
            name = 1
        break
while True: 
    try:
        np.asarray(Image.open((x+"0"*(digits-len(str(name))+1)+str(name)+'.png'),mode = "r"))
    except:
        break
    image = np.asarray(Image.open((x+"0"*(digits-len(str(name))+1)+str(name)+'.png'),mode="r"))
    lists = image.tolist()
    name += 1
    print(searchImage(lists,searchVal))