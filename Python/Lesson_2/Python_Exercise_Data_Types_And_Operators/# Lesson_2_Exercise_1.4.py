# Lesson 2 Exercise 1.4

'''1-4. Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, una cifra per riga:

2
0
2
4'''

x:int = 1996

a =  x // 1000
print(a)

b = (x - 1000) // 100
print(b)

c = (x - 1900) // 10
print(c)

d = (x - 1990)
print(d)

print(f"\n{(x - 996) // 1000}\n{(x - 1000) // 100}\n{(x - 1900) // 10}\n{x - 1990}")