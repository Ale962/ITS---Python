from __future__ import annotations

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
            
    def ratePercentage(self) -> str:
        rate_1 = 0
        rate_2 = 0
        rate_3 = 0
        rate_4 = 0
        rate_5 = 0
        for n in self.getReviews():
            if n <= 1:
                rate_1 += 1
            elif n <= 2:
                rate_2 += 1
            elif n <= 3:
                rate_3 += 1
            elif n <= 4:
                rate_4 += 1
            else:
                rate_5 += 1
        rate_perc1 = ((len(self.getReviews())*100)/rate_1)
        rate_perc2 = ((len(self.getReviews())*100)/rate_2)
        rate_perc3 = ((len(self.getReviews())*100)/rate_3)
        rate_perc4 = ((len(self.getReviews())*100)/rate_4)
        rate_perc5 = ((len(self.getReviews())*100)/rate_5)
        return rate_perc1, rate_perc2, rate_perc3, rate_perc4, rate_perc5

    def recensione(self) -> str:
        return f'Titolo: {self.getTitle()}\nMedia: {self.getMedia()}\nRating: {self.getRating()}'