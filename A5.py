# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:47:58 2021

@author: Sabiya Shaikh
"""


def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("myfile.txt"))