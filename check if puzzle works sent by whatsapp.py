#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:36:34 2020

@author: y3
"""

whatsapp = 1
instagram = 2
like = 3

screen = [[4,4,4,4,4,4,4,4,4,4,4,4],
          [4,4,4,4,4,4,4,4,4,4,4,4],
          [4,4,4,4,4,4,4,4,4,4,4,4],
          
          [4,4,4, 2,3,1,3,2,3 ,4,4,4],
          [4,4,4, 2,2,3,2,2,2 ,4,4,4],
          [4,4,4, 1,3,3,3,1,2 ,4,4,4],
          [4,4,4, 3,2,3,2,3,1 ,4,4,4],
          [4,4,4, 1,2,1,3,2,2 ,4,4,4],
          [4,4,4, 2,2,2,1,3,2 ,4,4,4],
          
          [4,4,4,4,4,4,4,4,4,4,4,4],
          [4,4,4,4,4,4,4,4,4,4,4,4],
          [4,4,4,4,4,4,4,4,4,4,4,4]]

target = (3,(5,5))

instegramsThatWork = []
whatsapps = []
countey = 0
for y in screen:
    countex = 0
    for x in y:
        if x == 1:
            whatsapps.append((countey,countex))
        countex += 1
    
    countey += 1
    
for z in whatsapps:
    nearLikes = []
    nearLikes.append([screen[z[0]-1][z[1]-1],[z[0]-1,z[1]-1]])
    nearLikes.append([screen[z[0]+1][z[1]+1],[z[0]+1,z[1]+1]])
    nearLikes.append([screen[z[0]-1][z[1]+1],[z[0]-1,z[1]+1]])
    nearLikes.append([screen[z[0]+1][z[1]-1],[z[0]+1,z[1]-1]])
    nearLikes.append([screen[z[0]-1][z[1]],[z[0]-1,z[1]]])
    nearLikes.append([screen[z[0]+1][z[1]],[z[0]+1,z[1]]])
    nearLikes.append([screen[z[0]][z[1]-1],[z[0],z[1]-1]])
    nearLikes.append([screen[z[0]][z[1]+1],[z[0],z[1]+1]])
    
    for x in nearLikes:
        if x[0] == 3:
            if screen[x[1][0] + 1][x[1][1]] == 2:
                pos = [x[1][0] + 1,x[1][1]]
            elif screen[x[1][0]][x[1][1]+1] == 2:
                pos = [x[1][0],x[1][1] + 1]
            instegramsThatWork.append(pos)

for x in instegramsThatWork:
    if screen[x[0]+1][x[1]+1] == target[0] and (x[0]+1,x[1]+1) == target[1]:
        print("worked")
    elif screen[x[0]+2][x[1]+2] == target[0] and (x[0]+2,x[1]+2) == target[1]:
        print("worked")
    elif screen[x[0]+3][x[1]+3] == target[0] and (x[0]+3,x[1]+3) == target[1]:
        print("worked")
        
    elif screen[x[0]-1][x[1]-1] == target[0] and (x[0]-1,x[1]-1) == target[1]:
        print("worked")
    elif screen[x[0]-2][x[1]-2] == target[0] and (x[0]-2,x[1]-2) == target[1]:
        print("worked")
    elif screen[x[0]-3][x[1]-3] == target[0] and (x[0]-3,x[1]-3) == target[1]:
        print("worked")
    
    elif screen[x[0]-1][x[1]+1] == target[0] and (x[0]-1,x[1]+1) == target[1]:
        print("worked")
    elif screen[x[0]-2][x[1]+2] == target[0] and (x[0]-2,x[1]+2) == target[1]:
        print("worked")
    elif screen[x[0]-3][x[1]+3] == target[0] and (x[0]-3,x[1]+3) == target[1]:
        print("worked")
    
    elif screen[x[0]+1][x[1]-1] == target[0] and (x[0]+1,x[1]-1) == target[1]:
        print("worked")
    elif screen[x[0]+2][x[1]-2] == target[0] and (x[0]+2,x[1]-2) == target[1]:
        print("worked")
    elif screen[x[0]+3][x[1]-3] == target[0] and (x[0]+3,x[1]-3) == target[1]:
        print("worked")
    
    else:
        print("didnt work")