class Student:
    pass


import csv
from user import User
from student import Student
from teacher import Teacher
from voca import Voca

while True:

    hi = input(print('로그인 1, 회원가입 2, 비밀번호 찾기 3, 프로그램 종료 4'))
    users = []

    if hi == 1:
        mail = input(print('e-mail: '))
        pw = input(print('password: '))

        f = open("user.csv", "r", newline="", encoding='utf-8')
        fr = csv.reader(f)
        user_info_list = []
        count = 0
        for line in fr:
            user_info_list.append(line)
            count += 1
        f.close()

        for i in range(count):
            if mail == user_info_list[i][0]:
                if pw == user_info_list[i][1]:
                    login_user = User()
                    login_user(mail, pw, user_info_list[i][2], user_info_list[i][3])
                    users.append(login_user)

                    print('Welcome 2 ma home')
                    for n in range(len(users)):
                        print(users[n].getname)

                    if user_info_list[i][3] == 'student':
                        mode = input(print('sutdy or logout: '))

                        if mode == 'logout':
                            users.pop()

                    if user_info_list[i][3] == 'teacher':
                        mode = input(print('make_exam or logout: '))

                        if mode == 'logout':
                            users.pop()

    elif hi == 2:
        imsi_user_info_list = []

        mail = input(print('e-mail: '))
        pw = input(print('password: '))
        name = input(print('name: '))
        who = input(print('are you student or teacher: '))

        imsi_user_info_list.append(mail, pw, name, who)

        f = open("user.csv", "w", newline="", encoding='utf-8')
        fw = csv.writer(f)
        fw.writerow(user_info_list)
        f.close()



    elif hi == 3:
        mail = input(print('e-mail: '))
        name = input(print('name: '))

        f = open("user.csv", "r", newline="", encoding='utf-8')
        fr = csv.reader(f)
        user_info_list = []
        count = 0
        for line in fr:
            user_info_list.append(line)
            count += 1
        f.close()

        for i in range(count):
            if mail == user_info_list[i][0]:
                if name == user_info_list[i][2]:
                    print(
                        f'This is your password: {user_info_list[i][1][:int(len(user_info_list[i][1]) / 2)]}{"*" * int(len(user_info_list[i][1]))}')

        print("You are wrong")




    else:
        exit()
