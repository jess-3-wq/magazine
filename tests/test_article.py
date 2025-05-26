from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_save_and_find():
    author = Author(name="Geoffery")
    author.save()

    magazine = Magazine(name="Liam", category="Literature")
    magazine.save()

    article = Article(title="Diana", author_id=author.id, magazine_id=magazine.id)
    article.save()

    found = Article.find_by_id(article.id)
    assert found.title == "Diana"
    assert found.author_id == author.id
    assert found.magazine_id == magazine.id
