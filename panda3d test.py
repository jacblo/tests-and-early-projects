#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:25:14 2020

@author: y3
"""


from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
import serial
import signal
import sys
import time


arduino=serial.Serial("/dev/ttyACM0",baudrate = 9600, timeout = 5)
axis1 = []
axis2 = []

def xyz():
    open('mocapResultTest.txt', 'w').close()
    with open("mocapResultTest.txt" ,mode = "w") as f:
        f.write(str(axis1)+","+str(axis2))

   

def keyboardInterruptHandler(signal, frame):

    xyz()

    #print("call your function here".format(signal))

    sys.exit(0)


signal.signal(signal.SIGINT, keyboardInterruptHandler)

"""
while True:
    time.sleep(1/24)
    
    print((str(arduino.readline())[2:-5]))
    mylist.append(int(str(arduino.readline())[2:-5]))
"""
#arduino=serial.Serial("/dev/ttyACM1",baudrate = 9600, timeout = 1)

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

 
        
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        
        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinPanda, "SpinPanda")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model")
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)

    # Define a procedure to move the camera.
    def spinPanda(self, task):
        
        x = str(arduino.readline())[2:-5].split(",")
        #axis1.append(int(x[0]))
        #axis1.append(int(x[1]))
        xyz()
        angleDegrees = int(str(arduino.readline())[2:-5])
        angleRadians = angleDegrees * (pi / 180.0)
        self.pandaActor.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.pandaActor.setHpr(angleDegrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()