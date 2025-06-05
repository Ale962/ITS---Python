# Exercise 3

'''
3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45

'''

list1 = []
list2 = []
list3 = []
list4 = []

for x in range(2, 14+1, 2):
    list1.append(x)
print(*list1)

for y in range(1, 13+1, 3):
    list2.append(y)
print(*list2)

for z in range(0, 30+1, 5):
    list3.append(z)
print(*list3[::-1])

for w in range(5,45+1, 10):
    list4.append(w)
print(*list4)