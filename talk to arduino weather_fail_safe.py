#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:17:35 2020

@author: y3
"""


import requests
import struct
import serial
import time

api_address = "https://api.openweathermap.org/data/2.5/weather?q="
api_key_url = "&APPID=749e8aa818a63c61c31acd7ee948d6d8"

arduino=serial.Serial("/dev/ttyACM1",baudrate = 9600, timeout = 1)

while True:
    data = str(arduino.readline())[2:-5]
    if data == "ask":
        city_name = "Bet shemesh,IL"
        weather_data = requests.get(api_address+city_name+api_key_url).json()
        print("\n",int(round(weather_data["main"]["temp"]-273.15))," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(round(weather_data["main"]["temp"]-273.15))))
        
        while not(str(arduino.readline())[2:-5] == str(int(round(weather_data["main"]["temp"]-273.15)))):
            pass
        
        city_name = "Jerusalem, IL"
        weather_data = requests.get(api_address+city_name+api_key_url).json()
        print("\n",int(round(weather_data["main"]["temp"]-273.15))," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(round(weather_data["main"]["temp"]-273.15))))
        
        while not(str(arduino.readline())[2:-5] == str(int(round(weather_data["main"]["temp"]-273.15)))):
            pass
        
        city_name = "Rochester, US"
        weather_data = requests.get(api_address+city_name+api_key_url).json()
        print("\n",int(round(weather_data["main"]["temp"]-273.15))," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(round(weather_data["main"]["temp"]-273.15))))
        
        while not(str(arduino.readline())[2:-5] == str(int(round(weather_data["main"]["temp"]-273.15)))):
            pass
        
        city_name = "Hollywood, US"
        weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?id=4158928&appid=749e8aa818a63c61c31acd7ee948d6d8").json()
        print("\n",int(round(weather_data["main"]["temp"]-273.15))," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(round(weather_data["main"]["temp"]-273.15))))
        
        
    print(data)