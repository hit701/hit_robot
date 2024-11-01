import csv

def replace_data(user, kind):
    with open('../db/robots_data.csv', 'r', newline='') as csv_file_read:
        reader = csv.DictReader(csv_file_read)
        with open('../db/robots_data.csv', 'w', newline='') as csv_file_write:
            writer = csv.DictWriter(csv_file_write)
            writer.writerow(['user_name'], ['robot_kind'], ['count'])
            for row in reader:
                if user == row['user_name'] and kind == row['robot_kind']:
                    row['count'] += 1
                    break


