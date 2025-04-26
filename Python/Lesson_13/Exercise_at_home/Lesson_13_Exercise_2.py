# Lesson 13 Exercise 2

def compoundinterest(m:float, t:int) -> float:

    if t == 0:
        return m
        
    else:
        return 1.005* compoundinterest(m, t-1)
    

    
print(f'L\'interesse maturato da 50000 euro in 12 mesi è {compoundinterest(1000, 3)}')

'''

cI(1000,3) -> dopo il terzo mese io sul mio conto in bacnca avrò 1.005 * SaldoDopo2mesi
cI(1000,2) -> dopo il secondo mese io sul mio conto in banca avrò 1.005 * SaldoDopo1Mese
CI(1000,1) -> dopo il primo mese io sul mio conto in banca avrò 1.005 * saldoIniziale
CI(1000,0) -> perchè se t è 0 significa che non è trascorrso ancora 1 mese da quando ho depositato il mio saldo in bacna. quindi il saldo disponibile rimane 1000

'''