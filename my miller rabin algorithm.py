#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:41:43 2020

@author: y3
"""

import random
import time

def my_miller_rabin(n,k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a,d,n)
        if x == 1 or x == n-1:
            continue
        for __ in range(r-1):
            x = pow(x,2,n)
        if x == n-1:
            continue
        return False
    return True





x = int(input("what num "))
a = time.time()
print(my_miller_rabin(x,40))
b = time.time()
print(f"time = {b-a}")