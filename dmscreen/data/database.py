import sqlite3
import os
from sqlite3 import Error
from dmscreen.util.singleton import Singleton
dir_ = os.path.dirname(__file__)
filename = os.path.join(dir_, 'db.sqlite')

sql_create_ability_score_table = """ CREATE TABLE IF NOT EXISTS ability_score_set (
                                        id integer PRIMARY KEY,
                                        set_id integer NOT NULL,
                                        strength integer NOT NULL,
                                        dexterity integer NOT NULL,
                                        constitution integer NOT NULL,
                                        intelligence integer NOT NULL,
                                        wisdom integer NOT NULL,
                                        charisma integer NOT NULL
                                    ); """

sql_create_skills_table = """ CREATE TABLE IF NOT EXISTS skill_set (
                                        id integer PRIMARY KEY,
                                        set_id integer NOT NULL,
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

sql_create_character_table = """ CREATE TABLE IF NOT EXISTS character (
                                        id integer PRIMARY KEY,
                                        class_set_id integer NOT NULL,
                                        race_id integer NOT NULL,
                                        level integer NOT NULL,
                                        armor_id integer NOT NULL,
                                        ability_score_id integer NOT NULL,
                                        skills_id integer NOT NULL,
                                        hit_points_id integer NOT NULL,
                                        alignment integer NOT NULL,
                                        languages_id integer NOT NULL,
                                        spell_set_id integer NOT NULL
                                    ); """

sql_create_spell_set_table = """ CREATE TABLE IF NOT EXISTS spell_set (
                                        id integer PRIMARY KEY,
                                        set_id integer NOT NULL,
                                        spell_id integer NOT NULL
                                    ); """


class DatabaseConnector(metaclass=Singleton):
    conn = None

    def create_connection(self):
        """ create a database connection to SQLite database """
        try:
            self.conn = sqlite3.connect(filename)
            self.conn.row_factory = sqlite3.Row
            self.create_table(sql_create_spell_set_table)
            self.create_table(sql_create_ability_score_table)
            self.create_table(sql_create_skills_table)
            self.create_table(sql_create_character_table)
            print("create spell set")
        except Error as e:
            print(e)

    def create_table(self, create_table_sql):
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_ability_score_set(self, ability_score_set):
        sql = ''' INSERT INTO ability_score_set(strength, dexterity, constitution, intelligence,
                                                wisdom, charisma)
              VALUES(?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, ability_score_set)
        self.conn.commit()

    def create_character_class(self, character_class):
        sql = ''' INSERT INTO character_class(class, level)
              VALUES(?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, character_class)
        self.conn.commit()

    def create_character(self, character):
        sql = ''' INSERT INTO character(class_set_id, race_id, level, armor_id,
                                        ability_score_id, skills_id, hit_points_id,
                                        alignment, languages_id, spell_set_id)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, character)
        self.conn.commit()

    def select_character_by_id(self, id_):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM character WHERE id=?", (id_,))
        row = cur.fetchone()
        return row

    def select_spells_by_set_id(self, set_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM spell_set WHERE set_id=?", (set_id,))
        rows = cur.fetchall()
        for row in rows:
            print(row[1])

    def create_spell(self, spell):
        sql = ''' INSERT INTO spell_set(set_id, spell_id)
              VALUES(?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, spell)
        self.conn.commit()

    def create_character_class_set(self, character_class_set):
        sql = ''' INSERT INTO character_class_set(set_id, class_id)
              VALUES(?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, character_class_set)
        self.conn.commit()

    def create_skill_set(self, ability_score_set):
        sql = ''' INSERT INTO skill_set(acrobatics, animal_handling, arcana, athletics, deception,
                                        history, insight, intimidation, ivestigation, medicine,
                                        nature, perception, performance, persuasion, religion,
                                        sleight_of_hand, stealth, survival)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, ability_score_set)
        self.conn.commit()
