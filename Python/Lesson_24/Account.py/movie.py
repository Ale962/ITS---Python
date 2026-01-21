class Movie:
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False):
        self.__setMovieID(movie_id)
        self.__setTitle(title)
        self.__setDirector(director)
        self.__setIsRented(is_rented)
    
    def __setMovieID(self, movie_id: str) -> None:
        self.__movie_id = movie_id

    def __setTitle(self, title: str) -> None:
        self.__title = title
    
    def __setDirector(self, director: str) -> None:
        self.__director = director

    def __setIsRented(self, is_rented: bool) -> None:
        self.__is_rented = is_rented

    def getTitle(self) -> str:
        return self.__title
    
    def getIsRented(self) -> bool:
        return self.__is_rented

    def rent(self) -> None:
        if not self.__is_rented:
            self.__setIsRented(True)
        else:
            print(f"Il film '{self.getTitle()}' è già noleggiato.")
    
    def return_movie(self) -> None:
        if self.__is_rented:
            self.__setIsRented(False)
        else:
            print(f"Il film '{self.getTitle()}' non è stato noleggiato da questo cliente.")


class Customer:

    def __init__(self, customer_id: str, name: str, rented_movies: None|list[Movie] = None):
        self.__setCustomerID(customer_id)
        self.__setName(name)
        if rented_movies == None:
            self.__rented_movies: list[Movie] = []
        else:
            self.__rented_movies: list[Movie] = rented_movies

    def __setCustomerID(self, customer_id: str) -> None:
        self.__customer_id = customer_id

    def __setName(self, name: str) -> None:
        self.__name = name

    def rent_movie(self, movie: Movie) -> None:
        if movie.getIsRented() == False:
            movie.rent()
            self.__rented_movies.append(movie)

        else:
            print(f"Il film '{movie.getTitle()}' è già noleggiato.")

    def return_movie(self, movie: Movie) -> None:
        if movie in self.__rented_movies:
            self.__rented_movies.remove(movie)
            movie.return_movie()
        else:
            print(f"Il film '{movie.getTitle()}' non è stato noleggiato da questo cliente.")

    def getMovies(self) -> list[Movie]:
        return self.__rented_movies


class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie]|None = None, customers: dict[str, Customer]|None = None):

        if not movies:
            self.__movies: dict[str, Movie] = {}
        else:
            self.__movies: dict[str, Movie] = movies

        if not customers:
            self.__customers: dict[str, Customer] = {}
        else:
            self.__customers: dict[str, Customer] = customers

    def add_movie(self, movie_id: str, title: str, director: str) -> None:

        if movie_id not in self.__movies:
            movie: Movie = Movie(movie_id, title, director)
            self.__movies[movie_id] = movie
        else:
            print(f"Il film con ID '{movie_id}' esiste già.")

    def register_customer(self, customer_id: str, name: str) -> None:

        if customer_id not in self.__customers:
            customer: Customer = Customer(customer_id, name)
            self.__customers[customer_id] = customer
        else:
            print(f"Il cliente con ID '{customer_id}' è già registrato.")

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        
        if customer_id in self.__customers and movie_id in self.__movies:
            self.__customers[customer_id].rent_movie(self.__movies[movie_id])
        
        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str) -> None:

        if customer_id in self.__customers and movie_id in self.__movies:
            self.__customers[customer_id].return_movie(self.__movies[movie_id])

        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:

        if customer_id in self.__customers:
            return self.__customers[customer_id].getMovies()
        else:
            print("Cliente non trovato.")