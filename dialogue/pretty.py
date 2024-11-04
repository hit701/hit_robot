"""
Goales
1) ask people What kind of robot you would like
2) memorize the robot name to csv file or any kind of sql(we call them dbs)
3) then, the system show a robot name from the dbs
"""
import csv
import os

from controllers import question
from controllers import count_and_recommend
from controllers import replace_data
def main():
    """This ここはMVC modelのViewに相当j"""
    question.data_input()
    print('Thank you for visiting our site! See you again! ')


if __name__ == '__main__':
    # csvファイルがdbフォルダにあるか否かを判定、なければ、作成。
    file = '../db/robots_data.csv'
    r = os.path.isfile(file)
    if r is False:
        with open('../db/robots_data.csv', 'w', newline='') as csv_file:
            fieldnames = ['user_name', 'robot_kind', 'count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
    main()