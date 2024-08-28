#!/usr/bin/env python3

def greet_programmer():
    """Prints a greeting to the programmer."""
    print("Hello, programmer!")

def greet(name):
    """Prints a greeting to the given name."""
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """Prints a greeting to the given name, defaulting to 'programmer'."""
    print(f"Hello, {name}!")

def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def halve(number):
    """Returns half of the given number."""
    return number / 2
