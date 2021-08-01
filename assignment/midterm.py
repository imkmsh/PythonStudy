# 중간고사

# 지연평가나 제너레이터 등의 개념을 사용하지 않고 평범하게 구현하세요

# 아래의 요구사항을 보고 콘솔 프로그램을 완성하세요
# 요구사항에 없는 디테일은 자유롭게 해도 좋습니다
# 그 어떤 경우에도 유저가 직접 종료하지 않으면 프로그램이 종료되어서는 안됩니다
# User Student Teacher Voca 4개의 클래스를 서로 다른 4개의 파일에 만들어야 합니다
# 메인 코드는 midterm.py 에서 실행하세요

# 1. 유저 설명
# 프로그램을 실행하면 콘솔에서
# 로그인, 회원가입, 비밀번호 찾기, 프로그램 종료 4가지 모드를 선택할 수 있습니다

# 회원가입을 선택한 경우 이메일, 비밀번호, 이름, 유저 종류를 입력받으세요
# 유저 종류는 학생 또는 선생님입니다
# 가입이 완료되면 유저의 정보를 csv 파일에 저장하세요
# 가입이 완료되면 다시 첫 화면으로 돌아옵니다

# 로그인을 선택한 경우 이메일과 비밀번호를 입력해야 합니다
# 이메일과 비밀번호가 모두 일치하는 경우, 유저의 정보를 객체로 복원합니다
# 복원된 객체는 users 라는 배열에 저장됩니다
# users 배열에는 현재 프로그램을 사용중인 모든 유저 객체가 저장되어 있습니다
# 로그인에 성공하면 환영 메세지를 출력하고, 현재 프로그램을 사용하는 다른 모든 유저의 이름이 출력됩니다
# 로그인에 성공하면 학생 유저의 경우 단어 공부하기, 로그아웃 2가지 모드를 선택할 수 있습니다
# 로그인에 성공하면 선생님 유저의 경우 단어 출제하기, 로그아웃 2가지 모드를 선택할 수 있습니다
# 이메일과 비밀번호 둘 중 하나가 틀린 경우 이메일 또는 비밀번호가 올바르지 않다고 출력하고 첫 화면으로 돌아갑니다

# 로그아웃을 한 경우 users 배열에서 나를 삭제합니다
# 로그아웃을 한 경우 첫 화면으로 돌아갑니다

# 비밀먼호 찾기를 선택한 경우 이름과 이메일을 입력해야 합니다
# 이름과 이메일이 모두 일치하는 경우, 비밀번호의 절반을 문자 *로 바꾸어서 알려줍니다
# 이름과 이메일이 일치하지 않는 경우 이름과 이메일이 올바르지 않다고 출력하고 첫 화면으로 돌아갑니다

# 프로그램 종료를 선택하면 프로그램이 종료됩니다


# 2. 단어장 설명
# 선생님 유저가 로그인을 하고 단어 출제하기를 선택한 경우
# 콘솔에 "입력모드(1), 단어장 종료(0) 중 하나를 선택하세요: " 라고 출력됩니다
# 입력 모드의 경우 콘솔에 "영단어를 입력하세요: " 라고 출력된다
# 선생님 유저가 영단어를 입력하면 콘솔에 "한글 뜻도 입력하세요: " 라고 출력된다
# 반복적으로 입력받다가 "영단어를 입력하세요: " 에서 사용자가 exit를 입력하면
# voca.csv라는 텍스트 파일이 생성되며, 생성된 파일 내에는
# apple, 사과
# school, 학교
# 이와 같은 형태로 저장되고
# 콘솔에 "입력모드(1), 단어장 종료(0) 중 하나를 선택하세요: " 라고 출력됩니다

# 학생 유저가 로그인을 하고 단어 공부하기를 선택한 경우
# 콘솔에 "다 외운 단어 재시험(1), 자주 틀리는 단어 재시험(2), 일반 시험(3), 단어장 종료(0) 중 하나를 선택하세요: " 라고 출력됩니다
# 시험을 한 번도 보지 않은 학생의 경우 1, 2를 선택하면 아직 시험을 보지 않았습니다 라고 출력됩니다

# 일반 시험을 선택한 경우 선생님이 출제한 voca.csv 파일을 읽어서
# 모든 단어를 Voca 객체로 생성한 후 vocas 배열에 저장하고 랜덤하게 골라서 출제하세요
# 콘솔에 "apple의 뜻을 쓰세요: " 라고 출제되며
# 한글 뜻을 사용자가 입력한 경우
# 맞았다면 "맞았습니다!" 라고 출력하고 다른 단어를 질문합니다
# 맞은 경우 voca 객체의 wrong_count 숫자를 1 감소시킵니다
# wrong_count가 -1이면 더 이상 감소시키지 않습니다
# 틀렸다면 "틀렸습니다!" 라고 출력하고 다른 단어를 질문합니다
# 틀린 경우 단어 객체의 wrong_count 숫자를 1 늘려줍니다
# 일반 시험이 끝나면 유저이름_voca.csv 파일을 생성하고 정보를 저장합니다
# 저장 형태는 아래와 같습니다
# apple, 사과, 1
# apple, 사과, 0
# school, 학교, -1
# 뒤의 숫자는 틀린 횟수입니다.

# 다 외운 단어 재시험의 경우 유저이름_voca.csv 파일을 읽어서 위와 같은 방식으로 복원하고
# 단어의 wrong_count가 -1인 단어들만 랜덤하게 골라서
# 콘솔에 "apple의 뜻을 쓰세요: " 라고 출제합니다
# 한글 뜻을 사용자가 입력한 경우
# 맞았다면 "맞았습니다!" 라고 출력하고 다른 단어를 질문합니다
# 맞은 경우 voca 객체의 wrong_count 숫자를 1 감소시킵니다
# wrong_count가 -1이면 더 이상 감소시키지 않습니다(-1인 단어는 다음 시험에서 이미 다 외운 단어로 분류됩니다)
# 틀렸다면 "틀렸습니다!" 라고 출력하고 다른 단어를 질문합니다
# 틀린 경우 단어 객체의 wrong_count 숫자를 1 늘려줍니다
# exit를 입력하면 시험이 끝나고 바로 전 화면으로 돌아갑니다
# 시험이 끝나면 유저이름_voca.csv 파일을 업데이트하세요

# 자주 틀리는 단어 재시험의 경우 위와 비슷한 방식으로 출제됩니다
# 단어의 wrong_count가 0 이상인 단어들만 랜덤하게 골라서
# 콘솔에 "apple의 뜻을 쓰세요: " 라고 출제한다
# 한글 뜻을 사용자가 입력한 경우
# 맞았다면 "맞았습니다!" 라고 출력하고 다른 단어를 질문합니다
# 맞은 경우 voca 객체의 wrong_count 숫자를 1 감소시킵니다
# wrong_count가 -1이면 더 이상 감소시키지 않습니다(-1인 단어는 다음 시험에서 이미 다 외운 단어로 분류됩니다)
# 틀렸다면 "틀렸습니다!" 라고 출력하고 다른 단어를 질문합니다
# 틀린 경우 단어 객체의 wrong_count 숫자를 1 늘려줍니다
# exit를 입력하면 시험이 끝나고 바로 전 화면으로 돌아갑니다
# 시험이 끝나면 유저이름_voca.csv 파일을 업데이트하세요

# 단어장 종료를 선택하면 회원창으로 되돌아 갑니다

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
