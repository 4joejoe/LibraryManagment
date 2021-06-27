import psycopg2 as db
from db_connect import connect
conn = connect()
def searchByTitle():
    title = input('Enter Book Title: ')
    while title != 0:
        if title == 0:
            break
        else:
            crsr = conn.cursor()
            # query = """SELECT * FROM Books WHERE TO_TSVECTOR(Title) @@ TO_TSQUERY(%(title)s);"""
            # data = (title,)
            crsr.execute( """SELECT * FROM Books WHERE TO_TSVECTOR(Title) @@ TO_TSQUERY(%(title)s)""",{"title":title})
            result = crsr.fetchall()
            # print(result)
            crsr.close()
            for book in result:
                print(f'Title: {book[1]}\nAuthor: {book[2]}\nYear: {book[3]}')
            searchByTitle()
def searchByAuthor():
    author = input('Enter Book Author: ')
    while author != 0:
        if author == 0:
            break
        else:
            crsr = conn.cursor()
            # query = """SELECT * FROM Books WHERE TO_TSVECTOR(Title) @@ TO_TSQUERY(%(title)s);"""
            # data = (title,)
            crsr.execute( """SELECT * FROM Books WHERE TO_TSVECTOR(Author) @@ TO_TSQUERY(%(author)s)""",{"author":author})
            result = crsr.fetchall()
            # print(result)
            crsr.close()
            for book in result:
                print(f'Title: {book[1]}\nAuthor: {book[2]}\nYear: {book[3]}')
            searchByAuthor()
def searchByYear():
    year = int(input('Enter Book Published Year: '))
    while year != 0:
        if year == 0:
            break
        else:
            crsr = conn.cursor()
            # query = """SELECT * FROM Books WHERE TO_TSVECTOR(Title) @@ TO_TSQUERY(%(title)s);"""
            # data = (title,)
            crsr.execute( """SELECT * FROM Books WHERE TO_TSVECTOR(Year) @@ TO_TSQUERY(%(year)s)""",{"year":year})
            result = crsr.fetchall()
            # print(result)
            crsr.close()
            for book in result:
                print(f'Title: {book[1]}\nAuthor: {book[2]}\nYear: {book[3]}')
            searchByAuthor()

