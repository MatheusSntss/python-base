#!/usr/bin/env python3
import os
import sys

#EAFP
try: 
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f'{str(e)}')
    sys.exit(1)
    #TODO:usar retry
    

try:
    print(names[2])
except:
    print("ERROR: Missing name in the list")
    sys.exit(1)
