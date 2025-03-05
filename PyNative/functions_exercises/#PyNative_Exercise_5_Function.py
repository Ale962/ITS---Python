# PyNative Exercise 5 Function

'''
    Create an outer function that will accept two parameters, a and b
    Create an inner function inside an outer function that will calculate the addition of a and b
    At last, an outer function will add 5 into addition and return it
'''


def addition(a:float, b:float):
    total:float = a + b
    return total

def plus(a, b):
    totale: float = addition(a, b)
    totale += 5
    return totale

a: float = input("Write first number: ")
b: float = input("Write second number: ")

total = plus(a, b)

print(total)
