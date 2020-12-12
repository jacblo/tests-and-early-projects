# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:10:48 2020

-----------------
settlers of catan
-----------------

@author: jblock
"""

def clicked():
    txt.delete(1.0,END)
    
    
def save():
    txt.insert(INSERT,"im alive!\nyou saved me!\n\n\n\n\n\n\n\n\n\n\n\n\n\ni even scroll!")

from tkinter import *

from tkinter import filedialog

from tkinter import scrolledtext

from tkinter import messagebox

from tkinter.ttk import Progressbar


window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('800x800')

canvas = Canvas(window, width = 300, height = 300)   

file = filedialog.askopenfilename(filetypes = (("png image","*.png"),("all files","*.*")))

img = PhotoImage(file=file)
canvas.create_image(1000,1000, anchor=NW, image=img)     

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2,row=0)

btn2 = Button(window, text="Click Me", command=save)

btn2.grid(column=2,row=2)

txt = scrolledtext.ScrolledText(window,width=40,height=10)

txt.grid(column=0,row=0)

txt.insert(INSERT,'You text goes here\nblah glob haksjdgflakdfhjasdfkjhaskjdhflhhsd haksjdgflakdfhjasdfkjhaskjdhflhhsd haksjdgflakdfhjasdfkjhaskjdhflhhsd\n\nn\n\n\nn\n\n\nn\n\n\nn\n\n\nn\n\n\nn\n\nfdf\nn\n\n\nn\n\n\nn\n\ngdgf\nn\n\n\nn\n\n\nn\n\ndf')

messagebox.showinfo('Message title','antidisetablishmenttarianisum jk im weird\n\nblob!')

spin = Spinbox(window, from_ = 0 , to = 100 , width=5)
spin.grid(column = 3 , row = 2)


var =IntVar()

var.set(200)

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 70

bar.grid(column=0, row=4)

spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)

spin.grid(column = 3 , row = 3)



dir = filedialog.askdirectory()


window.mainloop()