#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:47:26 2020

@author: y4
"""

url = 'https://sounddrout.com/banappeal'
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from screenshotAndKeypressTests import *
import numpy as np 
import pytesseract
import time
import datetime
from selenium import *
import cv2
import os
import string
import random

def genarateRandString(length):
    out = ""
    for x in range(length):
        out += random.choice(string.ascii_letters)
    return out
ff = webdriver.Firefox()
for x in range(541):
    print("has done ",x," times")
    time.sleep(0.1)
    ff.get(url)
    while True:
        try:
            ff.find_element_by_xpath("/html/body/section[3]/section/div/div/div/div/button").click()
        except:
            pass
        else:
            break
    ff.find_element_by_xpath("/html/body/div[4]/div[5]/div[1]/a/div").click()
    ff.find_element_by_xpath("/html/body/div[4]/form/table/tbody[1]/tr[2]/td/label/input").send_keys("bot"+genarateRandString(10)+"@gmail.com")
    ff.find_element_by_xpath("/html/body/div[4]/form/table/tbody[1]/tr[3]/td/label/input").send_keys("thisNeedsToBeDifferent"+genarateRandString(10)+"#"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
    ff.find_element_by_xpath("/html/body/div[4]/form/table/tbody[2]/tr[2]/td/span/span[1]/span/span[1]").click()
    ff.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[2]").click()
    time.sleep(0.2)
    ff.find_element_by_xpath("/html/body/div[4]/form/table/tbody[3]/tr[2]/td/div[1]/div[2]").send_keys("make your captcha better because it isn't even distorted so grayscale it and any computer can read it and so that this is not deleted i will add random string "+genarateRandString(20))
    ff.find_element_by_xpath('/html/body/div[4]/form/table/tbody[3]/tr[5]/td/label/input').send_keys(datetime.datetime.now().strftime("%Y/%m/%d"))
    ff.find_elements_by_xpath("/html/body/div[11]/div[4]/button[2]")[0].click()
    ff.find_elements_by_xpath("/html/body/div[4]/form/table/tbody[3]/tr[6]/td/label/label/input")[0].click()
    captcha = ff.find_elements_by_xpath("/html/body/div[4]/form/table/tbody[4]/tr[2]/td/div[1]/span/img")[0]
    captcha.screenshot("captcha.png")
    img = cv2.imread("captcha.png")
    text = pytesseract.image_to_string(img)[:-1]
    ff.find_element_by_xpath("/html/body/div[4]/form/table/tbody[4]/tr[2]/td/div[2]/input").send_keys(text)
    ff.find_element_by_xpath("/html/body/div[4]/form/p/input[1]").click()

    while True:
        try:
            ff.find_element_by_xpath('//*[@id="msg_notice"]')
        except:
            captcha = ff.find_elements_by_xpath("/html/body/div[4]/form/table/tbody[4]/tr[2]/td/div[1]/span/img")[0]
            captcha.screenshot("captcha.png")
            img = cv2.imread("captcha.png")
            text = pytesseract.image_to_string(img)[:-1]
            ff.find_element_by_xpath("/html/body/div[4]/form/table/tbody[4]/tr[2]/td/div[2]/input").send_keys(text)
            ff.find_element_by_xpath("/html/body/div[4]/form/p/input[1]").click()
        else:
            break

os.system('notify-send "done" "done"')