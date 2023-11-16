#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:47:35 2023

@author: evanbaerg
"""

import pandas as pd
import matplotlib.pyplot as plt #importing matplotlib


def appenddata(data, path):
    readData = pd.read_csv(path, header = None, sep = '\\t', engine='python')
    return data + readData.iloc[:,1].values.tolist()

file_path = '/Users/evanbaerg/Desktop/Edinburgh/Studies/Edinburgh Research/Confocal Data/Calibration/'
root = '10nM'
file_number = 5

# add data into a list
data = []
for i in range(1,file_number+1):
    
    if i == 1:
        path = file_path + root
        data = appenddata(data, path)
        print(data)
        
    if i > 1:
        if i < 10:
            path = file_path + root + '_0' + str(i)
            data = appenddata(data, path)
   
    if i > 9:
        path = file_path + root + '_' + str(i)
        data = appenddata(data, path)

# Calculate counts of > threshold
count_over = 0
threshold = 25
for point in data:
    if point > threshold:
        count_over = count_over + 1

# plot data
print(data)
binwidth = 1
plt.hist(data, bins=range(min(data), max(data) + binwidth, binwidth))
plt.xlabel('Intensity')
plt.ylabel('Count')
plt.title(root)
plt.text(max(data)/2, 3000, f"Count over {threshold}: {count_over}")
plt.show()
