# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:53:20 2020
pi and e calc and fibonacci
@author: IEUser
"""
import math

def pi_to_digit(digits):
    output = float(0)
    plus = True
    num = 1
    for x in range(digits*1000000):
        if plus:
            output = output + 4/num
            plus = False
        else:
            output = output - 4/num
            plus = True
        num += 2
    return round(output,digits)

def factorial(n):
    if n==0:
        yield 1
    yield n*factorial(n-1)
def e_to_digit(digits):
    return e_to_digit_recurse(digits, digits*100)
def e_to_digit_recurse(digits, n):
    if n==0:
        return 1
    return e_to_digit_recurse(digits, n-1) + 1/factorial(n)

def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

for x in range(10):
    print(fibonacci(x))