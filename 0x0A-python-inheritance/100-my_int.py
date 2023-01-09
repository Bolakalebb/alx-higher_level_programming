#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 08 2023

@author: Bolakale Aduloju
"""


class MyInt(int):
    """
    A class that inherits from int
    """
    def __eq__(self, num):
        """
        equal function for MyInt class

        Attributes:
            num (int): an inputed integer

        Returns:
            The opositive booleanof the input
        """
        return (int(self) != num)

    def __ne__(self, num):
        """
        no equal function for MyInt class

        Attributes:
            num (int): an inputed integer

        Returns:
            The opositive booleanof the input
        """
        return (int(self) == num)
