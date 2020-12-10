#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 01:04:33 2020

@author: edyta
"""

data = [line.strip(':') for line in open("data.txt", 'r')]
#print(data)
data22 = []
for elem in data:
    data22.append(elem.replace('-', ' '))
data2 = []
for elem in data22:
    data2.append(elem.replace(':', ''))

indata = []
#split
for i in data2:
    indata.append(i.split(' '))
    

    
    
def split(word, letter): 
    counter = 0
    for char in word:
        if letter == char:
            counter+= 1
    return counter


def split1(word): 
    return [char for char in word]


tup = []
for elem in indata :
    tup.append([(int(elem[0])), int(elem[1]), elem[2], (split(elem[3], elem[2]))])
    
counter2 = 0
for e in tup:
    if e[0] <= e[3] <= e[1]:
        counter2 +=1
        
##Part two 
tup1 = []
for elem in indata :
    tup1.append([(int(elem[0])), int(elem[1]), elem[2], (split1(elem[3]))])


counter3 = 0
for e in tup1:
    a=e[0]
    b=e[1]
    if ((e[2] == e[3][b])):
        counter3 +=1
        
counter4 = 0
for e in tup1:
    a=e[0]
    b=e[1]
    if (e[2] == e[3][a]):
        counter4 +=1 
       
counter5 = 0
for e in tup1:
    a=e[0] -1
    b=e[1] -1
    if (e[2] == e[3][a]) and (e[2] != e[3][b]):
       counter5 +=1

counter55 = 0
for e in tup1:
    a=e[0]-1
    b=e[1]-1
    if (e[2] != e[3][a]) and (e[2] == e[3][b]):
       counter55 +=1
