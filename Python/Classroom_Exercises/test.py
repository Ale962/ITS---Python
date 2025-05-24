from MathOperation import MathOperations
from Book import Book

if __name__ == "__main__":

    print(MathOperations.add(12, 1.6))
    print(MathOperations.add(150, 121))
    print(MathOperations.multiply(12, 11.6))
    book_str: str = "La Divina Commedia, D. Alighieri, 999000666"
    divina_commedia: Book = Book.from_string(book_str)