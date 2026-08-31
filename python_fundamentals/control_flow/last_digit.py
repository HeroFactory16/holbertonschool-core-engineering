#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)
last = number % 10
output = f"Last digit of {number} is {last}"

if last == 0:
    output += "and is 0"
elif last < 5:
    output += "and is less than 6 and not 0"
if last > 5:
    output += "and is greater than 5"

print(output)
