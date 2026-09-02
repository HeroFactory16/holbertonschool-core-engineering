#!/usr/bin/env python3
def pow(a, b):
    result = 1
    if b < 0:
        b = -b
        for _ in range (0, b):
            result /= a
        print(result)
        return result

    for _ in range (0, b):
        result *= a
    print(result)
    return result
