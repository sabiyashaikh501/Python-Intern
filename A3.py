# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:20:18 2021

@author: Sabiya Shaikh
"""


import json
j_str = {'c': 5, 'd': 7, 'a': 1, 'b': 2}
print("Original String:")
print(j_str)
print("\nJSON data:")
print(json.dumps(j_str, sort_keys=True, indent=4))
