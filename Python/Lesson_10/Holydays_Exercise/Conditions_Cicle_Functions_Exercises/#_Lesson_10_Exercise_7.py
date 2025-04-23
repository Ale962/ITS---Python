# Lesson 10 Exercise 7

'''
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

Expected Output:

print(frequency_dict(['mela', 'banana', 'mela'])) --> {'mela': 2, 'banana': 1}
'''

def frequency_dict(elements: list) -> dict:

    frequency: dict = {}

    for x in elements:

        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1

    return frequency

print(frequency_dict(['mela', 'banana', 'mela']))