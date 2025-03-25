# Howork Exercise 10

'''
Esercizio 10
Scrivere un programma che permetta di analizzare una lista di numeri interi inseriti dall’utente.

Il programma deve:

acquisire una sequenza di numeri interi, terminando l’inserimento quando l’utente digita 0 (che non deve essere considerato nei calcoli);
calcolare e visualizzare la somma di tutti i numeri pari inseriti;
calcolare e visualizzare la media di tutti i numeri dispari inseriti;
determinare e visualizzare il numero con la frequenza più alta (cioè quello che compare più volte nella lista);
se più numeri hanno la stessa frequenza massima, visualizzarli tutti.
Esempio di input e output
Input:

Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 2
Inserisci un numero (0 per terminare): 7
Inserisci un numero (0 per terminare): 3
Inserisci un numero (0 per terminare): 4
Inserisci un numero (0 per terminare): 0
Output:

Somma dei numeri pari: 10
Media dei numeri dispari: 5.67
Numero più frequente: 7 (2 volte)
'''
# Start of the Program
print("Program running")

# Variable needed
n: int = int(input("Write the number here (Write 0 to end the program): "))
numbers: list = []                  # List of the numbers inserted
sum_even: int = 0                   # Variable needed to do the sum of the even numbers
average_odd: int = 0                # Variable needed to count the average of the odd numbers
i: int = 1                          # Counter to count how many odd numbers are inserted
sum_odd: int = 0                    # Variable needed to do the sum of the odd numbers
numbers_counter: dict = {}          # Dictionary needed to keep track of the numbers and their ripetions
max_equal_number: list = []         # List where the most inserted number/s is/are stored
max_equal_number_counter: int = 0   # Variable needed to see the number of repition of that number

# Start of the cicle
while n != 0:
    
    if n % 2 != 0:      # Checking if a number is odd and calculating the average of the odd numbers
        sum_odd += n
        average_odd = sum_odd / i
        i += 1    
    else:               # Checking if a number is even and adding it to sum of the even numbers
        sum_even += n
    
    numbers.append(n)
    
    # Adding the numbers to the dictionary (The value in this disctionary rappresent the number of repition)
    if n in numbers_counter:                # Checking if they are already present and increasing the value of 1
        numbers_counter[n] += 1
    else:                                   # Checking if they are not present and if so create a new key with the number and value of 1
        numbers_counter[n] = 1
        
    # Restarting the cicle untill 0 is inserted
    n: int = int(input("Write the number here (Write 0 to end the program): "))

# Calling each key and value in our dictionary    
for number, count in numbers_counter.items():
    
    # Check to see if the value (counter of the ripetions if the numbers), is the highest
    if count > max_equal_number_counter:
        max_equal_number_counter = count
        max_equal_number = [number]
    
    # Check to see if there are more numbers with the same value and append it to the list of the most used numbers    
    elif count == max_equal_number_counter:
        max_equal_number.append(number)

        

print(f"The sum of the even numbers is: {sum_even}")
print(f"The average of the odd numbers is: {average_odd}")
print(f"The most frequent number/s is/are: {max_equal_number} ({max_equal_number_counter} times)")