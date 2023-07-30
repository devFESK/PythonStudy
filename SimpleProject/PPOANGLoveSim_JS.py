import PPOANGLoveSim_CH as ch
import time
import random

name = "default"
name_m = "뽀동이"
name_f = "소앙마"
health = 100
sex = "default"
tem = 3.0
# 챕터 함수
## 01 프롤로그

def Chapter01():
    global name
    global sex
    global tem
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
        txt01_1 = ["지나치게 화창한 올해 여름.", f"오늘의 날씨는 무려 <{tem}도>(화씨임). 엄청난 폭염이다...", f"무더운 여름을 나기 위해 {name}(은/는) 친구들과 함께 워터파크에 놀러갔다.", "그들 앞에 다가올 엄청난 운명을 예측하지 못한 채..."]
        ch.countDays()
        for i in txt01_1:
            for j in i:
                print(j, end = "")
                time.sleep(0.1)
            print()
            time.sleep(0.2)
        print()
Chapter01()

## 02 첫 만남

def Chapter02():
    global name
    global tem
    txt02_1 = [f"{tem}도의 폭염을 이겨내고, 워터파크에 도착한 우리들.", f"{name}은 수영복으로 갈아입고 깨끗하게 샤워를 했다.", "(오늘을 위해 다이어트를 했지. 귀엽고 섹시한 내 모습을 뽐내볼까..!)", f"파도 풀로 힘찬 걸음을 옮기는 {name}.", "그런데..!", "[으앗..!] / [꺅….!!]", "(강한 통증과 함께 어렴풋이 부드러운 살결이 느껴졌다.)", "[(크아아악 아파라..) 저기…. 괜찮으세요?]", "[지금 눈을 어디다 두고 다니시는 거예욧!!!]", "[???]", "[????????]", "(분명 나는 잘 걷고 있었는데… 내가 잘못했다는 건가, 적반하장도 가분수지.)"]
    ch.countDays()
    for i in txt02_1:
        for j in i:
            print(j, end = "")
            time.sleep(0.1)
        print()
        time.sleep(0.2)
Chapter02()
