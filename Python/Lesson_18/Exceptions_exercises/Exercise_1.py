# Lesson 18 Exercise 1

'''
Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). Handle ValueError if the input is negative by returning an informative message.

'''
import math

def safe_sqrt(x):

    try:
        return math.sqrt(x)
    except ValueError:
        return "Number must be positive"

print(safe_sqrt(12))
print(safe_sqrt(-12))