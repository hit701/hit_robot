# if user_name and robot_kind has the same, increment count.
# If there are the highest point, recommend the user_name.
import csv
from controllers import question

from controllers import replace_data
from dialogue import pretty


def recommend(user_name, robot_kind):
    # user_name, robot_kindを分析し、一番頻度の高いuser_nameを提案する
    # 性格の推薦、user_name, robot_kindが一致した場合のデータの更新
    # question.py, data_input()にてupdateフラッグを追加。
    with open('../db/robots_data.csv', 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            # user_name and robot_kindが同じか判定するコードを書く
            max_count = 0
            max_user = ''
            max_kind = ''
            update = 1
            for row in reader:
                user = row['user_name']
                kind = row['robot_kind']
                count = row['count']
                count = int(count)
                if user_name == user and robot_kind == kind:
                    replace_data.write_update(user_name, robot_kind)
                    update = 0
                    break
                else:
                    if max_count < count:
                        max_count = count
                        max_user = user
                        max_kind = kind
    return  max_user, max_kind, max_count, update

# r = recommend()
# jprint(r)

def count(user_name, robot_kind):
    """もしcsvファイルがなければ作成し終了する。
    もし、あれば、データからでヘッダーのみを作成してユーザーに返答する。"""
    recommend_user, recommend_kind, count, update = recommend(user_name, robot_kind)

    return recommend_user, recommend_kind, count, update


# count()

