# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:58:59 2020

@author: IEUser
"""

list1 = []
for x in range(0,40,5):
    a = x
    for y in range(0,40,5):
        b = y
        for z in range(0,40,5):
            c = z
            list1.append((a,b,c))
print(list1)
print("length ",len(list1))
list2 = []
for x in range(0,40):
    a = x
    for y in range(0,40):
        b = y
        for z in range(0,40):
            c = z
            list2.append((a,b,c))
print("\nlength it would have been ",len(list2))
print("\n")
for x in list1:
    print(x)
    x = input("press enter for next code to try")