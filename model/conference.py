class Conference:
    """
    Class that stores the definition of what it is to be a conference
    """

    def __init__(self, key, author, title, conference, date, location, pages, type):
        self.key = key
        self.author = author
        self.title = title
        self.conference = conference
        self.location = location
        self.date = date
        self.pages = pages
        self.type = type
