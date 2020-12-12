#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:43:40 2020

@author: y3
"""

import requests
import os

while True:
    try:
        requests.get("https://www.google.com")
    except:
        print("No internet or something")
    else:
        print("\n\n\n----------------------------------\n----------------------------------\nyay! internet is on!!!\n----------------------------------\n----------------------------------\n")
        os.system('notify-send "yay!" "There is internet!!"')
        break