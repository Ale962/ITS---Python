# Homework Execise 9

'''
Esercizio 9
Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate. Quindi:

progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.
'''
######## WARNING !!!!!!!!!!!! #########

### ACTUALLY IS NOT POSSIBLE FOR ME TO SEE IF THIS CODE RUN, I'M FORCED TO USE THE ONLINE EDITOR WHICH GOES ALWAYS IN TIMEOUT WHATEVER I USE, 
### IT COULD BE AN IF OR A WHILE, MATCH STATMENT ARE NOT SUPPORTED IN THE ONLINE EDITOR SO THOSE CAN NOT BE USED, I'M SORRY 


# Setting up the variables needed
x = 4
y = 1
counter1 = 0    # Counter for iteraction to get to have 3.14 
counter2 = 0    # Counter for iteraction to get to have 3.141
counter3 = 0    # Counter for iteraction to get to have 3.1415
counter4 = 0    # Counter for iteraction to get to have 3.14159

# Cicle to search for the iteration needed
while x/y != 3.14159:
    
    while x/y != 3.14:      # Check to count iteration needed to get 3.14
        counter1 += 1
        
    while x/y != 3.141:     # Check to count iteration needed to get 3.141
        counter2 += 1
        
    while x/y != 3.1415:    # Check to count iteration needed to get 3.1415
        counter3 += 1
    
    counter4 += 1           # Check to count iteration needed to get 3.14159
        
    y += 2                  # Adding 2 to the denominator
    
print(f"To obtain π ≈ 3.14 where needed {counter1} iterations")
print(f"To obtain π ≈ 3.141 where needed {counter2} iterations")
print(f"To obtain π ≈ 3.1415 where needed {counter3} iterations")
print(f"To obtain π ≈ 3.14159 where needed {counter4} iterations")