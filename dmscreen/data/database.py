import sqlite3
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'db.sqlite')

from sqlite3 import Error

class DatabaseConnector():
    conn = None

    def create_connection(self):
        """ create a database connection to SQLite database """
        try:
            self.conn = sqlite3.connect(filename)
        except Error as e:
            print(e)

    def create_table(self, create_table_sql):
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_ability_score_set(self, ability_score_set):
        sql = ''' INSERT INTO ability_score_set(strength,dexterity,constitution,intelligence,wisdom,charisma)
              VALUES(?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, ability_score_set)
        self.conn.commit()
