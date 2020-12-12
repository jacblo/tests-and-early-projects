# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:31:34 2020

@author: IEUser
"""


import urllib
url = "https://us04web.zoom.us/j/3333333333"
counter = int(input("start at? "))
while True:
    url = "https://us04web.zoom.us/j/" + str(counter)
    
    counter += 1
    file = urllib.request.urlopen(url)
    
    w = False
    for line in file:
        decoded_line = line.decode("utf-8")
        x = decoded_line.lower().find("<input type=\"hidden\" id=\"data_is_iframe_verified\" value=\"true\">")
        if x != -1:
            print("online")
            w = True
            break
    if w:
        break
    else:
        print("nope tested \n",url)

input("press enter to exit")