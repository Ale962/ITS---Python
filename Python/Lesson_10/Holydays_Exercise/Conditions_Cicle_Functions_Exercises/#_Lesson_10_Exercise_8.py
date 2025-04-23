# Lesson 10 Exercise 8

'''

Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.

Expected Output:

print(time_difference(1, 0, 0, 3, 15, 30)) --> 8130

print(time_difference(0, 0, 0, 12, 0, 0)) --> 43200

'''

def seconds_since_noon(h: int, m: int, s: int):

    seconds = 0

    if h <= 12:
        seconds = s + (m*60) + (h*60*60)
    else:
        h -= 12
        seconds = s + (m*60) + (h*60*60)

    return seconds

def time_difference(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int):

    seconds1 = seconds_since_noon(h1, m1, s1)
    seconds2 = seconds_since_noon(h2, m2, s2)

    difference = 0

    if seconds1 > seconds2:
        difference = seconds1 - seconds2

    else:
        difference = seconds2 - seconds1

    return difference


print(time_difference(13, 0, 0, 15, 15, 30))
print(time_difference(0, 0, 0, 24, 0, 0))