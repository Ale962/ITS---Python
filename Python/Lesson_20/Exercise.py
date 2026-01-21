from abc import ABC

class Pagamento:

    def __init__(self, importo: float):
        self.__setImporto(importo)

    def __setImporto(self, importo: float) -> None:
        self.__importo = importo

    def getImporto(self) -> float:
        return self.__importo
    
    def dettagliPagamento(self) -> str:
        return f"L'importo del pagamento è {(self.getImporto()):.2f}"
    
class PagamentoContanti(Pagamento):
    
    def __init__(self, importo):
        super().__init__(importo)

    def inPezziDa(self) -> None:
        importo_totale = self.getImporto()
        money_value: dict[float, int] = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.01: 0}
        while importo_totale > 0:
            for key, value in money_value.items():
                if key <= importo_totale:
                    money_value[key] += 1
                    importo_totale = round((importo_totale-key), 2)
        print('Da pagare con: ')
        for key, value in money_value.items():
            if value > 0:
                print(f'{value} pezzi da {key}')


    def dettagliPagamento(self):
        return super().dettagliPagamento() + f', il pagamento è in contati. ' + f'{self.inPezziDa()}'
    
class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, importo, titolare: str, data: str, numero_carta: str):
        super().__init__(importo)
        self.__setTitolare(titolare)
        self.__setData(data)
        self.__setNumero(numero_carta)

    def __setTitolare(self, titolare) -> None:
        self.__titolare = titolare

    def __setData(self, data) -> None:
        self.__data = data

    def __setNumero(self, numero_carta) -> None:
        self.__numero_carta = numero_carta

    def getTitolare(self) -> str:
        return self.__titolare
    
    def getData(self) -> str:
        return self.__data
    
    def getNumero(self) -> str:
        return self.__numero_carta
    
    def dettagliPagamento(self):
        return super().dettagliPagamento() + f" il pagamento avviene con carte, i dati della carta sono: titolare: {self.getTitolare()}, data: {self.getData()}, numero carta: {self.getNumero()}"

if __name__ == '__main__':
    p1 = Pagamento(120)
    print(p1.dettagliPagamento())

    p2 = PagamentoContanti(352.42)
    p2.dettagliPagamento()