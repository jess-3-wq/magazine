from lib.models.author import Author
from lib.models.article import Article

def seed():
 
    a1 = Author(name="George Orwell")
    a1.save()

    a2 = Author(name="Virginia Woolf")
    a2.save()

   
    art1 = Article(title="Politics and the English Language", author_id=a1.id, magazine_id=1)
    art1.save()

    art2 = Article(title="The Death of the Moth", author_id=a2.id, magazine_id=2)
    art2.save()

    print("Database seeded!")

if __name__ == "__main__":
    seed()
