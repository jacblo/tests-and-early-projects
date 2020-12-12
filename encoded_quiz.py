"""
Created on Sun May 10 18:38:54 2020

@author: IEUser
"""
import base64
from Crypto.Cipher import AES


x = {'5+5 = ': b'gUhd9TxpnQppnZVAf7cv9kdIpvEwCkwAog+GUZDCFP0=', '9+2 = ': b'gUhd9TxpnQppnZVAf7cv9ldWuji3s/46QUkIWGSmDhA='}


secret_key = b'1234567890123456'
cipher = AES.new(secret_key,AES.MODE_ECB)
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

points = 0

print("חידון מיינקראפט\n\n")
counter = 0
points_per_q = 100/len(x)
for z in x:
    counter += 1
    print(f"שאלה מספר {counter}")
    print(z)
    w = input("תשובה - ")
    if w == decode(x[z]):
        print(f"תשובה נכונה קיבלת {round(points_per_q,3)} נקודות")
        points += points_per_q
    else:
        print("תשובה לא נכונה...")
print("\n\nניקוד\nקיבלת {points} נקודות מתוך מאה")
input("לחץ אנתר לסיום התוכנה")