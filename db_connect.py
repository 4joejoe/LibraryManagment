from db_config import config
import psycopg2 as db
def connect():
    conn = None
    try:
        params = config()
        print('Connecting to postgresql database')
        conn = db.connect(**params)
        print('Connected To Database')
        # cursor = conn.cursor()
        # print('Cursor created')
    except(Exception,db.DatabaseError) as err:
        print(err)
    return conn