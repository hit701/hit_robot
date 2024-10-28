# if user_name and robot_kind has the same, increment count.
# If there are the highest point, recommend the user_name.
import csv
import os
def recommend():
    # user_name, robot_kindを分析し、一番頻度の高いuser_nameを提案する
    with open('../db/robots_data.csv', 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(row['user_name'], row['robot_kind'], row['count'])
    # return user_name, count

def count():
    """もしcsvファイルがなければ作成し終了する。
    もし、あれば、データがからでヘッダーのみを作成してユーザーに返答する。"""
    file = '../db/robots_data.csv'
    r = os.path.isfile(file)
    if r:
        # user_name, robot_kindを分析し、一番頻度の高いuser_nameを提案する
        recommend()
    else:
        with open(file, 'w', newline='') as csv_file:
            fieldnames = ['user_name', 'robot_kind', 'count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
    
    return

count()

