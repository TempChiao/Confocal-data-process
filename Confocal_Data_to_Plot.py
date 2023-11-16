#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:22:42 2023

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

file_path = '/Users/tempchiao/UofE/RA/EVAN/Linear/'
root = '2.083pM'
file_number = 5
thresholdA = -1
thresholdB = 10
dataA = []
dataB = []
for i in range(1,file_number+1):
    
    if i == 1:
        path = file_path + root
        m,n = get(path)
        for p in m:
            if p > thresholdA:
                dataA.append(p)
        for q in n:
            if q > thresholdB:
                dataB.append(q)
        
    if i > 1:
        if i < 10:
            path = file_path + root + '_0' + str(i)
            m,n = get(path)
            for p in m:
                if p > thresholdA:
                    dataA.append(p)
            for q in n:
                if q > thresholdB:
                    dataB.append(q)
   
    if i > 9:
        path = file_path + root + '_' + str(i)
        m,n = get(path)
        for p in m:
            if p > thresholdA:
                dataA.append(p)
        for q in n:
            if q > thresholdB:
                dataB.append(q) 
length = len(dataB)
count = []
for i in range(1,int(length)+1):
    count.append(i)
# plt.plot(count,dataB)
def genehis(data,path1,path2):
    binwidth = 1
    plt.hist(data, bins=range(min(data), max(data) + binwidth, binwidth))
    
    plt.xlabel('Intensity')
    plt.ylabel('Counts')
    plt.savefig('{}{}_his.png'.format(path1, path2))  

# genehis(dataB,file_path,root)
print(length)

def genesimu(datax,datay,path1,path2):
    plt.figure(figsize=(30,3))
    plt.plot(datax,datay)

    plt.ylim(min(datay),100)
    plt.ylabel('Intensity')
    plt.xlabel('ms')
    plt.savefig('{}{}_sim.png'.format(path1, path2))
    

# genesimu(count,dataB,file_path,root)
