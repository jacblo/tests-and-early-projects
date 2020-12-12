#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:28:48 2020

@author: y3
"""


import serial
import signal
import sys
import time

mylist = []

def xyz():
    open('mocapResultTest.txt', 'w').close()
    with open("mocapResultTest.txt" ,mode = "w") as f:
        f.write(str(mylist))

   

def keyboardInterruptHandler(signal, frame):

    xyz()

    #print("call your function here".format(signal))

    sys.exit(0)


signal.signal(signal.SIGINT, keyboardInterruptHandler)


while True:
    time.sleep(1/24)
    arduino=serial.Serial("/dev/ttyACM0",baudrate = 9600, timeout = 5)
    print((str(arduino.readline())[2:-5]))
    mylist.append(int(str(arduino.readline())[2:-5]))
