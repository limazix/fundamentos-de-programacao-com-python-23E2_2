# -*- coding: utf-8 -*-


def add(a, b):
    """ It add two numbers
        
        param a: First value
        type a: int, float
        param b: Second valor
        type b: int, float
        
        return: int, float
    """
    if type(a) == str or type(b) == str:
        raise TypeError()
    return a + b


def substraction(a, b):
    """ It substract two numbers
        
        param a: First value
        type a: int, float
        param b: Second valor
        type b: int, float
        
        return: int, float
    """
    if type(a) == str or type(b) == str:
        raise TypeError()
    return a - b
