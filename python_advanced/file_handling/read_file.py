#!/usr/bin/env python3
"""
read_file.py

Simple text file reader.
"""
def read_file(filename=""):
    """
    Reads a text file and print its content in stdout.
    File's encoded as UTF-8
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
