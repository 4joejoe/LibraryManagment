from configparser import Error
from db_connect import connect
import psycopg2 as db
conn = connect()
def createTable(tableName):
    try:
        crsr = conn.cursor()
        # crsr.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc"))
        crsr.execute("""CREATE TABLE Books (ID VARCHAR(32), Title VARCHAR(200), Author VARCHAR(200),Year INTEGER)""")
        cmt = conn.commit()
        print("Table Created")
    except(Exception, db.DatabaseError) as err:
        print(err)

if __name__ == "__main__":
    createTable("Books")