# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:26:33 2024

@author: s2279999
"""


import numpy as np


#where to work
path = 'D:/20240222_CE/1_1_2_294030/'
root = '488'
# how many files were collected
file_numbers=10

# Threshold, change here to set different threshold
green_threshold = 10
red_threshold = 10
sum_threshold = 20
# choose different threshold type between 'sum' and 'and'.
threshold_type = 'and' 

file_list=[]
for i in range (file_numbers):
    if int(i)+1 == 1:
        file_list.append(path+root)
    if int(i) + 1 >1:
        if int(i) + 1 < 10:
            file_list.append(path+root+'_0'+str(i+1))
        else:
            file_list.append(path+root+'_'+str(i+1))


def read_data(path):
    data = np.genfromtxt(path, delimiter = '\t')
    return data

red_data = []
green_data = []
for i in file_list:
    d = read_data(i)
    for row in d:
        green = row[0]
        red = row[-1]
        green_data.append(green)
        red_data.append(red)

# def sum_threshold(red,green,threshold):
#     if red+green > threshold:
#         return red,green
#     else:
#         return 0,0
    
# def add_threshold(red,green,red_threshold,green_threshold):
#     if red >red_threshold:
#         if green > green_threshold:
#             return red,green
#         else:
#             return False
red_count = 0
green_count = 0
Fret_count = 0
if threshold_type == 'sum':
    for i in range (len(red_data)):
        if red_data[i]+green_data[i] > sum_threshold:
            Fret_count +=1
elif threshold_type == 'and':
    for i in range (len(red_data)):
        if red_data[i] > red_threshold:
            red_count += 1
            if green_data[i] > green_threshold:
                Fret_count +=1
        if green_data[i] > green_threshold:
            green_count += 1
            
if threshold_type == 'sum':
    print('The number of FRET event is {}'.format(Fret_count))
else:
    print('The number of red event is {}'.format(red_count))
    print('The number of green event is {}'.format(green_count))
    print('The number of FRET event is {}'.format(Fret_count))

