#!/bin/user/env python3
"""Print multiplication tables from 1 to 10 """
__version__ = "0.1.0"
__author__ = "Matheus"

for number in range(1,11):
    print("---------------------------")
    for other_number in range(1,11):
        print("Table number:",number) 
        print(number, "X", other_number, "=", number*other_number)   
