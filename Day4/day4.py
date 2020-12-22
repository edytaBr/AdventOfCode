#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:02:12 2020

@author: edyta
"""
import re 


str1 = open('input.txt', 'r').read()

x = str1.split('\n\n')

data2 = []

for elem in x:
    a = elem.replace('\n', ' ')
    a = a.split(' ')
    data2.append(a)

count = 0
for elem in data2:
    if len(elem) == 7:
        count+1
        for e in elem:
            if e[0:3] == 'cid':
                count+=1
count2 = 0
for elem in data2:
    if len(elem) == 8:
        count2+=1
        
result = count+count2