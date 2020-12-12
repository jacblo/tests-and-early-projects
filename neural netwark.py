#!/usr/bIn/env python3
# -*- codIng: utf-8 -*-
"""
Created on Sun May 31 21:43:47 2020

@author: y3
""" 
"""

old
--------------

in1           out1
     hidden1 
in2           out2
     hidden2 
in3           out3


weightToChange
0/1 - in1 1
2 - in1 2
3 - in2 1
4 - in2 2
5 - in3 1
6 - in3 2

7 - hid1 1
8 - hid1 2
9 - hid1 3
10 - hid2 1
11 - hid2 2
12 - hid2 3
"""
"""
new system
-----------
one hidden layer

in1                 out1
        hidden1
in2                 out2
        hidden2
in3                 out3
        hiddenx
inx                 outx


tasks
-------
v - list of inputs biases and weights       - [[biases,hidden1,hidden2],[weights,hidden1,hidden2]] - inVals
v - list of hidden layer biases and weights - [[biases,out1,out2],[weights,out1,out2]] - hidVals
v - list of weights for inputs and hidden layers
v - input of how many outputs and how many inputs
output func

update func
------------
    learn how to learn
    

"""


import random
import time

class learningBad:
    """
    this is a basic neural netwark with 3 inputs 3 outputs and 1 hidden layer
    """
    bestScore = 0
    def __init__(self):
        self.In1 = 0
        self.In2 = 0
        self.In3 = 0

        
        #weights range
        self.in1weightsRange = [[0,10],[0,10]]
        self.in2weightsRange = [[0,10],[0,10]]
        self.in3weightsRange = [[0,10],[0,10]]
        
        self.hidden1weightsRange = [[0,10],[0,10],[0,10]]
        self.hidden2weightsRange = [[0,10],[0,10],[0,10]]
        
        self.weightToChange = None
        
        #weights
        self.in1weights = [random.randrange(self.in1weightsRange[0][0],self.in1weightsRange[0][1]),random.randrange(self.in1weightsRange[1][0],self.in1weightsRange[1][1])]
        self.in2weights = [random.randrange(self.in2weightsRange[0][0],self.in2weightsRange[0][1]),random.randrange(self.in2weightsRange[1][0],self.in1weightsRange[1][1])]
        self.in3weights = [random.randrange(self.in3weightsRange[0][0],self.in3weightsRange[0][1]),random.randrange(self.in3weightsRange[1][0],self.in3weightsRange[1][1])]
                
        self.hidden1weights = [random.randrange(self.hidden1weightsRange[0][0],self.hidden1weightsRange[0][1]),random.randrange(self.hidden1weightsRange[1][0],self.hidden1weightsRange[1][1]),random.randrange(self.hidden1weightsRange[2][0],self.hidden1weightsRange[2][1])]
        self.hidden2weights = [random.randrange(self.hidden2weightsRange[0][0],self.hidden2weightsRange[0][1]),random.randrange(self.hidden2weightsRange[1][0],self.hidden2weightsRange[1][1]),random.randrange(self.hidden2weightsRange[2][0],self.hidden2weightsRange[2][1])]
        
        
    
    def update(self,In1,In2,In3,score):
        self.In1 = In1
        self.In2 = In2
        self.In3 = In3
        [1,1]
        #calculate weights and ranges
        if self.weightToChange == None:
            self.weightToChange = 0
            return
        
        #0 needs to be here so you dont think you did well out of nowhere
        if self.weightToChange == 0:
            self.bestScore = score
            self.weightToChange += 1            
            self.in1weights = [random.randrange(self.in1weightsRange[0][0],self.in1weightsRange[0][1]),random.randrange(self.in1weightsRange[1][0],self.in1weightsRange[1][1])]
        
        
        
        if self.weightToChange == 1:
            if score > self.bestScore:
                self.bestScore = score
                self.in1weightsRange[0][0] = self.in1weights[0] - round((self.in1weightsRange[0][0] - self.in1weightsRange[0][1]-2)/2)
                self.in1weightsRange[0][1] = self.in1weights[0] + round((self.in1weightsRange[0][0] - self.in1weightsRange[0][1]-2)/2)
            else:
                self.weightToChange += 1
            self.in1weights = [random.randrange(self.in1weightsRange[0][0],self.in1weightsRange[0][1]),random.randrange(self.in1weightsRange[1][0],self.in1weightsRange[1][1])]
            
        if self.weightToChange == 2:
            if score > self.bestScore:
                self.bestScore = score
                self.in1weightsRange[1][0] = self.in1weights[1] - round((self.in1weightsRange[1][0] - self.in1weightsRange[1][1]-2)/2)
                self.in1weightsRange[1][1] = self.in1weights[1] + round((self.in1weightsRange[1][0] - self.in1weightsRange[1][1]-2)/2)
            else:
                self.weightToChange += 1
            self.in1weights = [random.randrange(self.in1weightsRange[0][0],self.in1weightsRange[0][1]),random.randrange(self.in1weightsRange[1][0],self.in1weightsRange[1][1])]
        
        if self.weightToChange == 3:
            if score > self.bestScore:
                self.bestScore = score
                self.in2weightsRange[0][0] = self.in2weights[0] - round((self.in2weightsRange[0][0] - self.in2weightsRange[0][1]-2)/2)
                self.in2weightsRange[0][1] = self.in2weights[0] + round((self.in2weightsRange[0][0] - self.in2weightsRange[0][1]-2)/2)
            else:
                self.weightToChange += 1
            self.in2weights = [random.randrange(self.in2weightsRange[0][0],self.in2weightsRange[0][1]),random.randrange(self.in2weightsRange[1][0],self.in2weightsRange[1][1])]
        
        if self.weightToChange == 4:
            if score > self.bestScore:
                self.bestScore = score
                self.in2weightsRange[1][0] = self.in2weights[1] - round((self.in2weightsRange[1][0] - self.in2weightsRange[1][1]-2)/2)
                self.in2weightsRange[1][1] = self.in2weights[1] + round((self.in2weightsRange[1][0] - self.in2weightsRange[1][1]-2)/2)
            else:
                self.weightToChange += 1
            self.in2weights = [random.randrange(self.in2weightsRange[0][0],self.in2weightsRange[0][1]),random.randrange(self.in2weightsRange[1][0],self.in2weightsRange[1][1])]
    
        if self.weightToChange == 5:
            if score > self.bestScore:
                self.bestScore = score
                self.in3weightsRange[0][0] = self.in3weights[0] - round((self.in3weightsRange[0][0] - self.in3weightsRange[0][1]-2)/2)
                self.in3weightsRange[0][1] = self.in3weights[0] + round((self.in3weightsRange[0][0] - self.in3weightsRange[0][1]-2)/2)
            else:
                self.weightToChange += 1
            self.in3weights = [random.randrange(self.in3weightsRange[0][0],self.in3weightsRange[0][1]),random.randrange(self.in3weightsRange[1][0],self.in3weightsRange[1][1])]

        if self.weightToChange == 6:
            if score > self.bestScore:
                self.bestScore = score
                self.in3weightsRange[1][0] = self.in3weights[1] - round((self.in3weightsRange[1][0] - self.in3weightsRange[1][1]-2)/2)
                self.in3weightsRange[1][1] = self.in3weights[1] + round((self.in3weightsRange[1][0] - self.in3weightsRange[1][1]-2)/2)
            else:
                self.weightToChange += 1
            self.in3weights = [random.randrange(self.in3weightsRange[0][0],self.in3weightsRange[0][1]),random.randrange(self.in3weightsRange[1][0],self.in3weightsRange[1][1])]

    
        
        if self.weightToChange == 7:
            if score > self.bestScore:
                self.bestScore = score
                self.hidden1weightsRange[0][0] = self.hidden1weights[0] - round((self.hidden1weightsRange[0][0] - self.hidden1weightsRange[0][1]-2)/2)
                self.hidden1weightsRange[0][1] = self.hidden1weights[0] + round((self.hidden1weightsRange[0][0] - self.hidden1weightsRange[0][1]-2)/2)
            else:
                self.weightToChange += 1
            self.hidden1weights = [random.randrange(self.hidden1weightsRange[0][0],self.hidden1weightsRange[0][1]),random.randrange(self.hidden1weightsRange[1][0],self.hidden1weightsRange[1][1]),random.randrange(self.hidden1weightsRange[2][0],self.hidden1weightsRange[2][1])]
        
        if self.weightToChange == 8:
            if score > self.bestScore:
                self.bestScore = score
                self.hidden1weightsRange[1][0] = self.hidden1weights[1] - round((self.hidden1weightsRange[1][0] - self.hidden1weightsRange[1][1]-2)/2)
                self.hidden1weightsRange[1][1] = self.hidden1weights[1] + round((self.hidden1weightsRange[1][0] - self.hidden1weightsRange[1][1]-2)/2)
            else:
                self.weightToChange += 1
            self.hidden1weights = [random.randrange(self.hidden1weightsRange[0][0],self.hidden1weightsRange[0][1]),random.randrange(self.hidden1weightsRange[1][0],self.hidden1weightsRange[1][1]),random.randrange(self.hidden1weightsRange[2][0],self.hidden1weightsRange[2][1])]

        if self.weightToChange == 9:
            if score > self.bestScore:
                self.bestScore = score
                self.hidden1weightsRange[2][0] = self.hidden1weights[2] - round((self.hidden1weightsRange[2][0] - self.hidden1weightsRange[2][1]-2)/2)
                self.hidden1weightsRange[2][1] = self.hidden1weights[1] + round((self.hidden1weightsRange[2][0] - self.hidden1weightsRange[2][1]-2)/2)
            else:
                self.weightToChange += 1
            self.hidden1weights = [random.randrange(self.hidden1weightsRange[0][0],self.hidden1weightsRange[0][1]),random.randrange(self.hidden1weightsRange[1][0],self.hidden1weightsRange[1][1]),random.randrange(self.hidden1weightsRange[2][0],self.hidden1weightsRange[2][1])]

        if self.weightToChange == 10:
            if score > self.bestScore:
                self.bestScore = score
                self.hidden2weightsRange[0][0] = self.hidden2weights[0] - round((self.hidden2weightsRange[0][0] - self.hidden2weightsRange[0][1]-2)/2)
                self.hidden2weightsRange[0][1] = self.hidden2weights[0] + round((self.hidden2weightsRange[0][0] - self.hidden2weightsRange[0][1]-2)/2)
            else:
                self.weightToChange += 1
            self.hidden2weights = [random.randrange(self.hidden2weightsRange[0][0],self.hidden2weightsRange[0][1]),random.randrange(self.hidden2weightsRange[1][0],self.hidden2weightsRange[1][1]),random.randrange(self.hidden2weightsRange[2][0],self.hidden2weightsRange[2][1])]
        
        if self.weightToChange == 11:
            if score > self.bestScore:
                self.bestScore = score
                self.hidden2weightsRange[1][0] = self.hidden2weights[1] - round((self.hidden2weightsRange[1][0] - self.hidden2weightsRange[1][1]-2)/2)
                self.hidden2weightsRange[1][1] = self.hidden2weights[1] + round((self.hidden2weightsRange[1][0] - self.hidden2weightsRange[1][1]-2)/2)
            else:
                self.weightToChange += 1
            self.hidden2weights = [random.randrange(self.hidden2weightsRange[0][0],self.hidden2weightsRange[0][1]),random.randrange(self.hidden2weightsRange[1][0],self.hidden2weightsRange[1][1]),random.randrange(self.hidden2weightsRange[2][0],self.hidden2weightsRange[2][1])]

        if self.weightToChange == 12:
            if score > self.bestScore:
                self.bestScore = score
                self.hidden2weightsRange[2][0] = self.hidden2weights[2] - round((self.hidden2weightsRange[2][0] - self.hidden2weightsRange[2][1]-2)/2)
                self.hidden2weightsRange[2][1] = self.hidden2weights[1] + round((self.hidden2weightsRange[2][0] - self.hidden2weightsRange[2][1]-2)/2)
            else:
                self.weightToChange += 1
            self.hidden2weights = [random.randrange(self.hidden2weightsRange[0][0],self.hidden2weightsRange[0][1]),random.randrange(self.hidden2weightsRange[1][0],self.hidden2weightsRange[1][1]),random.randrange(self.hidden2weightsRange[2][0],self.hidden2weightsRange[2][1])]
        
    
    
    
    def output(self):
        hidden1 = self.In1 * self.in1weights[0] + self.In2 * self.in2weights[0] + self.In3 * self.in3weights[0]
        hidden2 = self.In1 * self.in1weights[1] + self.In2 * self.in2weights[1] + self.In3 * self.in3weights[1]
        
        out1 = hidden1 * self.hidden1weights[0] + hidden2 * self.hidden2weights[0]
        out2 = hidden1 * self.hidden1weights[1] + hidden2 * self.hidden2weights[1]
        out3 = hidden1 * self.hidden1weights[2] + hidden2 * self.hidden2weights[2]
        
        return [out1,out2,out3]
    


class learning:
    def __init__(self,inNum,outNum):
        self.inNum = inNum
        self.outNum = outNum
        
        self.inVals = [[],[]]
        for x in range(inNum):
            self.inVals[0].append(1)
            self.inVals[1].append(1)
            
        self.hidVals = [[],[]]
        for x in range(inNum):
            self.hidVals[0].append(1)
            self.hidVals[1].append(1)
        
        
        
    def update(self):
        pass
    
    def output(self):
        pass

"""
test = learning()
score = 0
while True:
    test.update(10,10,10,score)
    x = test.output()
    print(x)
    time.sleep(0.01)
    score = 100 - abs(100 - x[0])
    if x == 100:
        print("success! we got to 100!")
        break
"""