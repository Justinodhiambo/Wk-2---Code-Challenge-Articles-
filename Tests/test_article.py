from your_module import Author, Article, Magazine  # Adjust the import path as necessary

def test_author_initialization():
    author = Author("John Doe")
    assert author.name == "John Doe", "Author's name should be initialized correctly"

def test_author_add_article():
    author = Author("Jane Doe")
    magazine = Magazine("Tech Trends", "Technology")
    article = Article(author, magazine, "The Future of Tech")
    assert article in author.articles(), "Article should be added to the author's list of articles"

def test_author_magazines():
    author = Author("Emily Bronte")
    magazine1 = Magazine("Literary Wonders", "Literature")
    magazine2 = Magazine("Modern Lit", "Literature")
    Article(author, magazine1, "Wuthering Heights Revisited")
    Article(author, magazine2, "The Tale of Two Cities: A Modern Review")
    assert len(author.magazines()) == 2, "Author should have articles in 2 unique magazines"
