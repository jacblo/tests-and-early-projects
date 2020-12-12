#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:04:10 2020

@author: y3

749e8aa818a63c61c31acd7ee948d6d8
"""

import requests

api_address = "https://api.openweathermap.org/data/2.5/weather?q="
api_key_url = "&APPID=749e8aa818a63c61c31acd7ee948d6d8"
city_name = "Bet shemesh,IL"
weather_data = requests.get(api_address+city_name+api_key_url).json()
print(weather_data["main"]["temp"])