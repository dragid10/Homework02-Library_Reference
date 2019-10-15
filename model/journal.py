class Journal:
    """
    Class that stores the definition of what it is to be a journal
    """

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
