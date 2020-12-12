# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:10:48 2020

-----------------
settlers of catan
-----------------

@author: jblock
"""


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

window = Toplevel()
window.title("Welcome to LikeGeeks app")
window.geometry('240x240')

grid = [None, None, None, 
        None, None, None, 
        None, None, None]
turn = 0
type_ = "x"
def xo1(turn = turn):
    if turn == 0:
        if type_ == "x":
            grid[0] = "x"
            btn1 = Button(window,text = "  x " ,command = xo1)
            btn1.grid(column = 1,row = 1)
            
        else:
            btn1 = Button(window,text = "  o " ,command = xo1)
            btn1.grid(column = 1,row = 1)
    else:
        if type_ == "x":
            btn1 = Button(window,text = "  o " ,command = xo1)
            btn1.grid(column = 1,row = 1)
        else:
            grid[0] = "x"
            btn1 = Button(window,text = "  x " ,command = xo1)
            btn1.grid(column = 1,row = 1)
            if turn == 1:
                turn = 0
            else:
                turn = 1

def xo2(turn = turn):
    if turn == 0:
        if type_ == "x":
            grid[1] = "x"
            btn2 = Button(window,text = "  x " ,command = xo2)
            btn2.grid(column = 2,row = 1)
        else:
            grid[1] = "o"
            btn2 = Button(window,text = "  o " ,command = xo2)
            btn2.grid(column = 2,row = 1)
    else:
        if type_ == "x":
            grid[1] = "o"
            btn2 = Button(window,text = "  o " ,command = xo2)
            btn2.grid(column = 2,row = 1)
        else:
            grid[1] = "x"
            btn2 = Button(window,text = "  x " ,command = xo2)
            btn2.grid(column = 2,row = 1)
            if turn == 1:
                turn = 0
            else:
                turn = 1

def xo3(turn = turn):
    if turn == 0:
        if type_ == "x":
            grid[2] = "x"
            btn3 = Button(window,text = "  x " ,command = xo3)
            btn3.grid(column = 3,row = 1)
        else:
            grid[2] = "o"
            btn3 = Button(window,text = "  o " ,command = xo3)
            btn3.grid(column = 3,row = 1)
    else:
        if type_ == "x":
            grid[2] = "o"
            btn3 = Button(window,text = "  o " ,command = xo3)
            btn3.grid(column = 3,row = 1)
        else:
            grid[2] = "x"
            btn3 = Button(window,text = "  x " ,command = xo3)
            btn3.grid(column = 3,row = 1)
            if turn == 1:
                turn = 0
            else:
                turn = 1

def xo4(turn = turn):
    if turn == 0:
        if type_ == "x":
            grid[3] = "x"
            btn4 = Button(window,text = "  x " ,command = xo4)
            btn4.grid(column = 1,row = 2)
        else:
            grid[3] = "o"
            btn4 = Button(window,text = "  o " ,command = xo4)
            btn4.grid(column = 1,row = 2)
    else:
        if type_ == "x":
            grid[3] = "o"
            btn4 = Button(window,text = "  o" ,command = xo4)
            btn4.grid(column = 1,row = 2)
        else:
            grid[3] = "x"
            btn4 = Button(window,text = "  x " ,command = xo4)
            btn4.grid(column = 1,row = 2)
            if turn == 1:
                turn = 0
            else:
                turn = 1

def xo5(turn = turn):
    if turn == 0:
        if type_ == "x":
            grid[4] = "x"
            btn5 = Button(window,text = "  x " ,command = xo5)
            btn5.grid(column = 2,row = 2)
        else:
            grid[4] = "o"
            btn5 = Button(window,text = "  o " ,command = xo5)
            btn5.grid(column = 2,row = 2)
    else:
        if type_ == "x":
            grid[4] = "o"
            btn5 = Button(window,text = "  o " ,command = xo5)
            btn5.grid(column = 2,row = 2)
        else:
            grid[4] = "x"
            btn5 = Button(window,text = "  x " ,command = xo5)
            btn5.grid(column = 2,row = 2)
            if turn == 1:
                turn = 0
            else:
                turn = 1

def xo6(turn = turn):
    if turn == 0:
        if type_ == "x":
            grid[5] = "x"
            btn6 = Button(window,text = "  x " ,command = xo6)
            btn6.grid(column = 3,row = 2)
        else:
            grid[5] = "o"
            btn6 = Button(window,text = "  o " ,command = xo6)
            btn6.grid(column = 3,row = 2)
    else:
        if type_ == "x":
            grid[5] = "o"
            btn6 = Button(window,text = "  o " ,command = xo6)
            btn6.grid(column = 3,row = 2)
        else:
            grid[5] = "x"
            btn6 = Button(window,text = "  x " ,command = xo6)
            btn6.grid(column = 3,row = 2)
            if turn == 1:
                turn = 0
            else:
                turn = 1
            
def xo7(turn = turn):
    if turn == 0:
        if type_ == "x":
            grid[6] = "x"
            btn7 = Button(window,text = "  x " ,command = xo7)
            btn7.grid(column = 1,row = 3)
        else:
            grid[6] = "o"
            btn7 = Button(window,text = "  o " ,command = xo7)
            btn7.grid(column = 1,row = 3)
    else:
        if type_ == "x":
            grid[6] = "o"
            btn7 = Button(window,text = "  o " ,command = xo7)
            btn7.grid(column = 1,row = 3)
        else:
            grid[6] = "x"
            btn7 = Button(window,text = "  x " ,command = xo7)
            btn7.grid(column = 1,row = 3)
            if turn == 1:
                turn = 0
            else:
                turn = 1

def xo8(turn = turn):
    if turn == 0:
        if type_ == "x":
            grid[7] = "x"
            btn8 = Button(window,text = "  x " ,command = xo8)
            btn8.grid(column = 2,row = 3)
        else:
            grid[7] = "o"
            btn8 = Button(window,text = "  o " ,command = xo8)
            btn8.grid(column = 2,row = 3)
    else:
        if type_ == "x":
            grid[7] = "o"
            btn8 = Button(window,text = "  o " ,command = xo8)
            btn8.grid(column = 2,row = 3)
        else:
            grid[7] = "x"
            btn8 = Button(window,text = "  x " ,command = xo8)
            btn8.grid(column = 2,row = 3)
            if turn == 1:
                turn = 0
            else:
                turn = 1

def xo9(turn = turn):
    if turn == 0:
        if type_ == "x":
            grid[8] = "x"
            btn9 = Button(window,text = "  x " ,command = xo9)
            btn9.grid(column = 3,row = 3)
        else:
            grid[8] = "o"
            btn9 = Button(window,text = "  o " ,command = xo9)
            btn9.grid(column = 3,row = 3)
    else:
        if type_ == "x":
            grid[8] = "o"
            btn9 = Button(window,text = "  o " ,command = xo9)
            btn9.grid(column = 3,row = 3)
        else:
            grid[8] = "x"
            btn9 = Button(window,text = "  x " ,command = xo9)
            btn9.grid(column = 3,row = 3)
            if turn == 1:
                turn = 0
            else:
                turn = 1


#pos by numpad pos
btn1 = Button(window,text = "    " ,command = xo1)
btn1.grid(column = 1,row = 1)
btn2 = Button(window,text = "    " ,command = xo2)
btn2.grid(column = 2,row = 1)
btn3 = Button(window,text = "    " ,command = xo3)
btn3.grid(column = 3,row = 1)
btn4 = Button(window,text = "    " ,command = xo4)
btn4.grid(column = 1,row = 2)
btn5 = Button(window,text = "    " ,command = xo5)
btn5.grid(column = 2,row = 2)
btn6 = Button(window,text = "    " ,command = xo6)
btn6.grid(column = 3,row = 2)
btn7 = Button(window,text = "    " ,command = xo7)
btn7.grid(column = 1,row = 3)
btn8 = Button(window,text = "    " ,command = xo8)
btn8.grid(column = 2,row = 3)
btn9 = Button(window,text = "    " ,command = xo9)
btn9.grid(column = 3,row = 3)

window.mainloop()