# Lesson 3 Exercise 4.5

'''4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.'''

numbers: list = range(1, 1000001)

minimo: int = min(numbers)
massimo: int = max(numbers)
print(f"The minimal is {minimo}, the maximus is {massimo}")

somma: int = sum(numbers)

print(somma)