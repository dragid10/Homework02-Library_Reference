import Settings

"""
Class that stores the definition of what it is to be a book. Simplifies parsing a bit
"""


class Book:
    def __init__(self, key, author, title, publisher, date):
        self.key = key
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date


def parse_book_list(book_list):
    for i in range(0, len(book_list), 6):
        book_type = book_list[i]
        key = book_list[i + 1][4:].strip().rstrip()
        if "Book" in book_type:
            Settings.BOOK_REPOSITORY[key] = Book(
                key,  # Adds Key
                book_list[i + 2][7:].strip().rstrip(),  # Adds author
                book_list[i + 3][7:].strip().rstrip(),  # Adds title
                book_list[i + 4][11:].strip().rstrip(),  # Adds publisher
                book_list[i + 5][6:].strip().rstrip()  # Adds date
            )
            print("Book added!")
        elif "Journal" in book_type:
            print("THIS IS A JOURNAL")


if __name__ == '__main__':
    # The list of books to read in and save
    book_list = open("/home/seyi/programming/school/CSE211/Homework/Homework02/Step1Data.txt").readlines()
    parse_book_list(book_list)  # Parse the file and add each book to the dictionary
    # print(gottenBook.key)
    # print(gottenBook.author)
    # print(gottenBook.title)
    # print(gottenBook.publisher)
    # print(gottenBook.date)
