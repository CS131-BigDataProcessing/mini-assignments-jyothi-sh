import math

def power_function(x,y):
    answer = math.pow(x,y)
    return answer

def divide_function(x,y):
    if(y!=0):
        answer = x/y
        return answer
    else:
        return "Division By Zero Not Allowed"

import math

def power(x, y):
    return math.pow(x, y)

def divide(a, b):
    if b == 0:
        raise ValueError("---denominator cannot be 0")
    return a / b

