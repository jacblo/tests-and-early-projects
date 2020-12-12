#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:56:25 2020

@author: y3
"""


import PIL
import numpy as np
from PIL import Image
import random

pixels = []
for y in range(1000):
    w = []
    for x in range(1000):
        w.append((255,255,255))
    pixels.append(w)
    
counter = 0
for y in pixels:
    y[500] = (0,0,0)
    y[501] = (0,0,0)
    pixels[counter] = y
    counter += 1;
    
w = []
for y in range(1000):
    w.append((0,0,0))

pixels[500] = w
pixels[501] = w


counter = 0
for x in pixels[::50]:
    
    l = 480
    for w in range(480,521):
        x[l] = (0,0,0)
        l += 1
    
    pixels[counter] = x
    
    counter += 50


for y in range(480,521):
    z = pixels[y]
    counter = 0
    for x in z[::50]:
        z[counter] = (0,0,0)
        
        counter += 50
    pixels[y] = z

for x in range(int(input("how many points? "))):
    Posx = random.randrange(0,1000)
    Posy = random.randrange(0,1000)
    
    try:
        pixels[Posy][Posx] = (0,0,0)
        pixels[Posy][Posx+1] = (0,0,0)
        pixels[Posy+1][Posx] = (0,0,0)
        pixels[Posy+1][Posx+1] = (0,0,0)
        pixels[Posy][Posx-1] = (0,0,0)
        pixels[Posy-1][Posx] = (0,0,0)
        pixels[Posy-1][Posx-1] = (0,0,0)
        pixels[Posy-1][Posx+1] = (0,0,0)
        pixels[Posy+1][Posx-1] = (0,0,0)
    except:
        pass
    else:
        pixels[Posy][Posx] = (0,0,0)
        pixels[Posy][Posx+1] = (0,0,0)
        pixels[Posy+1][Posx] = (0,0,0)
        pixels[Posy+1][Posx+1] = (0,0,0)
        pixels[Posy][Posx-1] = (0,0,0)
        pixels[Posy-1][Posx] = (0,0,0)
        pixels[Posy-1][Posx-1] = (0,0,0)
        pixels[Posy-1][Posx+1] = (0,0,0)
        pixels[Posy+1][Posx-1] = (0,0,0)
    
        

data = np.array(pixels)
#data = np.random.random((100,100))

#Rescale to 0-255 and convert to uint8
rescaled = (255.0 / data.max() * (data - data.min())).astype(np.uint8)

im = Image.fromarray(rescaled)
im.save('test.png')


image = Image.open('test.png')
image.show()