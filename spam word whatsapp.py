#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:08:53 2020

@author: J Block
"""


from screenshotAndKeypressTests import *
import time
from subprocess import Popen, PIPE
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

def spam(text = "atuk",number = 10,waitSec = 1):
    time.sleep(waitSec)
    for x in range(number):
        keypress(bytes("str "+text+" ","utf-8"))
        keypress(b"key Return\n")

master = tk.Tk()
master.title("Group message spammer")
master.geometry('250x80')
canvas = Canvas(master, width = 600, height = 200)
tk.Label(master, text="text: ").grid(row=0)
tk.Label(master, text="num: ").grid(row=1)
tk.Label(master, text="timer (sec): ").grid(row=2)

text = tk.Entry(master)
text.grid(row=0, column=1)

num= Spinbox(master, from_ = 0 , to = 100 , width=5)
num.grid(column = 1 , row = 1)

var = StringVar(master)
var.set("5")
timer = Spinbox(master, from_ = 0 , to = 1000 , width=5 , textvariable=var)
timer.grid(column = 1 , row = 2)

def clicked():
    spam(str(text.get()),int(num.get()),int(timer.get()))

btn = Button(master, text="Go", command=clicked)
btn.grid(column = 0, row = 3)

master.mainloop()