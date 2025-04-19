import sqlite3
class Database:

    def __init__(self,dbname):
        self.conn=sqlite3.connect(dbname)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id_book INTEGER PRIMARY KEY, title_book TEXT,author_book TEXT,year_publication_book INTEGER,isbn_book INTEGER)")
        self.conn.commit()
        


    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows=self.cur.fetchall()
    
        return(rows)
        
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title_book=? OR author_book=? OR year_publication_book=? OR isbn_book=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
 
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM books WHERE id_book=?",(id,))
        self.conn.commit()
  

    def update(self,id, title="", author="", year="", isbn=""):
        self.cur.execute("UPDATE books SET title_book=?, author_book=?, year_publication_book=?, isbn_book=? WHERE id_book=?", (title, author, year, isbn, id))
        self.conn.commit()

# metodo destructor
def __del__(self):
    self.conn.close()




