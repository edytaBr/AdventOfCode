#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:46:38 2020

@author: edyta
"""

data = [line.strip() for line in open("data.txt", 'r')]
#print(data)

inte = []
for x in data:
    inte.append(int(x))
    

out = []
yy = len(inte)

#Part1
for x in inte:
    for y in range(yy):
        for z in range(yy):
              out.append(x)
              break
            
        

#Part2
for x in inte:
    for y in range(yy):
        for z in range(yy-1):
          if (x+inte[y]+inte[z]) == 2020:
              out.append(x)
              break
            
        
        
