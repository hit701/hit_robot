import csv

def data_input():
    name = input('My name is Hit.  What is your name? \n')
    kind_robot = input(f'Hey. {name}. What kind of robot do you like? \n')
    return name, kind_robot

def csv_data(user_name, kind, count):
    #
    with open('../db/robots_data.csv', 'w', newline='') as csv_file:
        fieldnames = ['user_name', 'robot_kind', 'count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'user_name': user_name, 'robot_kind': kind, 'count': count})
        # writer.writerow({'user_name': user_name, 'robot_kind': kind, 'count': count})

count = 2
name = 'H'
kind_robot = 'pretty'
csv_data(name, kind_robot, count)