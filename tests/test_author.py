from lib.models.author import Author

def test_author_save_and_find():
    author = Author(name="Jeff Koinange")
    author.save()

    assert author.id is not None

    found = Author.find_by_id(author.id)
    assert found.name == "Jeff Koinange"
