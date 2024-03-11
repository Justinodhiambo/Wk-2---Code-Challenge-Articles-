from magazine import Author, Article, Magazine

def test_magazine_initialization():
    magazine = Magazine("Global Science", "Science")
    assert magazine.name == "Global Science", "Magazine's name should be initialized correctly"
    assert magazine.category == "Science", "Magazine's category should be initialized correctly"

def test_magazine_add_article():
    author = Author("Neil Armstrong")
    magazine = Magazine("Space Today", "Space Exploration")
    Article(author, magazine, "A Walk on the Moon")
    assert len(magazine.articles()) == 1, "Magazine should have one article added"

def test_magazine_contributors():
    author1 = Author("Albert Einstein")
    author2 = Author("Isaac Newton")
    magazine = Magazine("Physics Monthly", "Physics")
    Article(author1, magazine, "Theory of Relativity")
    Article(author2, magazine, "Laws of Motion")
    assert len(magazine.contributors()) == 2, "Magazine should have two unique contributors"
