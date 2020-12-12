#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:18:56 2020

@author: y3
"""

import webbrowser
import urllib
import time
url = "https://example.com"

while True:
    #time.sleep(120)
    try:
        urllib.request.urlopen(url)
    except:
        print("nope")
    else:
        file = urllib.request.urlopen(url)
        for line in file:
            print(line)
        chrome_path = '/usr/bin/google-chrome'
        webbrowser.get(chrome_path).open(url)
        break