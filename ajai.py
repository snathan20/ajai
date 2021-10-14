# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:44:10 2021

@author: sugan
"""

import csv
import sys
import matplotlib.pyplot as plt


import numpy as np

np.random.uniform()


a = np.random.normal(size=10)
b = np.random.normal(size= 10)




ecd = np.sum(np.square(a-b))

print(np.sqrt(ecd))

dist = np.linalg.norm(a-b)
print(dist)


# print(a)
# plt.hist(a)
# plt.show() 

f = open('TB.csv')

# for row in csv.reader(f, newline=''):
#     reader = csv.reader(f)
#     next(reader)
#     r3 = [float(row[3]) for row in reader]
#     try:
#         avg3 = round(sum(r3) / len(r3),2)
#     except ZeroDivisionError:
#         avg3

#     print("================================================")
#     print(avg3)
#     print("================================================")
    
        
# with open('tb.csv', newline = '') as f:
#     reader = csv.reader(f)
#     next(reader)
#     r3 = [float(row[3]) for row in reader]
#     avg3 = round(sum(r3) / len(r3),2)

#     try:
#         avg3 = round(sum(r3) / len(r3),2)
#     except ZeroDivisionError:
#         avg3

#     print("================================================")
#     print(avg3)
#     print("================================================")
    
    



# with open('tb.csv', newline = '') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         if row[5] == '1990':
#             r5 = [(row[5]=='1990') for row in reader]
#             avg5 = sum(r5) / len(r5),2)
#     try:
#         avg5 = round(sum(r5) / len(r5),2)
#     except ZeroDivisionError:
#         avg5

#     print("================================================")
#     print(avg5)
#     print("================================================")
    
# with open('tb.csv', newline = '') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         if row[5] == '2011':
#             r5 = [float(row[5]) for row in reader]
#             avg5 = round(sum(r5) / len(r5),2)
#     try:
#         avg5 = round(sum(r5) / len(r5),2)
#     except ZeroDivisionError:
#         avg5

#     print("================================================")
#     print(avg5)
#     print("================================================")


#QPart 2 

