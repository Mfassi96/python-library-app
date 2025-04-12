import sqlite3

def connect():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id_book INTEGER PRIMARY KEY, title_book TEXT,author_book TEXT,year_publication_book INTEGER,isbn_book INTEGER)")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return(rows)
    
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title_book=? OR author_book=? OR year_publication_book=? OR isbn_book=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE id_book=?",(id,))
    conn.commit()
    conn.close()

def update(id, title="", author="", year="", isbn=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET title_book=?, author_book=?, year_publication_book=?, isbn_book=? WHERE id_book=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
#insert("demo","demo",2025,1245)
#print(view())

update(2,'test')