class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.__name = name
        self.__articles = []

    @property
    def name(self):
        return self.__name

    def add_article(self, article):
        if article not in self.__articles:
            self.__articles.append(article)

    def articles(self):
        return self.__articles

    def magazines(self):
        return list(set(article.magazine for article in self.__articles))
