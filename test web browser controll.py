#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:00:26 2020

@author: y4
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from rsa_encryption import *
import json
import time

with open('rsa.json',mode='r') as f:
    keys = json.load(f)
with open('aternos Pass encrypted',mode='r') as f:
    passwordVal = decryptText(f.read(),keys[0][0],keys[0][1])

ff = webdriver.Chrome()
ff.get("https://aternos.org/go")
name = ff.find_elements_by_xpath('/html/body/div[3]/div/div/div[4]/div[3]/div[1]/div[2]/input')[0]
name.send_keys('KiwiMan19th')
password = ff.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/div[3]/div[2]/div[2]/input')
password.send_keys(passwordVal)
submit = ff.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/div[3]/div[4]/i')
submit.click()
element = WebDriverWait(ff, 10).until(
    lambda x: x.find_element_by_xpath("/html/body/div/main/section/div/div[2]/div[1]/div[1]/div[1]/div[2]"))
ServerSelect = ff.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div[1]/div[1]/div[1]/div[2]')
ServerSelect.click()
time.sleep(1)
ff.get('https://aternos.org/console/')

commandLine = ff.find_element_by_xpath('/html/body/div[2]/main/section/div[3]/div/div[3]/input')
for x in range(528):
    commandLine.send_keys('time set 0\n')
    time.sleep(60)