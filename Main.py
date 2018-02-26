import Settings

"""
Class that stores the definition of what it is to be a book. Simplifies parsing a bit
"""


class Book:
    def __init__(self, key, author, title, publisher, date, type):
        self.key = key
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date
        self.type = type


def parse_book_list(book_list):
    for i in range(0, len(book_list), 6):
        doc_type = book_list[i]
        doc_key = book_list[i + 1][4:].strip().rstrip()
        if "Book" in doc_type:
            Settings.LIBRARY[doc_key.lower()] = Book(
                doc_key,  # Adds Key
                book_list[i + 2][7:].strip().rstrip(),  # Adds author
                book_list[i + 3][7:].strip().rstrip(),  # Adds title
                book_list[i + 4][11:].strip().rstrip(),  # Adds publisher
                book_list[i + 5][6:].strip().rstrip(),  # Adds date
                doc_type.strip().rstrip()
            )
            # print("Book added!")
        elif "Journal" in doc_type:
            print("THIS IS A JOURNAL")


"""
Prints the info for books
"""


def print_book_info(book):
    split_names = book.author.split(" ")
    print('{}\t\t{}, {}, {}, {}, {}.\n'.format(book.key, split_names[1], split_names[0], book.title,
                                               book.publisher, book.date))


"""
Prints the info for journals
"""


def print_journal_info(journal):
    split_names = journal.author.split(" ")
    print('{}\t\t{}, {}, {}, {}, {}.'.format(split_names[1], split_names[0], journal.title,
                                             journal.publisher, journal.date))


def print_conference_info(coference):
    pass


def parse_user_input(key):
    if key not in Settings.LIBRARY:
        print("Book Not found! Please use a valid key\n\n")
    else:
        gotten_doc = Settings.LIBRARY[key]
        if gotten_doc.type == "Book":
            print_book_info(gotten_doc)
        elif gotten_doc.type == "Journal":
            print_journal_info(gotten_doc)
        elif gotten_doc.type == "Conference":
            print_conference_info(gotten_doc)
        else:
            "The programmer must have really messed up to even get to this stage. Sorry fam."


if __name__ == '__main__':
    # The list of books to read in and save
    book_info_list = open("Step1Data.txt").readlines()
    # book_info_list + open("Step2Data.txt").readlines()
    # book_info_list + open("Step3Data.txt").readlines()
    parse_book_list(book_info_list)  # Parse the file and add each book to the dictionary
    print("Database loaded.\n\n\n")

    isRunning = True  # Sets flag in order to be able to break out of the loop
    # gottenBook = Settings.LIBRARY["Rowling1997"]
    # print(gottenBook.key)
    # print(gottenBook.author)
    # print(gottenBook.title)
    # print(gottenBook.publisher)
    # print(gottenBook.date)
    # print_book_info(gottenBook)
    while isRunning:
        key = input("Which document would you like to access? (Or type END to exit the program): ").lower()
        if key == "END" or key == "end":
            isRunning = not isRunning
        else:
            parse_user_input(key)
