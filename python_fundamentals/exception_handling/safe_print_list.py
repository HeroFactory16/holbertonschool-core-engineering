#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(0, x):
            print(my_list[x], end="")
    except:
        print("Index out of bounds")
    return i
