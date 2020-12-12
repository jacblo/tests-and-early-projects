#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:14:07 2020

@author: y3
"""
import time
import random
import numpy

z = int(input("how many numbers to test? "))

input("start genarating 2d positions?")
print("\ngenarating positions 2d\n")
positions2d = []
for x in range(z):
    pos1 = (random.randrange(int(z/2),z),random.randrange(int(z/2),z))
    pos2 = (random.randrange(int(z/2),z),random.randrange(int(z/2),z))
    positions2d.append((pos1,pos2))
print("done")

input("start genarating 3d positions?")
print("\ngenarating positions 3d\n")
positions3d = []

for x in range(z):
    pos1 = (random.randrange(int(z/2),z),random.randrange(int(z/2),z),random.randrange(int(z/2),z))
    pos2 = (random.randrange(int(z/2),z),random.randrange(int(z/2),z),random.randrange(int(z/2),z))
    pos3 = (random.randrange(int(z/2),z),random.randrange(int(z/2),z),random.randrange(int(z/2),z))
    positions3d.append((pos1,pos2,pos3))

print("done")



input("start to do calculations for 2d linear? (square)")
print("\nstarting to do calculations for 2d linear (square)\n")
time1 = time.time()
for x in positions2d:
    distance = (abs(x[0][0] - x[1][0]),abs(x[0][1] - x[1][1]))

time2 = time.time()
linear2dtime = time2 - time1
print("done")

input("start calculations for 2d radius? (circle)")

print("\nstarting to do calculations for 2d radius (circle)")
time3 = time.time()
for x in positions2d:
    distance = numpy.sqrt(float((x[0][0] - x[1][0])**2+(x[0][1]- x[1][1])**2))

time4 = time.time()
radius2dtime = time4 - time3
print("done")

input("start calculations for 3d linear? (cube)")

print("\nstarting to do calculations for 3d linear (cube)")

time5 = time.time()
for x in positions3d:
    distance = (abs(x[0][0] - x[1][0]),abs(x[0][1] - x[1][1]),abs(x[0][2] - x[1][2]))
time6 = time.time()
linear3dtime = time6 - time5
print("done")

input("start calculations for 3d radius? (sphere)")

print("\nstarting to do calculations for 3d radius (sphere)")
time7 = time.time()
for x in positions3d:
    distance = numpy.sqrt(float((x[0][0] - x[1][0]**2)**2+(x[0][1] - x[1][1])**2+(x[0][2] - x[1][2])**2))

time8 = time.time()
radius3dtime = time8 - time7
print("done")
print("\ntimes:\n---------")
print(f"2d linear (square) - {linear2dtime} seconds\n2d radius (circle) - {radius2dtime} seconds\n\n3d linear (cube) - {linear3dtime} seconds\n3d radius (sphere) - {radius3dtime} seconds\n")