#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:10:32 2020

@author: y3
"""

from copy import deepcopy

display = [[0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]

characters = ("  ","⬛⬛","΀΀")

def showscreen(display):
    print("-"*35)
    for y in display:
        for x in y:
            print("|",characters[x],end="|")
        print("\n"+"-"*35)

def place(x,player):
    if display[0][x] != 0:
        return False
    y = 1
    for row in display[::-1]:
        state = row[x]
        if state == 0:
            display[-y][x] = player
            return True
        y += 1    
    return False

def fakeplace(x,player,display):
    if display[0][x] != 0:
        return False
    y = 1
    for row in display[::-1]:
        state = row[x]
        if state == 0:
            display2 = deepcopy(display)
            display2[-y][x] = player
            return display2
        y += 1
    return False

def checkWinner(current):
    for y in range(len(current)):
        for x in range(len(current[y])):
            try:
                if current[y][x] == 1 and current[y][x+1] == 1 and current[y][x+2] == 1 and current[y][x+3] == 1:
                    return 1
                elif current[y][x] == 2 and current[y][x+1] == 2 and current[y][x+2] == 2 and current[y][x+3] == 2:
                    return 2
            except:
                pass
            
            try:
                if current[y][x] == 1 and current[y+1][x] == 1 and current[y+2][x] == 1 and current[y+3][x] == 1:
                    return 1
                elif current[y][x] == 2 and current[y+1][x] == 2 and current[y+2][x] == 2 and current[y+3][x] == 2:
                    return 2
            except:
                pass
            
            try:
                if current[y][x] == 1 and current[y+1][x+1] == 1 and current[y+2][x+2] == 1 and current[y+3][x+3] == 1:
                    return 1
                elif current[y][x] == 2 and current[y+1][x+1] == 2 and current[y+2][x+2] == 2 and current[y+3][x+3] == 2:
                    return 2
            except:
                pass
            
            try:
                if current[y][x] == 1 and current[y+1][x-1] == 1 and current[y+2][x-2] == 1 and current[y+3][x-3] == 1:
                    return 1
                elif current[y][x] == 2 and current[y+1][x+1] == 2 and current[y+2][x+2] == 2 and current[y+3][x+3] == 2:
                    return 2
            except:
                pass
            
    return 0

def gamePVP():
    while True:
        for player in range(1,3):
            showscreen(display)
            while True:
                pos = input(f"player {player} what row do you want to place your character in? ")
                try:
                    pos = int(pos)-1
                    break
                except:
                    print("not a valid input try again")
            place(pos,player)
            win = checkWinner(display)
            if win != 0:
                showscreen(display)
                print(f"player {win} has won.")
                return
            



def giveAllOptions(toTest,player):
    opts = []
    for x in range(7):
        opts.append([x,fakeplace(x,player,toTest)])
    return opts

def computerNextMove(player):
    LastPossibilities = giveAllOptions(display,player)
    possibilities = []
    while True:
        for turn in range(1,3):
            for x in LastPossibilities:
                opts = giveAllOptions(x[1],turn)
                for a,b in opts:
                    if checkWinner(b) == player:
                        place(a,player)
                        return a
                    elif checkWinner(b) == 0:
                        possibilities.append([x[0],b])
        LastPossibilities = deepcopy(possibilities)
        possibilities = []
            
def gamePVC():
    showscreen(display)
    while True:
        player = 1
        
        while True:
            pos = input(f"player what row do you want to place your character in? ")
            try:
                pos = int(pos)-1
                break
            except:
                print("not a valid input try again")
        place(pos,player)
        showscreen(display)
        win = checkWinner(display)
        if win != 0:
            showscreen(display)
            if win == 1:
                print("player has won.")
            else:
                print("computer has won.")
            return
        computerNextMove(2)
        print("computer went")
        showscreen(display)
        win = checkWinner(display)
        if win != 0:
            showscreen(display)
            if win == 1:
                print("player has won.")
            else:
                print("computer has won.")
            return

gamePVC()