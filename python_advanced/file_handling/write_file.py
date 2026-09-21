#!/usr/bin/env python3
"""
write_file.py

Simple text file writer.
"""


def write_file(filename="", text=""):
    """
    Reads a text file and print its content in stdout.
    File's encoded as UTF-8
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            return file.write(text)
    except FileNotFoundError:
        with open(filename, "x", encoding="utf-8") as file:
            return file.write(text)

    return 0
