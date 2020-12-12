from subprocess import Popen, PIPE
import pyscreenshot
import PIL
import time
import pyautogui

def keymap(keys):
    keys = keys.split("+")
    out = "" 
    for x in keys[:-1]:
        out = out + "keydown " + x + "\n"
    out = out + "key " + keys[-1] + "\n"
    for x in keys[:-1:]:
        out = out + "keyup " + x + " \n"
    out = out[:-1]
    return bytes(out,"utf-8")

def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)

def mouseClick(button = 1,pos = (None,None)):
    p = Popen(['xte'], stdin=PIPE)
    if pos != (None,None):
        p.communicate(input=bytes("mousemove "+str(pos[0])+" "+str(pos[1]*10),"utf-8"))
    p.kill()
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=bytes("mouseclick "+str(button)+" ","utf-8"))
    
def mouseMove(ToPos = (0,0),timer = 0,samples = 10):
    if timer == 0:
        p = Popen(['xte'], stdin=PIPE)
        p.communicate(input=bytes("mousemove "+str(ToPos[0])+" "+str(ToPos[1]),"utf-8"))
        return None
    for x in range(1,timer*samples):
        start = time.time()
        mousePos=pyautogui.position()
        p = Popen(['xte'], stdin=PIPE)
        nextPos = [int(mousePos[0]),int(mousePos[0])]
        p.communicate(input=bytes("mousemove "+str(nextPos[0])+" "+str(nextPos[1]),"utf-8"))
        print(nextPos)
        time.sleep((1/samples)-(time.time()-start))
       

#keypress (keymap("Control_L+S"))
#im=pyscreenshot.grab(bbox=(10,10,500,500))

#mouseMove((100,100),1 , 10)