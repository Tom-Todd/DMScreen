import sqlite3
from sqlite3 import Error

class database_connector():

    conn = None

    def create_connection(db_file):
        """ create a database connection to SQLite database """
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn
