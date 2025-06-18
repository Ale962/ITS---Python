class Movie:
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False):
        self._movie_id = movie_id
        self._title = title
        self._director = director
        if is_rented:
            self._is_rented = is_rented

    def rent(self) -> None:
        if self._is_rented == True:
            print(f'The film {self._title} is already rented')

        else:
            self._is_rented = True

    def return_movie(self) -> None:
        if self._is_rented == False:
            print(f'The film {self._title} is not rented')

        else:
            self._is_rented = True

class Customer:
    def __init__(self, customer_id: str, name: str):
        self._customer_id = customer_id
        self._name = name
        self._rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:
        if movie._is_rented == False:
            self._rented_movies.append(movie)
            movie.rent()
        else:
            print(f'The movie is already rented')

    def return_movie(self, movie: Movie) -> None:
        if movie._is_rented == True:
            self._rented_movies.remove(movie)
            movie.return_movie()
        else:
            print(f'The film {movie._title} has not be rented by {self._name}')

class VideoRentalStore:
    def __init__(self):
        self._movies: dict[str, Movie] = {}
        self._customers: dict[str, Customer] = {}

    def add_movie(self, movie_id:str, title: str, director: str) -> None:
        new_movie: Movie = Movie(movie_id, title, director)
        if movie_id in self._movies.keys():
            print(f'The film with ID {movie_id} is already present')
        else:
            self._movies[movie_id] = new_movie

    def register_customer(self, customer_id: str, name: str) -> None:
        new_customer = Customer(customer_id, name)
        if customer_id in self._customers.keys():
            print(f'The customer with ID {customer_id} is already present')
        else:
            self._customers[customer_id] = new_customer

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id in self._customers.keys():
            if movie_id in self._movies.keys():
                movie: Movie = self._movies[movie_id]
                self._customers[customer_id].rent_movie(movie)
            else:
                print('Customer or movie not found')

    def return_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id in self._customers.keys():
            if movie_id in self._movies.keys():
                movie: Movie = self._movies[movie_id]
                self._customers[customer_id].return_movie(movie)
            else:
                print('Customer or movie not found')

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self._customers.keys():
            return self._customers[customer_id]._rented_movies
        else:
            print('Customer not found')

    def get_all_movies(self) ->list[Movie]:
        list_movies_rented:list[Movie] = []
        for movie in self._movies.values():
            if movie._is_rented:
                list_movies_rented.append(movie)
                
        return list_movies_rented