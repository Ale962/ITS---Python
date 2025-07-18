from abc import ABC, abstractmethod
import string

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(self, testoInChiaro):
        pass

class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self, testoCodificato):
        pass

class CifratoreAScorrimento(DecodificatoreMessaggio,CodificatoreMessaggio):

    pool: str = string.ascii_letters + string.punctuation + ' '

    def __init__(self, key: int):
        self.__set_key(key)

    def __set_key(self, key:int):
        self.__key = key

    def __get_key(self) -> int:
        return self.__key
    
    def codifica(self, testoInChiaro) -> str:
        testocriptato:str = ''

        for c in testoInChiaro:
            testocriptato += self.__sposta_carattere(c)

        return testocriptato
    
    def decodifica(self, testoCodificato)-> str:
        testodecriptato = ''

        for c in testoCodificato:
            testodecriptato += self.__decodifica_carattere(c)

        return testodecriptato
    
    def __sposta_carattere(self, c: str) -> str:
        index = __class__.pool.index(c)
        l = __class__.pool[(index + self.__get_key())%len(__class__.pool)]
        return l
    
    def __decodifica_carattere(self, c: str) -> str:
        index = __class__.pool.index(c)
        l = __class__.pool[(index - self.__get_key())%len(__class__.pool)]
        return l
    
class CifratoreACombinazione(DecodificatoreMessaggio, CodificatoreMessaggio):

    def __init__(self, key):
        self.__set_key(key)

    def __set_key(self, key) -> None:
        self.__key = key

    def __get_key(self) -> int:
        return self.__key

    def codifica(self, testoInChiaro: str) -> str:
        testo = ''

        for i in range(self.__get_key()):
            testo = self.__combinazione(testoInChiaro)

        return testo

    def decodifica(self, testoCodificato: str) -> str:
        testo = ''

        for i in range(self.__get_key()):
            testo = self.__decodifica_combinazione(testoCodificato)

        return testo

    def __combinazione(self, testo:str) -> str:
        if len(testo) % 2 == 0:
            mid = len(testo) // 2
            half1: str = testo[:mid]
            half2: str = testo[mid:]
        else:
            mid = len(testo) // 2
            half1: str = testo[:mid]
            half2: str = testo[mid+1:]

        testocombinato = ''

        for i in range(len(half1)):
            if len(half1) == len(half2):
                testocombinato += (half1[i]+half2[i])
            else:
                if i not in range(len(half2)):
                    testocombinato += half1[i]
                else:
                    testocombinato += (half1[i]+half2[i])
        
        return testocombinato
    
    def __decodifica_combinazione(self, testo: str) -> str:
        half1: list[str] = []
        half2: list[str] = []
        for i in range(len(testo)):
            if (i % 2) == 0:
                half1 += testo[i]
            else:
                half2 += testo[i]
        
        testodecombinato:str = str(''.join(half1)) + str(''.join(half2))
        return testodecombinato

if __name__ == '__main__':
    cifr1: CifratoreAScorrimento = CifratoreAScorrimento(10)
    cifr2: CifratoreACombinazione = CifratoreACombinazione(3)

    path = 'Python/Esercizi_Recupero_&_Potenziamento/Exercise_message_codificator/testo.txt'
    path2 = 'Python/Esercizi_Recupero_&_Potenziamento/Exercise_message_codificator/testo_criptato_a_combinazione.txt'
    path3 = 'Python/Esercizi_Recupero_&_Potenziamento/Exercise_message_codificator/testo_criptato_a_scorrimento.txt'

    with open(path, 'r') as file:
        text = file.read()

    textencryptcomb = cifr2.codifica(text)
    textencryptscor = cifr1.codifica(text)

    
    with open(path2, 'w') as file:
        file.write(textencryptcomb)

    with open(path3, 'w')as file:
        file.write(textencryptscor)

    with open(path3, 'r') as file:
        textdecrypt = cifr1.decodifica(file.read())

    with open(path2, 'r') as file:
        textdecrypt2 = cifr2.decodifica(file.read())

    print(textdecrypt)
    print(textdecrypt2)