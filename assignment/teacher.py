import random
import csv
from voca import Voca
from user import User

vocas = []
vocaf = open("voca.csv", "r", encoding='utf-8')
vocafr = csv.reader(vocaf)
for voca in vocafr:
    voca_obj = Voca(voca[0], voca[1])
    vocas.append(voca_obj)
vocaf.close()

while True:

    rand_num = random.randrange(0, len(vocas))
    answer = input(f"{vocas[rand_num].get_eng()}의 뜻을 쓰세요: ")

    if answer == vocas[rand_num].get_kor():
        vocas[rand_num].set_count(-1)
        print(vocas[rand_num].get_count())
        print("맞았습니다!")

    elif answer == "시험 끝":
        cf = open(f"{'minseo'}_voca.csv", "a", encoding='utf-8')
        cfw = csv.writer(cf)
        for n in range(len(vocas)):
            test_result = []
            test_result.append(vocas[n].get_eng())
            test_result.append(vocas[n].get_kor())
            test_result.append(vocas[n].get_count())
            print(test_result)
            cfw.writerow(test_result)
        cf.close()
        print("시험이 끝났습니다.")

    else:
        vocas[rand_num].set_count(1)
        print(vocas[rand_num].get_count())
        print("틀렸습니다!")