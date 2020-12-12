#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:32:11 2020

@author: y3
"""

import datetime
from rsa_encryption import *
import requests
import struct
from os import listdir
from os.path import isfile, join
import json



n = 4680769976151176270880385373311349011331186144201672419960137781171339129718812111700234283960145321154280168787073591493248646286305217996114605642677939
e = 936153995230235254176077074662269802266237228840334483992027556234267825943734992984626796837492745159599740235908873586071342476662733099244449201144125
d = 5

def getItems(resourcePackPath):
    resourcePackPath = resourcePackPath + "/assets/minecraft/textures/item"
    items = [f for f in listdir(resourcePackPath) if isfile(join(resourcePackPath, f))]
    outItems = []
    for x in range(len(items)):
        items[x] = items[x][:-4]
    
    for x in items:
        if x[:5] != "clock" and x[:7] != "compass" and x[:len("empty_armor_slot")] != "empty_armor_slot" and x[:len("bow_pulling")] != "bow_pulling":
            outItems.append(x)
    return outItems

def Command(userName = "blub",itemName = "diamond_sword",enchants = [("sharpness",5)],number = 1):
    command = f"/give {userName} {itemName}" + "{Enchantments:["
    
    for enchant,lvl in enchants:
        command = command + f"(id:\"{enchant}\",lvl:{lvl}),"
    command = command[:-1]
    command = command + "]} " + str(number)
    return command

def addToUserMonthlyCounter(name):
    
    
    timesLost = 0
    with open("timesLostItemsCounter.txt" ,mode = "r") as f:
        text = decryptText(f.read(), n, d)
    
    with open("timesLostItemsCounter.txt" ,mode = "w") as f:
        dt = datetime.datetime.today()
        month = dt.month
        oldMonth = int(text.split("\n")[0])
        if month != int(oldMonth):
            f.write(str(month)+"\n"+str(name)+":1")
            joined = str(month)+"\n"+str(name)+":1"
            timesLost = 1
        else:
            data = text.split("\n")
            counter = 0
            for x in data:
                y = x.split(":")
                if name == y[0]:
                    data[counter] = name+":"+str(int(y[1])+1)
                    timesLost = int(y[1])+1
                    joined = "\n".join(data)
                    f.write(joined)
                    break
                counter += 1
            if name != y[0]:
                data.append(name+":1")
                joined = "\n".join(data)
                f.write(joined)
                timesLost = 1
                
    #encrypt
    with open("timesLostItemsCounter.txt" ,mode = "w") as f:
        crypt = encryptText(joined, n, e)
        f.write(crypt)
        
def CheckUserMonthlyCounter(name):
    with open("timesLostItemsCounter.txt" ,mode = "r") as f:
        text = decryptText(f.read(), n, d)
    for x in text.split("\n"):
        y = x.split(":")
        if y[0] == name:
            return int(y[1])


allItems = getItems("/home/y3/.minecraft/resourcepacks/template")

def findWord(word):
    with open("dataFiles/wordsToItems.json", mode = "r") as f:
        file = json.loads(f.read())
    try:
        file[word]
    except:
        return False
    else:
        return file[word]

def parseMessage(message):
    """
    output syntax
    --------------
    item = (itemName, damage, [(enchant, level),(enchant, level)], count)
    """
    words = message.split()
    count = 0
    itemName = ""
    damage = 0
    enchantments = []
    for x in words:
        if x.isnumeric():
            count = None
    

def understandMessages(program,messages):
    '''

    Parameters
    ----------
    program :
        #whatsapp
        #raw
    message :
        message

    Returns
    -------
    out : list
        [list of commands in list syntax,list of unknowns]

    '''
    out = []
    strings = message.split("\n")
    if program == "whatsapp":
        for x in range(len(strings)):
            if strings[x].find("[") != -1:
                w = strings[x].find("]")
                strings[x] = strings[x][w+2:]
        for x in range(len(strings)):
            w = strings[x].find(":")
            strings[x] = strings[x][w+2:]
    