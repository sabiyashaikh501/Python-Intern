# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:49:17 2021

@author: Sabiya Shaikh
"""


List =["hey python\n ","is a great programming\n ","language",'!!'] 


file1 = open('files.txt', 'w') 
file1.writelines(List) 
file1.close() 
  
 
file1 = open('files.txt', 'r') 
count = 0
  
for line in file1: 
    count += 1
    print("Line{}: {}".format(count, line.strip())) 

file1.close()
  