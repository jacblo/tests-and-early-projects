# -*- coding: utf-8 -*-
"""
tic tak toe
Created on Wed Apr  1 03:39:55 2020

@author: jabl
"""
def clear():
    print("\n\n\n\n\n\n\n")

def screen(one = " ",two = " ",three = " ",four = " ",five = " ",six = " ",seven = " ",eight = " ",nine = " "):
    print(f"\n {seven} | {eight} | {nine} \n-----------\n {four} | {five} | {six} \n-----------\n {one} | {two} | {three} \n")

#variables
oneOut = " "
twoOut = " "
threeOut = " "
fourOut = " "
fiveOut = " "
sixOut = " "
sevenOut = " "
eightOut = " "
nineOut = " "
placesx = [0,False,False,False,False,False,False,False,False,False]
placeso = [0,False,False,False,False,False,False,False,False,False]
player1type = ""
winner = 0
posIn = 0
turn = 1
turnNum = 0

#game
while True:
    #setup
        #reset variables
    oneOut = " "
    twoOut = " "
    threeOut = " "
    fourOut = " "
    fiveOut = " "
    sixOut = " "
    sevenOut = " "
    eightOut = " "
    nineOut = " "
    placesx = [0,False,False,False,False,False,False,False,False,False]
    placeso = [0,False,False,False,False,False,False,False,False,False]
    player1type = ""
    winner = 0
    posIn = 0
    turn = 1
    turnNum = 0
        #instructions
    print("to change a tile input numbers from 1 to 9 acording to numpad layout or acording to the illistration below")
    screen(1,2,3,4,5,6,7,8,9)
    while True:
        player1type = input("Player 1 what shape do you want to be? x/o ")
        if player1type != 'o' and player1type != 'x':
            print("you have not typed o/k please try again")
        else:
            break
    
    #game
    print("\nPlayer 1 starts\n")
    screen()
    while True:
        if (placesx[1] and placesx[2] and placesx[3]) or (placesx[4] and placesx[4] and placesx[5]) or (placesx[7] and placesx[8] and placesx[9]) or (placesx[1] and placesx[4] and placesx[7]) or (placesx[2] and placesx[5] and placesx[8]) or (placesx[3] and placesx[6] and placesx[9]) or (placesx[1] and placesx[5] and placesx[9]) or (placesx[7] and placesx[5] and placesx[3]):
            if player1type == 'x':
                winner = 1
            else:
                winner = 2
            break
        
        elif (placeso[1] and placeso[2] and placeso[3]) or (placeso[4] and placeso[5] and placeso[3]) or (placeso[7] and placeso[8] and placeso[9]) or (placeso[1] and placeso[4] and placeso[7]) or (placeso[2] and placeso[5] and placeso[8]) or (placeso[3] and placeso[6] and placeso[9]) or (placeso[1] and placeso[5] and placeso[9]) or (placeso[7] and placeso[5] and placeso[3]):
            if player1type == 'x':
                winner = 2
            else:
                winner = 1
            break
        elif (turnNum == 9):
            winner = 0
            break
        
        while True:
            posInStr = input("what position do you want to mark? (1-9 acording to numpad) ")
            posTaken= False
            try:
                int(posInStr)
            except:
                print("you have not inputed a number please try again\n")
            else:
                posIn = int(posInStr)
                posTaken = False               
                if placesx[posIn] == True:
                    posTaken = True
                if placeso[posIn] == True:
                    posTaken = True
                if posTaken:
                    print("you can't go there - that position is taken. try again")
                else:
                    if player1type == 'x':
                        if turn == 1:
                            placesx[posIn] = True
                        else:
                            placeso[posIn] = True
                    else:
                        if turn == 1:
                            placeso[posIn] = True
                        else:
                            placesx[posIn] = True
                    
                    break
        
        if posIn == 1:
            if player1type == 'x':
                if turn == 1:
                    oneOut = 'x'
                else:
                    oneOut = 'o'
            else:
                if turn == 1:
                    oneOut = 'o'
                else:
                    oneOut = 'x'
        elif posIn == 2:
            if player1type == 'x':
                if turn == 1:
                    twoOut = 'x'
                else:
                    twoOut = 'o'
            else:
                if turn == 1:
                    twoOut = 'o'
                else:
                    twoOut = 'x'
        elif posIn == 3:
            if player1type == 'x':
                if turn == 1:
                    threeOut = 'x'
                else:
                    threeOut = 'o'
            else:
                if turn == 1:
                    threeOut = 'o'
                else:
                    threeOut = 'x'
        elif posIn == 4:
            if player1type == 'x':
                if turn == 1:
                    fourOut = 'x'
                else:
                    fourOut = 'o'
            else:
                if turn == 1:
                    fourOut = 'o'
                else:
                    fourOut = 'x'
        elif posIn == 5:
            if player1type == 'x':
                if turn == 1:
                    fiveOut = 'x'
                else:
                    fiveOut = 'o'
            else:
                if turn == 1:
                    fiveOut = 'o'
                else:
                    fiveOut = 'x'
        elif posIn == 6:
            if player1type == 'x':
                if turn == 1:
                    sixOut = 'x'
                else:
                    sixOut = 'o'
            else:
                if turn == 1:
                    sixOut = 'o'
                else:
                    sixOut = 'x'
        elif posIn == 7:
            if player1type == 'x':
                if turn == 1:
                    sevenOut = 'x'
                else:
                    sevenOut = 'o'
            else:
                if turn == 1:
                    sevenOut = 'o'
                else:
                    sevenOut = 'x'
        elif posIn == 8:
            if player1type == 'x':
                if turn == 1:
                    eightOut = 'x'
                else:
                    eightOut = 'o'
            else:
                if turn == 1:
                    eightOut = 'o'
                else:
                    eightOut = 'x'
        elif posIn == 9:
            if player1type == 'x':
                if turn == 1:
                    nineOut = 'x'
                else:
                    nineOut = 'o'
            else:
                if turn == 1:
                    nineOut = 'o'
                else:
                    nineOut = 'x'
        
        if turn == 1:
            turn = 2
        else:
            turn = 1
        turnNum += 1
        clear()
        screen(oneOut,twoOut,threeOut,fourOut,fiveOut,sixOut,sevenOut,eightOut,nineOut)
        
    
    
    clear()
    screen(oneOut,twoOut,threeOut,fourOut,fiveOut,sixOut,sevenOut,eightOut,nineOut)       
    if winner == 0:
        print("--------------------------------\nit was a tie. there were no winners.\n--------------------------------\n")
    else:
        print(f"--------------------------------\nPlayer {winner} has won!\n--------------------------------\n")
    
    #again?
    again = input("do you want another game? y/n ")
    if again.lower() != 'n' and again.lower() != 'y':
        print("you didn't input y/n")
        break
    elif again.lower() == 'n':
        break

input("press enter to exit")