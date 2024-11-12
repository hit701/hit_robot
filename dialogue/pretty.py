"""
Goales
1) ask people What kind of robot you would like
2) memorize the robot name to csv file or any kind of sql(we call them dbs)
3) then, the system show a robot name from the dbs
"""
import csv
import os
import sqlite3

from controllers import question


def main():
    """This ここはMVC modelのViewに相当"""
    question.data_input()
    print('Thank you for visiting our site! See you again! ')


if __name__ == '__main__':
    # csvファイルがdbフォルダにあるか否かを判定、なければ、作成。
    csv_file = '../db/robots_data.csv'
    is_csv = os.path.isfile(csv_file)
    sql_lite_db = '../db/ai_sql_lite.db'
    is_sql_lite = os.path.isfile(sql_lite_db)
    if is_csv is False:
        with open('../db/robots_data.csv', 'w', newline='') as csv_file:
            fieldnames = ['user_name', 'robot_kind', 'count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
    print(is_sql_lite)
    if is_sql_lite is False:
        conn = sqlite3.connect(sql_lite_db)
        curs = conn.cursor()
        curs.execute(
            'create table ais(id integer primary key autoincrement, ai_name string, ai_kind string, ai_count int)'
        )
        curs.execute(
            'insert into ais(ai_name, ai_kind, ai_count) values("Yuto", "Kind", 1)'
        )
        conn.commit()
        curs.close()
        conn.close()
    main()
