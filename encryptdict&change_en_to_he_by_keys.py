# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:10:42 2020

@author: IEUser
"""
import base64
from Crypto.Cipher import AES

secret_key = b'1234567890123456'
cipher = AES.new(secret_key,AES.MODE_ECB)
def hebrew_english_by_keyboard(text,engToHebTrueFalse):
    out = ""
    if engToHebTrueFalse:
        for x in text:
            if x == "a":
                out = out + "ש"
            elif x == "b":
                out = out + "נ"
            elif x == "c":
                out = out + "ב"
            elif x == "d":
                out = out + "ג"
            elif x == "e":
                out = out + "ק"
            elif x == "f":
                out = out + "כ"
            elif x == "g":
                out = out + "ע"
            elif x == "h":
                out = out + "י"
            elif x == "i":
                out = out + "ן"
            elif x == "j":
                out = out + "ח"
            elif x == "k":
                out = out + "ל"
            elif x == "l":
                out = out + "ך"
            elif x == "m":
                out = out + "צ"
            elif x == "n":
                out = out + "מ"
            elif x == "o":
                out = out + "ם"
            elif x == "p":
                out = out + "פ"
            elif x == "q":
                out = out + "/"
            elif x == "r":
                out = out + "ר"
            elif x == "s":
                out = out + "ד"
            elif x == "t":
                out = out + "א"
            elif x == "u":
                out = out + "ו"
            elif x == "v":
                out = out + "ה"
            elif x == "w":
                out = out + "'"
            elif x == "x":
                out = out + "ס"
            elif x == "y":
                out = out + "ט"
            elif x == "z":
                out = out + "ז"
            elif x == ",":
                out = out + "ת"
            else:
                out = out + x
    else:    
        for x in text:
            if x == "א":
                out = out + "t"
            elif x == "ב":
                out = out + "c"
            elif x == "ג":
                out = out + "d"
            elif x == "ד":
                out = out + "s"
            elif x == "ה":
                out = out + "v"
            elif x == "ו":
                out = out + "u"
            elif x == "ז":
                out = out + "z"
            elif x == "ח":
                out = out + "j"
            elif x == "ט":
                out = out + "y"
            elif x == "י":
                out = out + "h"
            elif x == "כ":
                out = out + "f"
            elif x == "ל":
                out = out + "k"
            elif x == "מ":
                out = out + "n"
            elif x == "נ":
                out = out + "b"
            elif x == "ס":
                out = out + "x"
            elif x == "ע":
                out = out + "g"
            elif x == "פ":
                out = out + "p"
            elif x == "צ":
                out = out + "m"
            elif x == "ק":
                out = out + "e"
            elif x == "ר":
                out = out + "r"
            elif x == "ש":
                out = out + "a"
            elif x == "ת":
                out = out + ","
            else:
                out = out + x
    return out
        
        
        
def encode(msg_text):
    msg_text = msg_text.rjust(len(msg_text)*16)
    encoded = base64.b64encode(cipher.encrypt(msg_text))
    return encoded

x = {"5+5 = " : "10" ,"9+2 = ": "11"}

p = input("is it in english(y) or hebrew(n)? y/n ")
if p == "y":
    for z in x:
        x[z] = encode(x[z])

elif p == "n":
    for z in x:
        x[z] = encode(hebrew_english_by_keyboard(x[z],False))

print(x)