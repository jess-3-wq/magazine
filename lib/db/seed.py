from lib.models.author import Author
from lib.models.article import Article

def seed():
 
    a1 = Author(name="Greg Saita")
    a1.save()

    a2 = Author(name="Mutali Chesebe")
    a2.save()

   
    art1 = Article(title="My life in crime", author_id=a1.id, magazine_id=1)
    art1.save()

    art2 = Article(title="The Diary of a Wimpy kid", author_id=a2.id, magazine_id=2)
    art2.save()

    print("Magazine seeded!")

if __name__ == "__main__":
    seed()
