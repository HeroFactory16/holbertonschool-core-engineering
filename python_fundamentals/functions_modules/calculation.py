#!/usr/bin/env python3
from calculation_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    print(a, "+".format(), b, "=", add(a, b))
    print(a, "-".format(), b, "=", sub(a, b))
    print(a, "*".format(), b, "=", mul(a, b))
    print(a, "/".format(), b, "=", div(a, b))
