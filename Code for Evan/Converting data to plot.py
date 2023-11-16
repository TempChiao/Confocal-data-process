#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:22:13 2023

@author: tempchiao
"""

import matplotlib.pyplot as plt

import pandas as pd

def aveB(path):
    Sum = 0
    count = 0
    readData = pd.read_csv(path, header = None, sep = '\\t', engine='python')
    a = readData[1]
    for i in a:
        Sum = Sum + i
        count = count + 1
    return Sum/count

def get(path):
    geta = []
    getb = []
    readData = pd.read_csv(path, header = None, sep = '\\t', engine='python')
    a = readData[0]
    b = readData[1]
    for i in a:
        geta.append(i)
    for i in b:
        getb.append(i)
    return geta, getb

file_path = '//Volumes/Tianxiao/Calibration/Meg_beads/270/'
root = '1in1000'
file_number = 10
signalB = 0
dataA = []
dataB = []
for i in range(1,file_number+1):
    
    if i == 1:
        path = file_path + root
        m,n = get(path)
        for p in m:
            dataA.append(p)
        for q in n:
            dataB.append(q)
        
    if i > 1:
        if i < 10:
            path = file_path + root + '_0' + str(i)
            m,n = get(path)
            for p in m:
                dataA.append(p)
            for q in n:
                dataB.append(q)
   
    if i > 9:
        path = file_path + root + '_' + str(i)
        m,n = get(path)
        for p in m:
            dataA.append(p)
        for q in n:
            dataB.append(q)
length = len(dataB)
count = []
for i in range(1,int(length)+1):
    count.append(i)
plt.plot(count,dataB)
# print (dataB)