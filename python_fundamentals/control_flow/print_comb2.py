#!/usr/bin/env python3
result = "00"
for i in range(1, 100):
    result += f", {i:02}".format()
print(result)
