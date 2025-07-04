from __future__ import annotations
import random

class Media:

    def __init__(self, title: str):
        self.__reviews: list[int] = []
        self.setTitle(title)

    def setTitle(self, title: str) -> None:
        self.__title = title

    def getTitle(self) -> str:
        return self.__title
    
    def getReviews(self) -> list:
        return self.__reviews
    
    def aggiungiValutazione(self, n: int) -> None:
        if n >= 1 and n <= 5:
            self.__reviews.append(n)
        else:
            raise ValueError('Feedback must be between 1 adn 5')
        
    def getMedia(self) -> int:
        if len(self.getReviews()) >= 1:    
            media = (sum(self.getReviews()))/(len(self.getReviews()))
            return media
    
    def getRating(self):
        media = self.getMedia()
        match int(media):
            case 1:
                return 'Terribile'
            case 2:
                return 'Brutto'
            case 3:
                return 'Normale'
            case 4:
                return 'Bello'
            case 5:
                return 'Grandioso'
            case _:
                return 'Not enough reviews to get a rating'
            
    def ratePercentage(self, v: int) -> str:
        i = 0
        for x in self.getReviews():
            if x == v:
                i += 1
        rate = (i*100)/len(self.getReviews())

        match v:
            case 1:
                return f'Terribile: {rate}%'
            case 2:
                return f'Brutto: {rate}%'
            case 3:
                return f'Normale: {rate}%'
            case 4:
                return f'Bello: {rate}%'
            case 5:
                return f'Grandioso: {rate}%'
            case _:
                return f'Inserted value is not a possible vote and is not possible to calculate its percentage'
            

    def recensione(self) -> str:
        return f'Titolo: {self.getTitle()}\nRatings: {self.getReviews()}\nMedia: {self.getMedia()}\nRating: {self.getRating()}\n{self.ratePercentage(1)}\n{self.ratePercentage(2)}\n{self.ratePercentage(3)}\n{self.ratePercentage(4)}\n{self.ratePercentage(5)}'
    

class Film(Media):
    
    def __init__(self, title):
        super().__init__(title)

if __name__ == '__main__':

    film1 = Film("Inception")
    film2 = Film("Titanic")

    for i in range(20):
        film1.aggiungiValutazione(random.randint(1,5))
        film2.aggiungiValutazione(random.randint(1,5))
    
    print()
    print('--------------------'*4)
    print(film1.recensione())
    print('--------------------'*4)
    print()
    print('--------------------'*4)
    print(film2.recensione())
    print('--------------------'*4)
    print()