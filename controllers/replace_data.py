import csv
file_name = '../db/robots_data.csv'

# reader = read_csv(file_name)
fieldnames = ['user_name', 'robot_kind', 'count']

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
                # value = int(3)
                # writer.writerow({'user_name': user, 'robot_kind': kind, 'count': value})

# write_update('Yuto', 'Kind')