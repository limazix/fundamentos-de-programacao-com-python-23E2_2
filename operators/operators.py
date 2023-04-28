# -*- coding: utf-8 -*-


def add(a: int, b: int) -> int:
    """ It add two numbers
        
        param a: First value
        type a: int
        param b: Second valor
        type b: int
        
        return: int
    """
    if type(a) == str or type(b) == str:
        raise TypeError()
    return a + b


def subtraction(a, b):
    """ It subtract two numbers
        
        param a: First value
        type a: int, float
        param b: Second valor
        type b: int, float
        
        return: int, float
    """
    if type(a) == str or type(b) == str:
        raise TypeError()
    return a - b


def division(a, b):
    """ It divides two numbers
        
        param a: First value
        type a: int, float
        param b: Second valor
        type b: int, float
        
        return: int, float
    """
    if type(a) == str or type(b) == str:
        raise TypeError()
    return a / b
