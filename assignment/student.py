if __name__ == '__main__':

    import csv
    import random
    from user import User
    from voca import Voca

    while True:

        hi = int(input('로그인 1, 회원가입 2, 비밀번호 찾기 3, 프로그램 종료 4: '))
        users = []

        if hi == 1:
            mail = input('e-mail: ')
            pw = input('password: ')

            f = open("user.csv", "r", newline="", encoding='utf-8')
            fr = csv.reader(f)
            user_info_list = []
            count = 0
            for line in fr:
                user_info_list.append(line)
                count += 1
            f.close()

            for i in range(count):
                if (mail == user_info_list[i][0]) and (pw == user_info_list[i][1]):
                    login_user = User(mail, pw, user_info_list[i][2], user_info_list[i][3])
                    users.append(login_user)

                    print('Welcome 2 ma home')
                    for n in range(len(users)):
                        print(users[n].get_name)

                    if login_user.get_who() == 'student':
                        mode = input('sutdy or logout: ')

                        while True:
                            if mode == 'study':
                                what = int(input('다 외운 단어 재시험(1), 자주 틀리는 단어 재시험(2), 일반 시험(3), 단어장 종료(0) 중 하나를 선택하세요: '))

                                if what == 1:
                                    result_num = 0
                                    results = []
                                    f = open(f"{login_user.get_name}_voca.csv", "r", encoding='utf-8')
                                    fr = csv.reader(f)
                                    for result in fr:
                                        result_num += 1
                                        result_num = Voca(result[0], result[1])
                                        if result_num.get_count == -1:
                                            results.append(result_num)
                                        f.close()

                                    for k in range(len(results)):
                                        rand_num = random.randrange(0, len(results))
                                        answer = input(f"{results[k].get_eng}의 뜻을 쓰세요: ")

                                        if answer == results[k].get_kor:
                                            results[k].set_count(-1)
                                            print("맞았습니다!")

                                        elif answer == "시험 끝":
                                            cf = open(f"{login_user.get_name}_voca.csv", "w", encoding='utf-8')
                                            cfw = csv.writer(cf)
                                            for n in range(len(results)):
                                                renew_test_result = []
                                                renew_test_result.append(results[n].get_eng)
                                                renew_test_result.append(results[n].get_kor)
                                                renew_test_result.append(results[n].get_count)
                                                cfw.writerow(renew_test_result)
                                            print("시험이 끝났습니다.")
                                            break

                                        else:
                                            results[k].set_count(1)
                                            print("틀렸습니다!")

                                if what == 2:
                                    result_num = 0
                                    results = []
                                    f = open(f"{login_user.get_name}_voca.csv", "r", encoding='utf-8')
                                    fr = csv.reader(f)
                                    for result in fr:
                                        result_num += 1
                                        result_num = Voca(result[0], result[1])
                                        if result_num.get_count >= 0:
                                            results.append(result_num)
                                        f.close()

                                    for k in range(len(results)):
                                        rand_num = random.randrange(0, len(results))
                                        answer = input(f"{results[k].get_eng}의 뜻을 쓰세요: ")

                                        if answer == results[k].get_kor:
                                            results[k].set_count(-1)
                                            print("맞았습니다!")

                                        elif answer == "시험 끝":
                                            cf = open(f"{login_user.get_name}_voca.csv", "w", encoding='utf-8')
                                            cfw = csv.writer(cf)
                                            for n in range(len(results)):
                                                renew_test_result = []
                                                renew_test_result.append(results[n].get_eng)
                                                renew_test_result.append(results[n].get_kor)
                                                renew_test_result.append(results[n].get_count)
                                                cfw.writerow(renew_test_result)
                                            print("시험이 끝났습니다.")
                                            break

                                        else:
                                            results[k].set_count(1)
                                            print("틀렸습니다!")

                                if what == 3:
                                    vocas = []
                                    vocaf = open("voca.csv", "r", encoding='utf-8')
                                    vocafr = csv.reader(vocaf)
                                    for voca in vocafr:
                                        voca_obj = Voca(voca[0], voca[1])
                                        vocas.append(voca_obj)
                                    vocaf.close()

                                    while True:
                                        rand_num = random.randrange(0, len(vocas))
                                        answer = input(f"{vocas[rand_num].get_eng}의 뜻을 쓰세요: ")

                                        if answer == vocas[rand_num].get_kor:
                                            vocas[rand_num].set_count(-1)
                                            print("맞았습니다!")

                                        elif answer == "시험 끝":
                                            cf = open(f"{login_user.get_name}_voca.csv", "w", encoding='utf-8')
                                            cfw = csv.writer(cf)
                                            for n in range(len(vocas)):
                                                test_result = []
                                                test_result.append(vocas[n].get_eng)
                                                test_result.append(vocas[n].get_kor)
                                                test_result.append(vocas[n].get_count)
                                                cfw.writerow(test_result)
                                            print("시험이 끝났습니다.")
                                            break

                                        else:
                                            vocas[rand_num].set_count(1)
                                            print("틀렸습니다!")

                                else:
                                    break

                            if mode == 'logout':
                                users.remove(login_user)

                    if login_user.get_who() == 'teacher':
                        mode = input('make exam or logout: ')

                        while True:
                            if mode == 'make exam':
                                what = int(input('입력모드(1), 단어장 종료(0) 중 하나를 선택하세요: '))
                                if what == 1:
                                    f = open("voca.csv", "a", newline="", encoding='utf-8')
                                    fw = csv.writer(f)
                                    while True:
                                        word = []
                                        eng = input("영단어를 입력하세요: ")
                                        if eng == "exit":
                                            f.close()
                                            break
                                        kor = input("한글 뜻을 입력하세요: ")
                                        word.append(eng)
                                        word.append(kor)
                                        fw.writerow(word)

                                else:
                                    f.close()
                                    break

                            if mode == 'logout':
                                users.pop()

        elif hi == 2:
            imsi_user_info_list = []

            mail = input('e-mail: ')
            pw = input('password: ')
            name = input('name: ')
            who = input('are you student or teacher: ')

            imsi_user_info_list.append(mail)
            imsi_user_info_list.append(pw)
            imsi_user_info_list.append(name)
            imsi_user_info_list.append(who)

            f = open("user.csv", "a", newline="", encoding='utf-8')
            fw = csv.writer(f)
            fw.writerow(imsi_user_info_list)
            f.close()

        elif hi == 3:
            mail = input('e-mail: ')
            name = input('name: ')

            f = open("user.csv", "r", newline="", encoding='utf-8')
            fr = csv.reader(f)
            user_info_list = []
            count = 0
            for line in fr:
                user_info_list.append(line)
                count += 1
            f.close()

            for i in range(count):
                if (mail == user_info_list[i][0]) and (name == user_info_list[i][2]):
                    print(
                        f'This is your password: {user_info_list[i][1][:int(len(user_info_list[i][1]) / 2)]}{"*" * int(len(user_info_list[i][1]))}')

            print("You are wrong")

        else:
            exit()
