import csv
from controllers import count_and_recommend
from controllers import replace_data

def data_input():
    # まず名前を聞く。推薦する性格を聞く。判断する。なければ、気に入っている性格を聞く。
    name = input('My name is Hit.  What is your name? \n')
    if name is None:
        return
    user_name = name.capitalize()
    name, kind_robot, count = count_and_recommend.count('', '')
    if kind_robot == '':
        kind_robot = input(f'Hey. {user_name}. What charactor of AI robot would you like? (ex. pretty) \n')
        kind_robot = kind_robot.capitalize()
        if kind_robot != '':
            csv_data(user_name, kind_robot, 1)
        else:
            return
    else:
        yes_or_no = input(f'We recommend {kind_robot} charactor.  do you like? (Yes/y or No/n) \n')
        yes_or_no = yes_or_no.lower()
        if yes_or_no == 'y' or yes_or_no == 'yes':
            replace_data.write_update(name, kind_robot)
            return
        elif yes_or_no == 'n' or yes_or_no == 'no' or yes_or_no == '':
            kind_robot = input(f'Hey. {user_name}. What charactor of AI robot would you like? (ex. pretty) \n')
            kind_robot = kind_robot.capitalize()
            user, kind, count = count_and_recommend.recommend(user_name, kind_robot)
            if count != 0:
                csv_data(user_name, kind_robot, 1)
                return
            else:
                replace_data.write_update(user_name, kind_robot)
                return
        # else:
        #     csv_data(user_name, kind_robot, 1)
        #     return

def csv_data(user_name, kind, count):
    #
    with open('../db/robots_data.csv', 'a', newline='') as csv_file:
        fieldnames = ['user_name', 'robot_kind', 'count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # For the first time, you use 'w' mode. Use writeheader().
        # writer.writeheader()
         #if something
        writer.writerow({'user_name': user_name, 'robot_kind': kind, 'count': count})
        # writer.writerow({'user_name': user_name, 'robot_kind': kind, 'count': count})
#
# seek_position = 2
# count = 2
# name = 'H'
# kind_robot = 'pretty'
# csv_data(name, kind_robot, count, seek_position)