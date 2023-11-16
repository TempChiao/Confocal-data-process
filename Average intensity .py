#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:48:26 2023

@author: tempchiao
"""

import csv
import pandas as pd

# file_path = ''
# root = ''
# file_number = 
# for i in range(file_number):
#     if i == 0:
#         file = file_pathe + root
#         csvreader = csv.read(file)
# readData = pd.read_csv("/Users/tempchiao/UofE/TEST/Test_270_Unbind/1in100000",header= None ,sep='\\t')
# a = readData[1]
# for i in a:
#     print(i)
def aveB(path):
    Sum = 0
    count = 0
    readData = pd.read_csv(path, header = None, sep = '\\t', engine='python')
    a = readData[1]
    for i in a:
        Sum = Sum + i
        count = count + 1
    return Sum/count


file_path = '/Volumes/Tianxiao/Calibration/'
root = '10nM'
file_number = 10
signalB = 0
for i in range(1,file_number+1):
    
    if i == 1:
        path = file_path + root
        signalB += aveB(path)
        
    if i > 1:
        if i < 10:
            path = file_path + root + '_0' + str(i)
            signalB += aveB(path)
   
    if i > 9:
        path = file_path + root + '_' + str(i)
        signalB += aveB(path)

print('The average intensity in Channel B is {}'.format(signalB/file_number))


    


