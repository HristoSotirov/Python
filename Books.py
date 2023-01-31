#  В програмата се създава клас Книги с 4 инстанции на класа.
#  Създават се методи за сортиране по име на книгата, търсене по автор и търсене по година. 


class Book:
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author

    def __str__(self):
        return f'({self.book_code}, {self.book_name}, {self.book_author}, \
{self.book_price}, {self.book_year})'

    def __repr__(self):
        return f'({self.book_code}, {self.book_name}, {self.book_author}, \
{self.book_price}, {self.book_year})'

books = [
        Book('A1', 4300, 12.99, 2022, 'B.C.'),
        Book('A2', 4301, 39.99, 2021, 'B.D.'),
        Book('A3', 4302, 36.99, 2021, 'A.C'),
        Book('A4', 4303, 15.99, 2020, 'B.C.'),
    ]
    
def sort_name(books):
    print(sorted(books, key=lambda x: x.book_name, reverse=True))


def author(books, book_author):
    print([book for book in books if book.book_author == book_author])


def search_book(books, book_code):
    for book in books:
        if book.book_code == book_code:
            print(book)
            return
    print('The book is not found')

sort_name(books)
author(books, 'B.C.')
search_book(books, 4302)
search_book(books, 4300)
