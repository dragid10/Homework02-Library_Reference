import settings
from model.book import Book
from model.conference import Conference
from model.journal import Journal


def parse_document_list(document_list):
    """
    Determines the type of documents in the file and adds them to the library
    """
    for i in range(0, len(
            document_list)):  # Iterates through the list via index, in order to make parsing a bit easier
        if ":" not in document_list[i]:  # Makes sure we're processing full documents
            doc_type = document_list[i].strip().rstrip()
            doc_key = document_list[i + 1][4:].strip().rstrip()
            author_list = document_list[i + 2][7:].strip().rstrip().split(",")
            if "Book".lower() in doc_type.lower():
                settings.LIBRARY[doc_key.lower()] = Book(
                    doc_key,  # Book Key
                    author_list,  # Adds author
                    document_list[i + 3][7:].strip().rstrip(),  # Adds title
                    document_list[i + 4][11:].strip().rstrip(),  # Adds publisher
                    document_list[i + 5][6:].strip().rstrip(),  # Adds date
                    doc_type.strip().rstrip()  # Add doc type
                )
            elif "Journal".lower() in doc_type.lower():
                settings.LIBRARY[doc_key.lower()] = Journal(
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
            elif "Conference".lower() in doc_type.lower():
                settings.LIBRARY[doc_key.lower()] = Conference(
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
                print(
                    f"One of the documents in the list is not a recognized type. Document type: {doc_type}; With key: {doc_key}")
        else:
            continue  # Skips the line b/c its not the start of a document


def get_authors(document):
    """
    Iterates through the authors list (if there are multiple), and pre-formats it to be printed
    """
    authors = document.author
    split_name = authors[0].split(" ")  # Gets the first author in order to properly format it
    ret_authors = f"{split_name[1]}, {split_name[0]}"

    if len(authors) > 1:  # Formats the rest of the authors, skipping the first one in the list
        for i in range(1, len(authors)):
            ret_authors += f", {authors[i].strip().rstrip()}"
    return ret_authors


def print_book_info(book):
    """
    Prints the info for books
    """
    authors = get_authors(book)  # Gets the properly formatted authors
    print(f"{book.key}\t\t{authors}, {book.title}, {book.publisher}, {book.date}.\n")


def print_journal_info(journal):
    """
    Prints the info for journals
    """
    authors = get_authors(journal)  # Gets the properly formatted authors
    print(
        f"{journal.key}\t\t{authors}, {journal.title}, {journal.journal}, {journal.publisher}:{journal.volume}({journal.number}), {journal.date}.")


def print_conference_info(conference):
    """
    Prints the info for conferences
    """
    authors = get_authors(conference)  # Gets the properly formatted authors
    print(
        f"{conference.key}\t\t{authors}, {conference.title} in Proceedings of {conference.conference}, {conference.location}, {conference.date}, {conference.pages}.")


def parse_user_input(key):
    """
    Parses the user input based on whatever type the document they're requesting is
    """
    if key.lower() not in settings.LIBRARY:
        print("Document Not found! Please use a valid key\n\n")
    else:
        # Prints based on the type of document
        gotten_doc = settings.LIBRARY[key.lower()]
        if gotten_doc.type.lower() == "Book".lower():
            print_book_info(gotten_doc)
        elif gotten_doc.type.lower() == "Journal".lower():
            print_journal_info(gotten_doc)
        elif gotten_doc.type.lower() == "Conference".lower():
            print_conference_info(gotten_doc)
        else:
            print(f"The document requested is not of a supported type")
