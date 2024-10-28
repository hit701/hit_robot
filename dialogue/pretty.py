"""
Goales
1) ask people What kind of robot you would like
2) memorize the robot name to csv file or any kind of sql(we call them dbs)
3) then, the system show a robot name from the dbs
"""
from controllers import question

def main():
    name, kind = question.data_input()
    question.csv_data(name, kind, 3)
    print('Thak you')


if __name__ == '__main__':
    main()