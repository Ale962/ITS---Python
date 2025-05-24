from typing import Self

class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages


    @classmethod
    def from_string(cls, repr_str: str) -> Self:
        sub_strs: list = repr_str.split(",")
        return cls(sub_strs[0], sub_strs[1], sub_strs[2])