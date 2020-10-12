import sqlite3
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'db.sqlite')

from sqlite3 import Error

sql_create_ability_score_table = """ CREATE TABLE IF NOT EXISTS ability_score_set (
                                        id integer PRIMARY KEY,
                                        strength integer NOT NULL,
                                        dexterity integer NOT NULL,
                                        constitution integer NOT NULL,
                                        intelligence integer NOT NULL,
                                        wisdom integer NOT NULL,
                                        charisma integer NOT NULL
                                    ); """

sql_create_skills_table = """ CREATE TABLE IF NOT EXISTS skill_set (
                                        id integer PRIMARY KEY,
                                        acrobatics integer NOT NULL,
                                        animal_handling integer NOT NULL,
                                        arcana integer NOT NULL,
                                        athletics integer NOT NULL,
                                        deception integer NOT NULL,
                                        history integer NOT NULL,
                                        insight integer NOT NULL,
                                        intimidation integer NOT NULL,
                                        ivestigation integer NOT NULL,
                                        medicine integer NOT NULL,
                                        nature integer NOT NULL,
                                        perception integer NOT NULL,
                                        performance integer NOT NULL,
                                        persuasion integer NOT NULL,
                                        religion integer NOT NULL,
                                        sleight_of_hand integer NOT NULL,
                                        stealth integer NOT NULL,
                                        survival integer NOT NULL
                                    ); """

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

    def create_skill_set(self, ability_score_set):
        sql = ''' INSERT INTO skill_set(acrobatics,animal_handling,arcana,athletics,deception,history,
              insight,intimidation,ivestigation,medicine,nature,perception,performance,persuasion,religion,sleight_of_hand,stealth,survival)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, ability_score_set)
        self.conn.commit()
