# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:38:20 2020

@author: IEUser
"""
import base64
from Crypto.Cipher import AES

secret_key = b'1234567890123456'
cipher = AES.new(secret_key,AES.MODE_ECB)
def encode(msg_text):
    msg_text = msg_text.rjust(len(msg_text)*16)
    encoded = base64.b64encode(cipher.encrypt(msg_text))
    return encoded

def decode(code):
    decoded = cipher.decrypt(base64.b64decode(code))
    decoded = str(decoded)
    x = int(len(decoded)/16)
    decoded = decoded[x:-1]
    decoded2 = ""
    z = 0
    for x in decoded:
        if x != " ":
            break
        z += 1
    decoded2 = decoded[z:]
    return decoded2
