from flask import Flask

class Iscritto:
    def __init__(self, name: str, ID: int):
        self.__setID(ID)
        self.__setName(name)

    def __setName(self, name: str) -> None:
        self.__name = name

    def __setID(self, ID: int) -> None:
        self.__ID = ID

    def getName(self) -> str:
        return self.__name
    
    def getID(self) -> str:
        return self.__ID

class Istruttore:
    def __init__(self, name: str, ID: int):
        self.__setID(ID)
        self.__setName(name)

    def __setName(self, name: str) -> None:
        self.__name = name

    def __setID(self, ID: int) -> None:
        self.__ID = ID

    def getName(self) -> str:
        return self.__name
    
    def getID(self) -> str:
        return self.__ID

class Corso:
    def __init__(self, name: str, ID: int):
        self.__setID(ID)
        self.__setName(name)

    def __setName(self, name: str) -> None:
        self.__name = name

    def __setID(self, ID: int) -> None:
        self.__ID = ID

    def getName(self) -> str:
        return self.__name
    
    def getID(self) -> str:
        return self.__ID
    
class Centro_Sportivo:
    def __init__(self, corsi: dict[str, Corso] = None, iscritti: dict[str, Iscritto|Corso] = None, istruttori: dict[str, Istruttore|Corso] = None):
        if corsi:
            self_corsi: dict[str, Corso] = corsi
        else:
            self_corsi: dict[str, Corso] = {}

        if iscritti:
            self_iscritti: dict[str, Iscritto|Corso] = iscritti
        else:
            self_iscritti: dict[str, Iscritto|Corso] = {}

        if istruttori:    
            self_istruttori: dict[str, Istruttore|Corso] = istruttori
        else:
            self_istruttori: dict[str, Istruttore|Corso] = {}

app = Flask(__name__)

@app.route('/')
def home():
    return f'<h1>Welcome To Our Sport Center</h1>'


@app.route('/corsi/')
def get_corsi():
    pass