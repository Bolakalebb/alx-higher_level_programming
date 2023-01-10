#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 1 2023

@author: Bolakale Aduloju
"""


def read_file(filename=""):
    """
    Reads the file

    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
