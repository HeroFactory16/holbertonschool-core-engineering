#!/usr/bin/env python3
from calculation_1 import add
from calculation_1 import sub
from calculation_1 import mult
from calculation_1 import divide

if __name__ == "__main__":
    a = 10
    b = 5

    print(a, "+".format(), b, "=", add(a, b))
    print(a, "-".format(), b, "=", sub(a, b))
    print(a, "*".format(), b, "=", mult(a, b))
    print(a, "/".format(), b, "=", divide(a, b))
