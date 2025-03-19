# Homework Exercise 5

'''
Esercizio 5
Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.
Scrivere un programma che:
Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto.
Esempio:
Se l'utente inserisce N = 6, può acquistare 6 barrette ottenendo 6 buoni sconto, che gli permettono di riscattare 1 ulteriore barretta gratuita, per un totale di 7 barrette. Alla fine, non rimarranno buoni sconto inutilizzati.
Il programma deve continuare a scambiare i buoni con nuove barrette finché ce ne sono abbastanza per ottenere almeno una barretta gratuita.
'''

# Variables needed
choccolate_bars: int = 0
coupons: int = 0
remaning_coupons: int = 0
free_choccolate_bars: int = 0

# Money available
n: float = float(input("Write your monetary availability here: "))

# Setting up the condition that we need at last n = 1 to calculate everything, otherwise the program does not even start because you need 1 to buy 1 bar
if n >= 1:
    
    # Number of bars bought with the money
    choccolate_bars = n // 1
    
    # The coupons are equal to the bars we can buy
    coupons = choccolate_bars
    
    # Number of free bars earned with the coupons
    free_choccolate_bars = coupons // 6
    
    # Coupons left unused
    remaning_coupons = coupons % 6
    
    # Final number of bars obtained
    choccolate_bars = choccolate_bars + free_choccolate_bars
    
# Final statments and results
print(f"The choccolate bars obtainable are: {choccolate_bars}\nThe coupons left unused are: {remaning_coupons}")