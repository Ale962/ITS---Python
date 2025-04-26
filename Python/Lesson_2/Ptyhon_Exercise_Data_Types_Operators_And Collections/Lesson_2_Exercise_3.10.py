# Lesson 2 Exercise 3.10

'''3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.'''

thing: list = ["Gran Sasso", "Roma", "Lazio", "1900", "Tevere", "Olimpia"]
print(thing)
thing.pop (0)
print(thing)
thing.insert(0, "Olimpico")
print(thing)
thing.append("22")
print(thing)
del thing [5]
print(thing)
thing.reverse()
print(thing)
thing.sort()
print(thing)
thing.sort(reverse = True)
print(thing)