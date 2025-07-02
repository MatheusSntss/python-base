#!/bin/user/env python3
"""Print multiplication tables from 1 to 10 
---- table from 1 ----
        1 x 1 = 1
        1 x 2 = 2
        1 x 3 = 3
...
######################
---- table from 2 ----
        2 x 1 = 2
        2 x 2 = 4
        2 x 3 = 6
...
#####################
"""
__version__ = "0.1.1"
__author__ = "Matheus"


for n1 in range(1,11):
    print("{:-^18}".format(f"table from {n1}"))
    print()
    for n2 in range(1,11):
        result = n1 * n2 
        print("{:^18}".format(f"{n1} x {n2} = {result}"))
    print("#" * 18)
