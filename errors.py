#!/usr/bin/env python3
import os
import sys

if os.path.exists("names.txt"):
    names = open("names.txt").readlines()
else:
    print('Error: file "name.txt" not found')
    sys.exit(1)
#LBYL - Look before you Leap

if len(names) >= 3:
    print(names[2])
else:
    print("ERROR: Missing name in the list")
    sys.exit(1)
