class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise ValueError("Title must be a string of 5 to 50 characters.")
        self.__title = title
        self.author = author
        self.magazine = magazine
        author.add_article(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author class.")
        self.__author = value

    @property
    def magazine(self):
        return self.__magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine class.")
        self.__magazine = value
