#!/usr/bin/env python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except:
        pass
    finally:
        print("Inside result: {:.1f}".format(result))
    return result
