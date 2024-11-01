# if user_name and robot_kind has the same, increment count.
# If there are the highest point, recommend the user_name.
import csv
import os
from dialogue import pretty
def recommend():
    # user_name, robot_kindを分析し、一番頻度の高いuser_nameを提案する
    with open('../db/robots_data.csv', 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            # user_name and robot_kindが同じか判定するコードを書く
            max_count = 0
            max_user = ''
            max_kind = ''
            for row in reader:
                user = row['user_name']
                kind = row['robot_kind']
                count = row['count']
                count = int(count)
                if max_count < count:
                    max_count = count
                    max_user = user
                    max_kind = kind
    return  max_user, max_kind, max_count

# r = recommend()
# print(r)

def count():
    """もしcsvファイルがなければ作成し終了する。
    もし、あれば、データからでヘッダーのみを作成してユーザーに返答する。"""
    file = '../db/robots_data.csv'
    r = os.path.isfile(file)
    recommend_user = ''
    recommend_kind = ''
    count = 0
    if r:
        # user_name, robot_kindを分析し、一番頻度の高いuser_nameを提案する
        recommend_user, recommend_kind, count = recommend()
    else:
        with open(file, 'w', newline='') as csv_file:
            fieldnames = ['user_name', 'robot_kind', 'count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        recommnend_user = None
    
    return recommend_user, recommend_kind, count


# count()

