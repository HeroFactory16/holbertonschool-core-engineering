#!/usr/bin/env python3
"""
append_write.py

Simple text file writer.
"""


def append_write(filename="", text=""):
    """
    Appends text into a file and returns the number of printed characters.
    File's encoded as UTF-8
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            return file.write(text)
    except FileNotFoundError:
        with open(filename, "x", encoding="utf-8") as file:
            return file.write(text)

    return 0
