"""sqlite input"""
from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
#import sqlite3

import sqlalchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = 'jfklxclcoslsll',

    )

def data_input_sql():
    name = input('My name is Hit What is your name? \n')
    if name == '':
        return
    user_name = name.capitalize()

    '''To do recommned program'''

    if user_name:
        # write func sql codes
        sql_data(user_name, 'Hard', 1)
        return

def sql_data(user_name, kind, count):
    conn = sqlite3.connect('../db/ai_sql_lite.db')
    curs = conn.cursor()
    # curs.execute(
    #     f'insert into ais(ai_name, ai_kind, ai_count) values({user_name}, {kind}, {count}'
    # )
    curs.execute(
         'insert into ais(ai_name, ai_kind, ai_count) values("Hiromi", "Pretty", 1)'
    )
    curs.execute('select * from ais')
    print(curs.fetchall())
    r = curs.fetchall()
    for row in r:
        print(row)
    conn.commit()
    curs.close()
    conn.close()

# sql_data('Hiromi', 'Pretty', 1)