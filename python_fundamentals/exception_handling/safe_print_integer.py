#!/usr/bin/env python3
def safe_print_integer(value):
    try:
        print(f"{value:d}")
    except ValueError:
        return False
    return True
