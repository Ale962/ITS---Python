class Book:

    def __init__(self, title: str, author: str, status: str="Avaiable"):
        self.setTitle(title)
        self.setAuthor(author)
        self.setStatus(status)

    def setTitle(self, title) -> None:
        self.__title = title

    def setAuthor(self, author) -> None:
        self.__author = author

    def setStatus(self, status) -> None:
        self.__status = status

    def getTitle(self) -> str:
        return self.__title
    
    def getAuthor(self) -> str:
        return self.__author
    
    def getStatus(self) -> str:
        return self.__status
    
    def __str__(self) -> str:
        return f"The book is {self.getTitle()}, written by {self.getAuthor()}, and its aviability is {self.getStatus()}"
    
class Library:
    def __init__(self, name: str):
        self.setName(name)
        self.__book_shell: dict[Book, int] = {}

    def setName(self, name) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name
    
    def getBooks(self) -> list:
        return self.__book_shell

    def addBook(self, book: Book, number: int) -> None:
        if book not in self.__book_shell:
            self.__book_shell[book] = number
        else:
            print(f"Book {book.getTitle()} already present in the library, is avaiability is {self.__book_shell[book]}, and is avaiability is {book.getStatus()}.")


    def borrowBook(self, title: str) -> str:
        for book in self.__book_shell:
            if book.getTitle() == title:
                if self.__book_shell[book] > 0:    
                    self.__book_shell[book] -= 1
                    if self.__book_shell[book] == 0:
                        book.setStatus("Borrowed")
                        return f"There are no more copies of {title}, all copies have been borrowed."
                    else:
                        return f"The book {title} is avaiable, there are {self.__book_shell[book]} copies left."
        else:
            return f"The book {title} is not in the library"
        
    def returnBook(self, title: str) -> str:
        for book in self.__book_shell:
            if book.getTitle() == title:
                if self.__book_shell[book] > 0:
                    self.__book_shell[book] += 1
                    return f"The book {title} is avaiable and there are {self.__book_shell[book]} copies avaiable."
                else:
                    book.setStatus("Avaiable")
                    self.__book_shell[book] += 1
                    return f"The book {title} is now avaiable and there are {self.__book_shell[book]} copies avaiable."

    def listBooks(self) -> None:
        if not self.__book_shell:
            print("The library is empty")
        else:
            for book in self.__book_shell.keys():
                print(book)

    def __str__(self) -> str:
        return f"THe library {self.getName()} contains {self.getBooks()}."
    

if __name__ == "__main__":
    book1 = Book("1984", "George Orwell")
    book2 = Book("Brave New World", "Aldous Huxley")
    book3 = Book("Fahrenheit 451", "Ray Bradbury")


    my_library = Library("City Library")
    my_library.addBook(book1, 3)
    my_library.addBook(book2, 2)
    my_library.addBook(book3, 1)

    print("\n--- Lista iniziale libri ---")
    my_library.listBooks()

    print("\n--- Prestito libro '1984' ---")
    print(my_library.borrowBook("1984"))

    print("\n--- Prestito libro 'Fahrenheit 451' ---")
    print(my_library.borrowBook("Fahrenheit 451"))
    print(my_library.borrowBook("Fahrenheit 451"))

    print("\n--- Restituzione libro 'Fahrenheit 451' ---")
    print(my_library.returnBook("Fahrenheit 451"))

    print("\n--- Lista finale libri ---")
    my_library.listBooks()
