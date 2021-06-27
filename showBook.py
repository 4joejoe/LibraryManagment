import psycopg2 as db
from db_connect import connect
conn = connect()
def showBook():
    crsr = conn.cursor()
    # print('Crusor Created')
    crsr.execute("SELECT * FROM Books;")
    books = crsr.fetchall()
    for book in books:
        print(f'Title: {book[1]}\nAuthor: {book[2]}\nYear: {book[3]}')

# showBook()
