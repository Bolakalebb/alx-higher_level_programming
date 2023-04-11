#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 2023

@author: Bolakale Aduloju
"""


def matrix_divided(matrix, div):
    # Check if the matrix is a list of lists of integers/floats
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number and not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(num/div, 2) for num in row] for row in matrix]
    return new_matrix

