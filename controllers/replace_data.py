import csv
import controllers.question

file_name = '../db/robots_data.csv'

# reader = read_csv(file_name)
fieldnames = ['user_name', 'robot_kind', 'count']

# 部分的にcountのみを更新したいがseekを使うため保留
# メモリにデータを一時保存するため、大量データを扱えない。
# SQLを使うほうが良いかもしれない。
menu_dic = {}
def update_csv():
    with open(file_name, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            menu_dic.update({row['user_name'] + ',' + row['robot_kind']: int(row['count'])})


def write_update(user_name, robot_kind):
    update_csv()
    # 更新するが、全部変えて更新する方法
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in menu_dic.items():
            key_list = key.split(',')
            user = key_list[0]
            kind = key_list[1]
            if user == user_name and kind == robot_kind:
                value += 1
                writer.writerow({'user_name': user, 'robot_kind': kind, 'count': value})
                continue
            else:
                writer.writerow({'user_name': user, 'robot_kind': kind, 'count': value})


user = 'Hitoshi'
kind = 'Strong'
count = 1
# controllers.question.csv_data(user, kind, count)
# write_update('Yuto', 'Kind')