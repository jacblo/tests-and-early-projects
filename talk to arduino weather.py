#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:17:35 2020

@author: y3
"""
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
    print("arduino: ",data)
    if data == "ask":
        city_name = "Bet shemesh,IL"
        weather_data = requests.get(api_address+city_name+api_key_url).json()
        tempurature = round(weather_data["main"]["temp"]-273.15,2)
        tempuratureInt = int(str(tempurature)[:-3])
        tempuratureDec = int(str(tempurature)[3:])
        arduino.write(struct.pack('!B',tempuratureInt))
        print(tempuratureInt)
        
        while not(str(arduino.readline())[2:-5] == tempuratureInt):
            pass
        
        arduino.write(struct.pack('!B',tempuratureDec))
        print("\n",round(tempurature,2)," - ",city_name,"\n")
        
        while not(str(arduino.readline())[2:-5] == str(int(round(weather_data["main"]["temp"]-273.15)))):
            pass
        
        city_name = "Jerusalem, IL"
        weather_data = requests.get(api_address+city_name+api_key_url).json()
        tempurature = round(weather_data["main"]["temp"]-273.15,2)
        tempuratureInt = int(str(tempurature)[:-3])
        tempuratureDec = int(str(tempurature)[3:])
        arduino.write(struct.pack('!B',tempuratureInt))
        print(tempuratureInt)
        
        while not(str(arduino.readline())[2:-5] == tempuratureInt):
            pass
        
        arduino.write(struct.pack('!B',tempuratureDec))
        print("\n",round(tempurature,2)," - ",city_name,"\n")
        
        while not(str(arduino.readline())[2:-5] == str(int(round(weather_data["main"]["temp"]-273.15)))):
            pass
        
        city_name = "Rochester, US"
        weather_data = requests.get(api_address+city_name+api_key_url).json()
        tempurature = round(weather_data["main"]["temp"]-273.15,2)
        tempuratureInt = int(str(tempurature)[:-3])
        tempuratureDec = int(str(tempurature)[3:])
        arduino.write(struct.pack('!B',tempuratureInt))
        print(tempuratureInt)
        
        while not(str(arduino.readline())[2:-5] == tempuratureInt):
            pass
        
        arduino.write(struct.pack('!B',tempuratureDec))
        print("\n",round(tempurature,2)," - ",city_name,"\n")
        
        while not(str(arduino.readline())[2:-5] == str(int(round(weather_data["main"]["temp"]-273.15)))):
            pass
        
        city_name = "Hollywood, US"
        weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?id=4158928&appid=749e8aa818a63c61c31acd7ee948d6d8").json()
        tempurature = round(weather_data["main"]["temp"]-273.15,2)
        tempuratureInt = int(str(tempurature)[:-3])
        tempuratureDec = int(str(tempurature)[3:])
        arduino.write(struct.pack('!B',tempuratureInt))
        print(tempuratureInt)
        
        while not(str(arduino.readline())[2:-5] == tempuratureInt):
            pass
        
        arduino.write(struct.pack('!B',tempuratureDec))
        print("\n",round(tempurature,2)," - ",city_name,"\n")
        
        
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
        print("\n",int(round(weather_data["main"]["temp"]-273.15))-1," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int((weather_data["main"]["temp"]-273.15))-1))
        
        
        while not(str(arduino.readline())[2:-5] == str(int((weather_data["main"]["temp"]-273.15))-1)):
            pass
        
        print("\ndecimal value - ",int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])))
        read = arduino.readline()
        
        print(round(weather_data["main"]["temp"]-273.15,2)," - ",city_name) 
        
        while str(arduino.readline())[2:-5] != int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1]):
            if str(read)[2:-5] == str(int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])):
                break         
        
        
        
        
        city_name = "Jerusalem, IL"
        weather_data = requests.get(api_address+city_name+api_key_url).json()
        print("\n",int(round(weather_data["main"]["temp"]-273.15))-1," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(round(weather_data["main"]["temp"]-273.15))-1))
        
        while not(str(arduino.readline())[2:-5] == str(int(round(weather_data["main"]["temp"]-273.15))-1)):
            pass
        
        
        print("\ndecimal value - ",int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])))
        read = arduino.readline()
        
        print(round(weather_data["main"]["temp"]-273.15,2)," - ",city_name) 
        
        while str(arduino.readline())[2:-5] != int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1]):
            if str(read)[2:-5] == str(int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])):
                break       
        
        
        
        city_name = "Rochester, US"
        weather_data = requests.get(api_address+city_name+api_key_url).json()
        print("\n",int(round(weather_data["main"]["temp"]-273.15))-1," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(round(weather_data["main"]["temp"]-273.15))-1))
        
        while not(str(arduino.readline())[2:-5] == str(int(round(weather_data["main"]["temp"]-273.15))-1)):
            pass
        
        print("\ndecimal value - ",int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])))
        read = arduino.readline()
        
        print(round(weather_data["main"]["temp"]-273.15,2)," - ",city_name) 
        
        while str(arduino.readline())[2:-5] != int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1]):
            if str(read)[2:-5] == str(int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])):
                break          
        
        
        city_name = "Hollywood, US"
        weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?id=4158928&appid=749e8aa818a63c61c31acd7ee948d6d8").json()
        print("\n",int(round(weather_data["main"]["temp"]-273.15))-1," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(round(weather_data["main"]["temp"]-273.15))-1))
        
        while not(str(arduino.readline())[2:-5] == str(int(round(weather_data["main"]["temp"]-273.15))-1)):
            pass
        
        
        print("\ndecimal value - ",int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])," - ",city_name,"\n")
        arduino.write(struct.pack('!B',int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])))
        read = arduino.readline()
        
        print(round(weather_data["main"]["temp"]-273.15,2)," - ",city_name) 
        
        while str(arduino.readline())[2:-5] != int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1]):
            if str(read)[2:-5] == str(int(str(round(weather_data["main"]["temp"]-273.15,2)).split(".")[1])):
                break   
        
        
    print(data)