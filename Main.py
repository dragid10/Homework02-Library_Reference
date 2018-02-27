import Settings

"""
Authors: Alex Oladele, Jueru Xie, Kai Li, Mohan Ma
Class: CSE 211
Program to store and retrieve documents using a given key
WRITTEN IN PYTHON 3.5
"""

"""
Class that stores the definition of what it is to be a book
"""

class Book:
    def __init__(self, key, author, title, publisher, date, type):
        self.key = key
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date
        self.type = type


"""
Class that stores the definition of what it is to be a journal
"""


class Journal:
    def __init__(self, key, author, title, journal, publisher, date, volume, number, type):
        self.key = key
        self.author = author
        self.title = title
        self.journal = journal
        self.publisher = publisher
        self.date = date
        self.volume = volume
        self.number = number
        self.type = type


"""
Class that stores the definition of what it is to be a conference
"""


class Conference:
    def __init__(self, key, author, title, conference, date, location, pages, type):
        self.key = key
        self.author = author
        self.title = title
        self.conference = conference
        self.location = location
        self.date = date
        self.pages = pages
        self.type = type


"""
Determines the type of documents in the file and adds them to the library
"""


def parse_document_list(document_list):
    for i in range(0, len(document_list)):  # Iterates through the list via index, in order to make parsing a bit easier
        if ":" not in document_list[i]:  # Makes sure we're processing full documents
            doc_type = document_list[i].strip().rstrip()
            doc_key = document_list[i + 1][4:].strip().rstrip()
            author_list = document_list[i + 2][7:].strip().rstrip().split(",")
            if "Book" in doc_type:
                Settings.LIBRARY[doc_key.lower()] = Book(
                    doc_key,  # Book Key
                    author_list,  # Adds author
                    document_list[i + 3][7:].strip().rstrip(),  # Adds title
                    document_list[i + 4][11:].strip().rstrip(),  # Adds publisher
                    document_list[i + 5][6:].strip().rstrip(),  # Adds date
                    doc_type.strip().rstrip()  # Add doc type
                )
            elif "Journal" in doc_type:
                Settings.LIBRARY[doc_key.lower()] = Journal(
                    doc_key,  # Journal key
                    author_list,  # Adds author
                    document_list[i + 3][7:].strip().rstrip(),  # Adds title
                    document_list[i + 4][9:].strip().rstrip(),  # Adds Journal
                    document_list[i + 5][11:].strip().rstrip(),  # Adds publisher
                    document_list[i + 6][6:].strip().rstrip(),  # Adds date
                    document_list[i + 7][8:].strip().rstrip(),  # Adds Volume
                    document_list[i + 8][8:].strip().rstrip(),  # Adds Number
                    doc_type  # Adds type
                )
            elif "Conference" in doc_type:
                Settings.LIBRARY[doc_key.lower()] = Conference(
                    doc_key,  # Conference key
                    author_list,  # Adds authors
                    document_list[i + 3][7:].strip().rstrip(),  # Adds title
                    document_list[i + 4][12:].strip().rstrip(),  # Adds Conference
                    document_list[i + 5][6:].strip().rstrip(),  # Adds date
                    document_list[i + 6][10:].strip().rstrip(),  # Adds location
                    document_list[i + 7][7:].strip().rstrip(),  # Adds pages
                    doc_type  # Adds type
                )
            else:
                print("I honestly do not know how you even got here. The programmer messed up")  # This should never run
        else:
            continue  # Skips the line b/c its not the start of a document


"""
Iterates through the authors list (if there are multiple), and pre-formats it to be printed
"""


def get_authors(document):
    authors = document.author
    split_name = authors[0].split(" ")  # Gets the first author in order to properly format it
    ret_authors = '{}, {}'.format(split_name[1], split_name[0])

    if len(authors) > 1:  # Formats the rest of the authors, skipping the first one in the list
        for i in range(1, len(authors)):
            ret_authors += ", {}".format(authors[i].strip().rstrip())
    return ret_authors


"""
Prints the info for books
"""

def print_book_info(book):
    authors = get_authors(book)  # Gets the properly formatted authors
    print('{}\t\t{}, {}, {}, {}.\n'.format(book.key, authors, book.title, book.publisher, book.date))


"""
Prints the info for journals
"""

def print_journal_info(journal):
    authors = get_authors(journal)  # Gets the properly formatted authors
    print('{}\t\t{}, {}, {}, {}:{}({}), {}.'.format(journal.key, authors, journal.title, journal.journal,
                                                    journal.publisher, journal.volume, journal.number, journal.date))


def print_conference_info(conference):
    authors = get_authors(conference)  # Gets the properly formatted authors
    print('{}\t\t{}, {} in Proceedings of {}, {}, {}, {}.'.format(conference.key, authors, conference.title,
                                                                  conference.conference, conference.location,
                                                                  conference.date, conference.pages))


"""
Parts the user input based on whatever type the document they're requesting is
"""

def parse_user_input(key):
    if key not in Settings.LIBRARY:
        print("Document Not found! Please use a valid key\n\n")
    else:
        # Prints based on the type of document
        gotten_doc = Settings.LIBRARY[key]
        if gotten_doc.type == "Book":
            print_book_info(gotten_doc)
        elif gotten_doc.type == "Journal":
            print_journal_info(gotten_doc)
        elif gotten_doc.type == "Conference":
            print_conference_info(gotten_doc)
        else:
            "The programmer must have really messed up to even get to this stage. Sorry fam."


"""
The main method of the program
"""

if __name__ == '__main__':
    # The list of books to read in and save
    book_info_list = open("Step3Data.txt").readlines()
    parse_document_list(book_info_list)  # Parse the file and add each book to the dictionary

    isRunning = True  # Sets flag in order to be able to break out of the loop
    while isRunning:
        key = input("Which document would you like to access? (Or type END to exit the program): ").lower()
        if key == "END" or key == "end":  # ends program is user choses to do so
            isRunning = not isRunning
        else:
            parse_user_input(key)  # parses key user inputs
