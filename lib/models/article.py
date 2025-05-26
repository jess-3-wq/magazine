from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id,id=None):

        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id= magazine_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?", (self.title, self.author_id, self.magazine_id, self.id))
        else:
            cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",(self.title, self.author_id, self.magazine_id) )        
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls (id = row[0], title=row[1], author_id=row[2], magazine_id=row[3] ) if row else None     

def __repr__(self):
    return f"<Article {self.id}: {self.title}>"           