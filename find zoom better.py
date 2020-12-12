# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:06:43 2020

@author: IEUser
"""


import urllib

url = "https://us04web.zoom.us/j/3333333333"
counter = int(input("start at? "))
def loop(counter):
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
    if not(w):
        print("nope tested \n",url)
        loop(counter)
loop(counter)
input("press enter to exit")