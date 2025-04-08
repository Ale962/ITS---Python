# Lesson 13 Exercise 8

def volwescounter(line: str) -> int:

    if line == "":
        return 0
    
    if line[0].lower() in ["a", "e", "i", "o", "u"]:
        return 1 + volwescounter(line[1:])
    
    else:
        return 0 + volwescounter(line[1:])
    
print(f'Ciao contiene questo numero di vocali : {volwescounter("ciao")}')