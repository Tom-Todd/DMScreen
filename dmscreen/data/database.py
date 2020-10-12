import sqlite3
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'db.sqlite')

from sqlite3 import Error

class DatabaseConnector():
    conn = None

    def create_connection():
        """ create a database connection to SQLite database """
        try:
            conn = sqlite3.connect(filename)
        except Error as e:
            print(e)

    def create_table():
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
