import sqlite3
from sqlite3 import Error
import os

database_path = os.path.abspath(os.path.dirname('create_database.py'))
db_path = database_path+"\dashboard_db.db"

def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_connection(db_path)