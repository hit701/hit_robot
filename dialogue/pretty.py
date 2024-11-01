"""
Goales
1) ask people What kind of robot you would like
2) memorize the robot name to csv file or any kind of sql(we call them dbs)
3) then, the system show a robot name from the dbs
"""
from controllers import question
from controllers import count_and_recommend
from controllers import replace_data
def main():
    """This ここはMVC modelのViewに相当j"""
    user_name, robot_kind = question.data_input()
    if user_name is None or robot_kind is None:
        print('Thank you')
        return
    else:
        user, kind, count = count_and_recommend.count()
        yes_or_no = input(f'We recommend {user} robot and {kind} kind.  do you like? ')
        yes_or_no = yes_or_no.lower()
        if yes_or_no == 'y' or yes_or_no == 'yes':
            replace_data.replace_data(user, kind)

        # user, count = count_and_recommend.recommend(user_name, robot_kind)
            question.csv_data(user, kind, count)
            print('Thank you')
            return
        else:
            print('Thank you')


if __name__ == '__main__':
    main()