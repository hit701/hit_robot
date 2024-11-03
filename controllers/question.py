import csv

def data_input():
    name = input('My name is Hit.  What is your name? \n')
    if name is None:
        return
    name = name.capitalize()
    kind_robot = input(f'Hey. {name}. What charactor of robot would you like? (ex. pretty) \n')
    if kind_robot is None:
        return
    kind_robot = kind_robot.capitalize()
    return name, kind_robot

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