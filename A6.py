# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:56:36 2021

@author: Sabiya Shaikh
"""


import array
import binascii
a = array.array('i', [1,2,3,4,5,6])
print("Original array:")
print('A1:', a)
bytes_array = a.tobytes()
print('Array of bytes:', binascii.hexlify(bytes_array))