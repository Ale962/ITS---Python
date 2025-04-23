# Lesson 10 Exercise 4

'''
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51

'''

def print_seq():

    i = 1
    a = 0
    b = 3
    c = 20
    d = 19

    print("Sequanza a):")

    while i <= 6:
        a += 1
        print(a)
        i += 1
    
    i = 1

    print("\nSequenza b):")

    while i <= 5:
        print(b)
        b += 5
        i += 1

    i = 1

    print("\nSequenza c):")

    while i <= 6:
        print(c)
        c -= 6
        i += 1

    i = 1

    print("\nSequenza d):")

    while i <= 5:
        print(d)
        d += 8
        i += 1

print_seq()