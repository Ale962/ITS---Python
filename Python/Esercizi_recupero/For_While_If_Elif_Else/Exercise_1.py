# Exercise 1

'''
1) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.

'''

def validation(x, y, z) -> str:

    if x == True:
        if y == True or z == True:
            return 'Action authorized'
        else:
            return 'Action denied'
    else:
        return 'Action denied'

