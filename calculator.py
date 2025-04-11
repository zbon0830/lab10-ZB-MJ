"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
<<<<<<< HEAD

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

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def logarithm(a,b):
    if a <= 0 or a == 1:
        raise ValueError("Base of logarithm must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm operand must be positive.")
    return math.log(b, a)

def exponent(a,b):
    return a ** b
