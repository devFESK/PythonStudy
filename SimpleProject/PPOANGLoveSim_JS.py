import PPOANGLoveSim_CH as ch
import time
import random

name_m = "뽀동이"
name_f = "소앙마"
health = 100
sex = "default"

# 챕터 함수
def Chapter01():
    global sex
    while sex != "남" and sex != "여":
        sex = input("성별을 입력하세요(남/여) : ")
        if sex == "남" or sex == "여":
            continue
        else:
            print("성별은 '남' 또는 '여' 로만 입력해주세요.")
    else:
        name = input("이름을 입력 하세요 : ")
        tem = random.uniform(89, 95)
        tem = round(tem, 2)
        txt01_1 = ["지나치게 화창한 올해 여름.", f"오늘의 날씨는 무려 <{tem}>도(화씨임). 엄청난 폭염이다...", f"무더운 여름을 나기 위해 {name}은/는 친구들과 함께 워터파크에 놀러갔다.", "그들 앞에 다가올 엄청난 운명을 예측하지 못한 채..."]
        ch.countDays()
        for i in txt01_1:
            for j in i:
                print(j, end = "")
                time.sleep(0.1)
            print()
            time.sleep(0.2)
Chapter01()
