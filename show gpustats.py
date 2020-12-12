 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:34:29 2020

@author: y4
"""

import subprocess
import tkinter as tk
from tkinter import *
master = tk.Tk()

info = subprocess.getoutput("gpustat").split("\n")
def esc(event):
    master.destroy()
master.bind('<Return>', esc)
master.bind('<Escape>', esc)
master.title("gpustat")
master.geometry('1340x'+str(len(info)*20))
text = Text(master)
def reload():
    text.config(state=NORMAL) 
    text.delete('1.0', END)
    info = subprocess.getoutput("gpustat").split("\n")
    text.pack(expand=1, fill=BOTH)
    for x in info:
        text.insert(INSERT, x+"\n")
    text.tag_add("red","1.0",END)
    text.tag_config("red", foreground="black", font = ("Bahnschrift", 14))
    text.config(state=DISABLED)
btn = Button(master, text="Reload", command=reload).place(x=1270, y=0)
reload()
master.mainloop()
