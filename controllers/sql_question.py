"""sqlite input"""
import sqlite3

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite')

conn = sqlite3.connect('../db/ai_sql_lite.db')
curs = conn.cursor()

def data_input_sql():
    name = input('My name is Hit What is your name? \n')
    if name == '':
        return
    user_name = name.capitalize()

    '''To do recommned program'''

    if user_name:
        # write func sql codes
        pass