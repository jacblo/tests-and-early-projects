# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:27:09 2020

@author: IEUser
"""

x = input("what is the text? ")
y = ""
for x in x:
    z = ord(x) 
    for x in range(z):
        y = y + "Blub. Blub. "
    y = y + "Blub! Blub. Blub. Blub? "

print(y)