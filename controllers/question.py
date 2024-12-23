import csv
from controllers import count_and_recommend
from controllers import replace_data

def data_input():
    # まず名前を聞く。推薦する性格を聞く。判断する。なければ、気に入っている性格を聞く。
    name = input('My name is Hit.  What is your name? \n')
    if name == '':
        return
    user_name = name.capitalize()
    name, kind_robot, count, update = count_and_recommend.count('', '')
    # もし、csvファイルに何も入力されていなければ、どんな性格かを聞く。
    if kind_robot == '':
        kind_robot = input(f'Hey. {user_name}. What charactor of AI robot would you like? (ex. pretty) \n')
        kind_robot = kind_robot.capitalize()
        # データが入っていれば、書き込み。append.
        if kind_robot != '':
            csv_data(user_name, kind_robot, 1)
        else:
            return
    else:
        # DBに入っていて、一番、高いデータが良いのかを聞く。
        yes_or_no = input(f'We recommend {kind_robot} charactor AI !.  Do you like? (Yes/y or No/n) \n')
        yes_or_no = yes_or_no.lower()
        if yes_or_no == 'y' or yes_or_no == 'yes':
            user, kind, count_value, update = count_and_recommend.recommend(user_name, kind_robot)
            # もし、user_name, kind_robotが一致するデータがなければ、データを追加する。
            if update == 1:
                csv_data(user_name, kind_robot, 1)
                return
        elif yes_or_no == 'n' or yes_or_no == 'no' or yes_or_no == '':
            kind_robot = input(f'Hey. {user_name}. What charactor of AI robot would you like? (ex. pretty) \n')
            kind_robot = kind_robot.capitalize()
            # DRYの原則でrecommend
            user, kind, count, update = count_and_recommend.recommend(user_name, kind_robot)
            if update == 1:
                csv_data(user_name, kind_robot, 1)
                return
        else:
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