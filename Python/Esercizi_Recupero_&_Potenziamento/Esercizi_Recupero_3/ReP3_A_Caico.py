# Mostri contro Alieni
from __future__ import annotations
import random


# Classe Creautura
class Creatura:

    # attributi classe Creatura
    def __init__(self, nome: str):
        self.setNome(nome)

    # Setter Nome
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str):
            self.__nome = 'Creatura Generica'
        else:
            self.__nome = nome

    # Getter Nome
    def nome(self) -> str:
        return self.__nome
    
    # Metodo str personalizzato per Creatura
    def __str__(self):
        return f'Creatura: {self.nome()}'
    
# Classe Alieno
class Alieno(Creatura):

    # Attributi Alieno con richiamo alla super Classe
    def __init__(self, nome='Robot-'):
        super().__init__(nome)
        self.__setMatricola()
        self.__setMunizioni()

        # Modifica del metodo setNome della Super Classe per far in modo di adattarla ai parametri e hai controlli necessari
        if nome != 'Robot-':
            print('Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!')
            print()
            nome = 'Robot-'
        self.setNome(str(nome + str(self.matricola())))
        

    # setter Matricola con inizializzazione automatica senza parametri (privato)
    def __setMatricola(self):
        self.__matricola = random.randint(10000, 90000)
    
    def matricola(self) -> int:
        return self.__matricola
    
    # setter munizioni con inzializzazione automatica senza parametri (privato)
    def __setMunizioni(self):
        self.__munizioni: list[int] = list(x**2 for x in range(0, 16))
    
    def munizioni(self) -> list[int]:
        return self.__munizioni
    
    def __str__(self):
        return f'Alieno: {self.nome()}'
    

# Classe  Mostro    
class Mostro(Creatura):
    
    # attributi della classe con richiamo alla super classe
    def __init__(self, nome, urlo_vittoria: str, urlo_sconfitta: str):
        super().__init__(nome)
        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(urlo_sconfitta)
        self.__setAssalto()

    # metodo setter Vittoria con check che l'urlo sia una str (privato)
    def __setVittoria(self, urlo_vittoria: str) -> None:
        if not isinstance(urlo_vittoria, str):
            self.__urlo_vittoria = 'GRAAAHHH'
        else:
            self.__urlo_vittoria = urlo_vittoria

    def vittoria(self) -> str:
        return self.__urlo_vittoria
    

    # metodo setter Sconfitta con check che l'urlo sia una str (privato)
    def __setSconfitta(self, urlo_sconfitta: str) -> None:
        if not isinstance(urlo_sconfitta, str):
            self.__urlo_sconfitta = 'Uuurghhh'
        else:
            self.__urlo_sconfitta = urlo_sconfitta

    def sconfitta(self) -> str:
        return self.__urlo_sconfitta
    
    # metodo setter assalto automizzato senza parametri che ritorna una lista (privato)
    def __setAssalto(self) -> None:
        pool_number = list(x for x in range(1,101))
        self.__assalto: list[int] = random.sample(pool_number, 15)

    def assalto(self) -> list[int]:
        return self.__assalto
    
    def __str__(self):
        nome_list = list(self.nome().lower())
        
        for i in range(1, len(nome_list), 2):
            nome_list[i] = nome_list[i].upper()

        nome_str = "".join(nome_list)
        
        return f'Mostro: {nome_str}'
    
# funzione per vedere il risultato del combattimento
def pariUguali(a: list[int], b: list[int]) -> list:
    # controllo che i numeri delle liste siano interi positivi
    for x, y in zip(a, b):
        if x >= 0 and y >= 0:
            continue
        else:
            raise ValueError('La lista deve contenere numeri interi positivi')

    # confronto i numeri per determinare il risultato del confronto, 0 per i dispari, 1 per i pari
    c: list = []
    for x, y in zip(a, b):
        if x % 2 == 0 and y % 2 == 0:
            num = 1
            c.append(num)
        else:
            num = 0
            c.append(num)
    return c

# funzione che esegue il combattimento
def combattimento(a: Alieno, m: Mostro) -> None:

    # se i due parametri non sono ggetti (istanze) delle classi Alieno e Mostro termina il commbattimento con un messaggio visibile
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print(f'Combattimento interrotto un dei due tra {a} o {m} non è o un alieno o un mostro')

    # Inizia il combattimento
    else:
        # stampa le credenziali e gli attributi dei contendenti
        print(a.__str__())
        print(a.munizioni())
        print()
        print(m.__str__())
        print(m.assalto())
        print()
        print('Combattimento!!')
        result = pariUguali(a.munizioni(), m.assalto())
        counter = 0
        for x in result:
            if x == 1:
                counter += 1

        # risultato a favore del mostro
        if counter >= 4:
            print()
            print(f'{m.vittoria()}\n'*3)
            print()
            proclamaVincitore(m)
            print()
            print('**'+'*'*len(m.__str__())+'**')
            print()
            print('*'+' '*(len(m.__str__())+4)+'*')
            print()
            print(f'*  {m.__str__()}  *')
            print()
            print('*' + ' ' * (len(m.__str__()) + 4) + '*')
            print()
            print('**' + '*' * len(m.__str__()) + '**')

        # Risultato a favore dell'alieno
        else:
            print()
            print(m.sconfitta())
            print()
            proclamaVincitore(a)
            print()
            print('**'+'*'*len(a.__str__())+'**')
            print()
            print('*'+' '*(len(a.__str__())+4)+'*')
            print()
            print(f'*  {a.__str__()}  *')
            print()
            print('*' + ' ' * (len(a.__str__()) + 4)+ '*')
            print()
            print('**' + '*' * len(a.__str__()) + '**')

# Funzione che accerta e stampa il messaggio della tipologia della creaura vincente
def proclamaVincitore(c: Creatura) -> None:
    if isinstance(c,Alieno):
        print('Gli Alieni hanno vinto!!')
    else:
        print('I mostri hanno vinto!!')

if __name__ == "__main__":
    # Esempio 1: Scontro base tra un Alieno e un Mostro
    alieno1 = Alieno()
    mostro1 = Mostro("Zargon", "RRRRAAAH", "Noooooo")
    combattimento(alieno1, mostro1)

    print("\n" + "="*50 + "\n")

    # Esempio 2: Alieno con nome personalizzato (verrà comunque forzato con matricola)
    alieno2 = Alieno("Androide-")
    mostro2 = Mostro("Kragh", "HA!", "ARGH!")
    combattimento(alieno2, mostro2)

    print("\n" + "="*50 + "\n")

    # Esempio 3: Mostro con nomi strani, test degli urli di default
    mostro3 = Mostro("Xylg", 123, 456)  # Non stringhe, attiva default
    combattimento(Alieno(), mostro3)

    print("\n" + "="*50 + "\n")

    # Esempio 4: Tipo errato (test del controllo tipo in combattimento)
    combattimento("non un alieno", mostro1)