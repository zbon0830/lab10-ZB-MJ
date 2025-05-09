# https://github.com/zbon0830/lab10-ZB-MJ
# Partner 1: Zachary Bon
# Partner 2: Maxine Johnson
"""
calculator.py
- Defines functions used to create a simple calculator
One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        print(e)
        raise

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    else:
        return b / a

def logarithm(a,b):
    if a <= 0 or a == 1:
        raise ValueError("Base of logarithm must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm operand must be positive.")
    return math.log(b, a)

def exp(a, b):
    return a ** b




