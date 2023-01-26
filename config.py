import psycopg2
from config import config

def connect():

try:
    connection = None
    params =config()
    print('connect')
    connection = psycopg2.connect(**params)

    #creare un cursore

    curs= connection.cursor()
    print ('PostresSQL database version')
    curs.execute('SELECT version()')
    db_version = curs.fetchone()
    print(db_version)
    curs.close()
except(Exeception,psycopg2.DatabaseError) as Error:
    print(error)
    finally:
        if connection is not None: 
           connection.close()
        print( 'Database connection terminated')
if __name__=="__main__":
    connect()

