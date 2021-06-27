import uuid
import psycopg2 as db
from db_connect import connect
conn = connect()
def add_book():
    try:
        id = uuid.uuid4().hex
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        published_year = input('Published Year: ')
    except:
        print('Error in input block')

    return (id,title,author,published_year)

def add_to_db():
    try:
        crsr = conn.cursor()
        query = "INSERT INTO Books (id,title,author,year) VALUES (%s,%s,%s,%s);"
        data = add_book()
        crsr.execute(query,data)  
        cmt = conn.commit()
        crsr.close()
        print('Book Added')
        # print(crsr.fetchone())
    except(Exception,db.DatabaseError) as err:
        print(err)
if __name__ == '__main__':
    add_to_db()