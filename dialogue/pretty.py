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
    user_name, robot_kind = question.data_input()
    if user_name is None or robot_kind is None:
        print('Thank you')
        return
    elif user_name and robot_kind:
        question.csv_data(user_name, robot_kind, 1)
        print('Thank you')
    else:
        user, kind, count = count_and_recommend.count()
        yes_or_no = input(f'We recommend {user} robot and {kind} kind.  do you like? ')
        yes_or_no = yes_or_no.lower()
        if yes_or_no == 'y' or yes_or_no == 'yes':
            replace_data.write_update(user, kind)

        # user, count = count_and_recommend.recommend(user_name, robot_kind)

        elif yes_or_no == 'n' or yes_or_no == 'no':
            user, kind = question.data_input()
            question.csv_data(user, kind, 1)
            print('Thank you')
            return
        else:
            print('Thank you')


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