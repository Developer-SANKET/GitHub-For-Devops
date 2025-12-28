import os
import sys

x = 10  # unused variable (pylint warning)


def add(a, b):
    return a + b


def multiply(a,b):   # spacing issue
    return a*b       # missing spaces


def print_value():
    print("Value is:", y)   # undefined variable (error)


def long_function_name_with_many_parameters(param1, param2, param3, param4):
    return param1 + param2 + param3 + param4


print(add(5, 3);