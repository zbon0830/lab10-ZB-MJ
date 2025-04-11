"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a,b): a + b

def sub(a,b): a-b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    else:
        return b / a

def log(a, b):
    if a <= 1:
        raise ValueError("Invalid base.")
    else:
        return math.log(b,a)

def exp(a, b): a**b
