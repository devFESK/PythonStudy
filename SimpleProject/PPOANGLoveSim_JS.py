import PPOANGLoveSim_CH as ch
import time
import random


name = "default"
name_m = "뽀동이"
name_f = "소앙마"
health = 100
sex = "default"
tem = 3.0
game_over = False

def Loading():
    global name
    global health
    global sex
    global tem
    name = "default"
    health = 100
    sex = "default"
    tem = 3.0
    txt = "#######################################"
    for i in txt:
        print(i, end = "")
        time.sleep(1 / len(txt))
    print()
    print()

# 챕터 함수
## 01 프롤로그

def Chapter01():
    global name
    global sex
    global tem
    def Chaper01Text(name, tem):
        txt = ["지나치게 화창한 올해 여름.", f"오늘의 날씨는 무려 <{tem}도>(화씨임). 엄청난 폭염이다...", f"무더운 여름을 나기 위해 {name}(은/는) 친구들과 내일 워터파크에 놀러가기로 했다.", "그들 앞에 다가올 엄청난 운명을 예측하지 못한 채..."]
        return txt
    days = "1일차"
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
        #txt01_1 = ["지나치게 화창한 올해 여름.", f"오늘의 날씨는 무려 <{tem}도>(화씨임). 엄청난 폭염이다...", f"무더운 여름을 나기 위해 {name}(은/는) 친구들과 내일 워터파크에 놀러가기로 했다.", "그들 앞에 다가올 엄청난 운명을 예측하지 못한 채..."]
        ch.countDays(days)
        for i in Chaper01Text(name, tem):
            for j in i:
                print(j, end = "")
                time.sleep(0.1)
            print()
            time.sleep(0.2)
        print()

## 02 첫 만남

def Chapter02():
    global name
    global tem
    global health
    days = "2일차"
    def Chapter02Text1(name, tem):
        txt = [f"{tem + 1.0}도의 폭염을 이겨내고, 워터파크에 도착한 우리들.", f"{name}(은/는) 수영복으로 갈아입고 깨끗하게 샤워를 했다.", "(오늘을 위해 다이어트를 했지. 귀엽고 섹시한 내 모습을 뽐내볼까..!)", f"파도 풀로 힘찬 걸음을 옮기는 {name}.", "그런데..!", "[으앗..!] / [꺅...!!]", "(강한 통증과 함께 어렴풋이 부드러운 살결이 느껴졌다.)", "(크아아악 아파라..) [저기... 괜찮으세요?]", "[지금 눈을 어디다 두고 다니시는 거예욧!!!]", "[???]", "[????????]", "(분명 나는 잘 걷고 있었는데... 내가 잘못했다는 건가? 적반하장도 가분수지.)"]
        return txt
    ch.countDays(days)
    for i in Chapter02Text1(name, tem):
        for j in i:
            print(j, end = "")
            time.sleep(0.1)
        print()
        time.sleep(0.2)
    time.sleep(0.5)
    print()
    t01 = "default"
    c01 = {"a" : "[그쪽이 먼저 밀었잖아요]", "b" : "[이 씨이발 경찰 불러?]", "c" : "[아이구 죄송합니다...ㅠㅠ]"}
    c01a = ["[제가 먼저 밀었다구요???]", "[네. 그쪽이 제대로 앞을 안보고 다녀서 이런거잖아요... 그러면서 시비까지 거시네요.]", "[진짜 어이가 없다.]", "[누가 할 소릴..?]", "파직파직... 그들 사이에서 불꽃이 튀며, 묘한 신경전이 이어졌다.", "[하아... 네. 일단 알겠습니다. 그쪽도 조심해주세요. 저도 주의하겠습니다]", "[네.]", "(응 주의 절대 안해~ 무조건 니 잘못이야~)"]
    c01b = ["[뭐... 씨.. 씨발..???]", "[그래 씨발. 불만 있냐? 맞짱 떠?]", "[ㅋㅋ 완전 미친 사람이네. 네 제가 잘못했습니다. 지나가세요~]", "[다음부터 조심해라. 워터파크에서 익사하고 싶지 않으면...]"]
    c01c = ["[아야... 아니에요. 제가 앞을 안보고 가서 부딪힌 건데요 뭘.]", "[그래도 제가 더 잘 봤어야 하는데, 죄송해요...] (니가 잘못한걸 알긴 하네?)", "[저 친구들이 기다리고 있어서 먼저 가보겠습니다..! 죄송합니다!]", "(돌대가린가 엄청 아프네..)"]
    txt02_2 = [f"그 후 {name}(은/는) 허둥지둥 친구들과 합류했다.", "[뭐야 왜이렇게 늦었어. 또 똥 싸고 왔냐?]", "[아니야... 오다가 어떤 재수 없는 돌대가리랑 부딪혀가지고. 아이고 아직도 아프네]", "[ㅋㅋㅋ 너도 한 돌대가리 하잖아]"]
    while t01 not in c01:
        for i, j in c01.items():
            time.sleep(0.5)
            print(f"{j} >> '{i}' 입력")
        t01 = input("\n >> ")
        print()
        if t01 in c01:
            continue
        else:
            print("대답은 'a', 'b', 'c' 로만 입력해주세요.")
            print()
    else:
        time.sleep(0.2)
        if t01 == "a":
            health += 10
            for i in c01a:
                for j in i:
                    print(j, end = "")
                    time.sleep(0.1)
                print()
                time.sleep(0.2)
        elif t01 == "b":
            health -= 10
            for i in c01b:
                for j in i:
                    print(j, end = "")
                    time.sleep(0.1)
                print()
                time.sleep(0.2)
        elif t01 == "c":
            for i in c01c:
                for j in i:
                    print(j, end = "")
                    time.sleep(0.1)
                print()
                time.sleep(0.2)
    txt02_2.append("[ㅋㅋ 조용히 해. 그나저나 아까 부딪힌 사람...]")
    for i in txt02_2:
        for j in i:
            print(j, end = "")
            time.sleep(0.1)
        print()
        time.sleep(0.2)
    time.sleep(0.5)





def GameOver():
    global game_over
    game_over = True


if __name__ == "__main__":
    endmsg = "FESK의 개발은 계속됩니다. 구독과 좋아요를 눌러주세요! \n"
    while True:
        if game_over == True:
            for i in endmsg:
                print(i, end = "")
                time.sleep(0.1)
            time.sleep(0.2)
            print()
            msg = input("다시 시도하시겠습니까? (Y/N) >> ")
            if(msg == "y" or msg == "Y"):
                game_over = False
            elif(msg == "n" or msg == "N"):
                break
            else:
                print()
                print("대답은 'y', 'n'로만 입력해주세요.\n")
                continue
        Loading()
        Chapter01()
        Chapter02()
        GameOver()
        time.sleep(0.5)
        continued = "....."
        for i in continued:
            print(i)
            time.sleep(0.2)

