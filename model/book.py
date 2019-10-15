class Book:
    """
    Class that stores the definition of what it is to be a book
    """

    def __init__(self, key, author, title, publisher, date, type):
        self.key = key
        self.author = author
        self.title = title
        self.publisher = publisher
        self.date = date
        self.type = type
