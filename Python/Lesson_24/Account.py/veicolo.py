class Veicolo:

    def __init__(self, marca: str, modello: str, anno: int):

        self.__setMarca(marca)
        self.__setModello(modello)
        self.__setAnno(anno)

    def __setMarca(self, marca: str) -> None:
        self.__marca = marca
    
    def __setModello(self, modello: str) -> None:
        self.__modello = modello

    def __setAnno(self, anno: int) -> None:
        self.__anno = anno

    def getMarca(self) -> str:
        return self.__marca
    
    def getModello(self) -> str:
        return self.__modello
    
    def getAnno(self) -> int:
        return self.__anno
    
    def descrivi_veicolo(self) -> None:
        print(f"Marca: {self.getMarca()}, Modello: {self.getModello()}, Anno: {self.getAnno()}")


class Auto(Veicolo):

    def __init__(self, marca, modello, anno, numero_porte: int):
        super().__init__(marca, modello, anno)
        self.__setNumeroPorte(numero_porte)
    
    def __setNumeroPorte(self, numero_porte: int):
        self.__numero_porte = numero_porte

    def getNumeroPorte(self) -> int:
        return self.__numero_porte
    
    def descrivi_veicolo(self) -> None:
        print(f"Marca: {self.getMarca()}, Modello: {self.getModello()}, Anno: {self.getAnno()}, Numero di porte: {self.getNumeroPorte()}")
    

class Moto(Veicolo):

    def __init__(self, marca, modello, anno, tipo: str):
        super().__init__(marca, modello, anno)
        self.__setTipo(tipo)

    def __setTipo(self, tipo: str) -> None:
        self.__tipo = tipo

    def getTipo(self) -> str:
        return self.__tipo
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.getMarca()}, Modello: {self.getModello()}, Anno: {self.getAnno()}, Tipo: {self.getTipo()}")
    

if __name__ == '__main__':

    veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
    auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
    moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto

    veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
    auto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Auto
    moto.descrivi_veicolo()  # Test del metodo descrivi_veicolo 