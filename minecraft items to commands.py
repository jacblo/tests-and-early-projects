#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:38:57 2020

@author: y3
"""
import datetime
import sys
from rsa_encryption import *

n = 4680769976151176270880385373311349011331186144201672419960137781171339129718812111700234283960145321154280168787073591493248646286305217996114605642677939
e = 936153995230235254176077074662269802266237228840334483992027556234267825943734992984626796837492745159599740235908873586071342476662733099244449201144125
d = 5


name = input("username: ")
commandBase = f"/give {name} "


timesLost = 0
with open("timesLostItemsCounter.txt" ,mode = "r") as f:
    text = decryptText(f.read(), n, d)
    data = text.split("\n")
    dt = datetime.datetime.today()
    month = dt.month
    oldMonth = int(text.split("\n")[0])
    if month != int(oldMonth):
        timesLost = 1
    
    else:
        counter = 0
        for x in data:
            y = x.split(":")
            if name == y[0]:
                data[counter] = name+":"+str(int(y[1])+1)
                timesLost = int(y[1])+1
                break
            counter += 1
        if name != y[0]:
            data.append(name+":1")
            timesLost = 1

if timesLost > 3:
    print("already lost 3 times")
    sys.exit()



print("\nitems\n-------------")
items = []
while True:
    item = input("item: ")
    if item[0:10].lower() != "minecraft:":
        item = "minecraft:" + item
    
    count = input("count: ")
    if count == "":
        count = 1
    else:
        count = int(count)
    
    #enchantments
    EnchantsExist = input("enchanments? (Enter for no or y for yes) ")
    enchants = []
    if EnchantsExist.lower() == "y" or EnchantsExist.lower() == "yes":
        while True:
            enchant = input("enchant: ")
            if enchant[0:10].lower() != "minecraft:":
                enchant = "minecraft:" + enchant
            
            level = input("level: ")
            if level == "":
                level = 1
            else:
                level = int(level)
            
            enchants.append((enchant,level))
            
            more = input("another enchantment? (Enter for yes or n for no) ")
            if more.lower() == "n" or more.lower() == "no":
                break
    
    damage = input("Damage: ")
    if damage == "":
        damage = 0
    else:
        damage = int(damage)
    
    items.append((item,damage,enchants,count))
    
    
    more = input("another item? (Enter for yes or n for no) ")
    if more.lower() == "n" or more.lower() == "no":
        break
print("\nout\n-----")
commands = []
for x in items:
    if x[2] == []:
        command = commandBase + x[0] + "{Damage:" + str(x[1]) + "} " + str(x[3])
    else:
        command = commandBase + x[0] + "{Damage:" + str(x[1]) + ",Enchantments:["
        
        for z in x[2]:
            command = command + "{id:\""  + z[0] + "\",lvl:"  + str(z[1]) +  "},"
        
        command = command[0:-1] + "]} " + str(x[3])
        
    commands.append(command)

for x in commands:
    print(x)

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