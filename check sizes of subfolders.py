#!/usr/bin/env python3# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 20:04:03 2020

@author: y4
"""

import os
import subprocess

def sizeof_fmt(num, suffix='B'):
    for unit in [' ',' K',' M',' G',' T',' P',' E',' Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total


def get_directory_size(directory):
    return int(subprocess.getoutput("du -sb "+directory).split("\n")[-1].split("/")[0][:-1])


exclude = ['var', 'usr', 'sys', 'snap', 'proc', 'dev', 'home', 'media']
exclude = ['media','proc','home','tmp']

sizes = {"snap":617900000,"sys":915600000,"usr":7500000000}
originalPath = input("path: ")
paths = os.listdir(originalPath)
for x in paths:
    if not(x in exclude):
        sizes[x] = get_directory_size(originalPath+x)
        print("scaned ",x)

print("\n\n")

for x in sizes:
    print(x," : ",sizeof_fmt(sizes[x]))

print(sizeof_fmt(sum(sizes.values())))