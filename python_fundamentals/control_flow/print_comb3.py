#!/usr/bin/env python3
result = "01"
for i in range(0, 10):
    for j in range(0, 10):
        if i < j and not(i == 0 and j == 1):
            result += f", {i}{j}".format()
print(result)
