from classes import Author
from classes import BookItem
from classes import BookStore

def main():
    # author, book item, bookstore

    author1 = Author(name = "Raj Rathod", author_id = "ABCDE-FGHI")
    author2 = Author(name = "James Bond", author_id = "JKLM-NOPQ")
    author3 = Author(name = "Tony Stark", author_id = "RSTU-VWXY")

    book_item1 = BookItem(name = "The Autobiography of Raj", author = author1, year_published = 2023)
    book_item2 = BookItem(name = "How to Programme", author = author2, year_published = 1987)
    book_item3 = BookItem(name = "How to make a million dollars", author = author3, year_published = 1000)
    book_item_storage = [book_item1, book_item2, book_item3]
    book_store1 = BookStore(name = "Raj's Library", book_shelve = book_item_storage)

    print(book_store1.__dict__)

if __name__ == "__main__":
    main()