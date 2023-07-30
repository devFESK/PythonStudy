# 바로 실전 예제 달려~~~

'''
# 01 Hello World! 를 출력해보세요
print("Hello World!")

# 02 "진수 29살"이 나오도록 출력해보세요
name = "진수"
age = 29
print("진수 29살")
print(name, age, end = "살\n")
print("진수", end = " ")
print(age, end = "세\n")

# 03 결과값이 "진수, 29살"이 나오도록 출력해보세요
print("진수, 29살")
print("진수,", end = " ")
print("29살")
print("진수", end = ", ")
print("29살")
print("진수", "29살", sep = ", ")

# 04 <진수>와 <29살>을 변수에 넣고 진수, 29살을 출력해보세요 싫은데요~~
name = "진수"
age = 29
print(name, age, sep = ", ", end = "살\n")
name = 29
age = "진수"
print(age, name, sep = ", ", end = "살\n")
name = "진수"
age = 29
print(name, ", ", age, "살", sep="")
print(name + ", " + str(age), end = "살\n")
name = "진수"
age = 1+10+20-2
name2 = "살"
print("나는 {}, {}{}, 탐정이죠".format(name, age, name2))


# input 예제
    # 01 이름과 나이를 입력받고 다음과 같이 출력해보세요
text1 = input("이름을 입력해주세요: ")
text2 = input("나이를 입력해주세요: ")
print(f"{text1}({text2})님 어서오세요!")

    # 02 10을 입력받고 타입을 확인해보세요
num = input()
num = int(num)
print(type(num))

    # 03-04 다음 코드를 실행해보세요
       # num = input()
       # print(num + "10")
       # print(num + 10)
num = int(input())
print(num + 10)
num = input()
num = int(num)
print(num + 10)

    # 05 두개의 숫자(정수)를 입력받아 두개의 곱을 구해보세요
num01 = int(input("첫번째 숫자를 입력하세요 : "))
num02 = int(input("두번째 숫자를 입력하세요 : "))
print("두 숫자의 곱은", num01 * num02, end = "입니다.\n")
print(f"두 숫자의 곱은 {num01 * num02}입니다.")
print("두 숫자의 곱은", str(num01 * num02)+"입니다.")
print("두 숫자의 곱은" + " " + str(num01 * num02)+"입니다.")


    # 06 입력받은 문자열의 길이를 출력해보세요.
text01 = input("문자열을 입력해주세요: ")
print(f"입력받은 문자열: {text01}")
print(f"입력받은 문자열의 길이: {len(text01)}")


    # 07 정사각형 한변의 길이를 입력받아(실수) 해당 정사각형의 넓이를 출력해보세요
l = float(input("한변의 길이를 입력하세요: "))
print(f"정사각형의 넓이는 {l**2}입니다.")


    # 08 특정 모듈을 가져와서 원의 반지름(실수)를 입력받아 원의 넓이를 출력해보세요
r = float(input("원의 반지름을 입력하세요: "))
import math
a = math.pi * (r ** 2)

print(f"원의 넓이는 {math.pi * (r ** 2)}")
print(f"원의 넓이는 {a}")
print(f"원의 넓이는 {round(a, 2)}")



# 기초 예제
    # 01 변수 2개를 만들어 5와 10을 넣고, 여러가지 사칙연산을 출력해보세요
num01 = 10
num02 = 5

print(f"변수에 {num01}과 {num02}를 넣는다.")
print(f"덧셈: {num01 + num02}")
print(f"뺄셈: {num01 - num02}")
print(f"곱셈: {num01 * num02}")
print(f"거듭제곰: {num01 ** num02}")
print(f"나눗셈: {num01 / num02}")
print(f"나머지: {num01 % num02}")
# 이 모든 애들은 print("덧셈:", 숫자계산) 의 형식으로도 만들 수 있음

a = set([1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10])
print(a)


def addRange(num):
    for i in range(0, num):
        if i == num - 1:
            print(i)
            break
        print(i, end = " ")

addRange(5)


# 조건문 예제
    # 01 변수 하나를 선언하여 해당 값이 10보다 큰 경우 "크다", 그 외는 "작다"를 출력해보세요
x = 10
if x > 10:
    print("크다")
else:
    print("작다")

    # 02 변수 하나를 입력해서 해당 변수의 값이 홀수인지 짝수인지 확인할 수 있는 코드를 만들어보세요
x = 9
y = 8
if x % 2 != 0:
    print("너는 홀수야 ㅋㅋ")
else:
    print("너는 짝수임")
if y % 2 != 0:
    print("너는 홀수야 ㅋㅋ")
elif y % 2 == 0:
    print("너는 짝수임")

    # 03 숫자 하나를 입력받아서 90 이상은 A, 80 이상은 B, 70 이상은 C, 60 이상은 D, 그 외는 F를 출력 해보세요
a = int(input())
for i in range(10):
    b = a + (10*i)
    if b == 100:
        print("finished!")
        break
    if b >= 90:
        print("A")
    elif b >= 80:
        print("B")
    elif b >= 70:
        print("C")
    elif b >= 60:
        print("D")
    else:
        print("F")

    # 04 변수 두개를 입력하여 해당값이 같은지 크고 작은지를 출력 해보세요
num01 = int(input("첫번째 숫자를 입력하세요: "))
num02 = int(input("두번째 숫자를 입력하세요: "))

if num01 > num02:
    print("첫번째 숫자가 더 큽니다")
elif num01 < num02:
    print("두번째 숫자가 더 큽니다")
elif num02 == num01:
    print("두 숫자가 같습니다 뿅뿅")

    # 05 "password"를 입력하면 "비밀번호가 풀렸습니다"를 출력하고, 아닌경우 "비밀번호가 틀렸습니다"를 출력해보세요
pw = "password"
code = input()

if code == pw:
    print("비밀번호가 일치하였습니다.")
else:
    print("비밀번호가 틀렸습니다.")

    # 06 변수 두개를 입력받아 두 변수의 음수 양수를 구분하는 코드를 만들어보세요
n01 = int(input("첫번째 숫자를 입력하세요: "))
n02 = int(input("두번째 숫자를 입력하세요: "))
t01 = "첫 번째 숫자는"
t02 = "두 번째 숫자는"
t03 = "양수"
t04 = "음수"
if n01 > 0 and n02 > 0:
    print("두 숫자 모두 양수입니다.")
elif n01 > 0 and n02 < 0:
    print(f"{t01} {t03}, {t02} {t04}입니다.")
elif n01 < 0 and n02 > 0:
    print(f"{t01} {t04}, {t02} {t03}입니다.")
else:
    print(f"두 숫자 모두 {t04}입니다.")

    # 07 변수 하나가 True인 경우 "참"을 출력하고, False인 경우 "거짓"을 출력해보세요
x = 1
if x == True:
    print("True")
else:
    print("False")

if x:
    print("True")
else:
    print("False")

    # 08 여러가지 값이 담긴 dict 변수를 생성하고, 그 안에 입력한 값이 key로 존재하는지 확인해보고 존재한다면 value값과 함께 출력해보세요.
a = {"A" : 1, "B" : 2, "C" : 3}
b = input()
if b in a:
    print(f"{b}는 존재합니다. value = {a[b]}")
    print(f"{b}는 존재합니다. value = {a.get(b)}")
else:
    print(f"{b}는 존재하지 않습니다.")

if b in a:
    a.get(b, print(f"{b}는 존재하지 않습니다."))

    # 09 다음 결과를 보고 조건문을 완성해보세요
"""집, 회사중 어디로 가겠습니까? > #집
    #집을 입력한경우
	    집에서 게임하겠습니까? 휴식하시겠습니까? > #게임
	    #게임을 입력한경우
		게임을 하다가 회사를 짤렸습니다. 해고!
	    #휴식을 입력한 경우
		충분히 휴식해서 회사에 출근했습니다.
	    #그 외를 입력한 경우
		멍때리다가 회사를 못갔습니다. 해고!
    #회사를 입력한 경우
	    회사에서 일하겠습니까? 게임하겠습니까? > #일
	    #일을 입력한 경우
		열심히 한 당신! 진급했습니다!
	    #게임을 입력한 경우
		게임하다가 걸렸습니다. 해고!
	    #그 외를 입력한 경우
		회사에서 딴짓하다 혼났습니다.
    #그 외를 입력한 경우
	    백수시군요 집에갑시다
"""

q01 = input("집, 회사중 어디로 가겠습니까? > ")
if q01 == "집":
    q01_01 = input("집에서 게임하시겠습니다? 휴식하겠습니까? > ")
    if q01_01 == "게임":
        print("게임을 하다가 회사를 짤렸습니다. 해고!")
    elif q01_01 == "휴식":
        print("충분히 휴식해서 회사에 출근했습니다.")
    else:
        print("멍때리다가 회사를 못갔습니다. 해고!")
elif q01 == "회사":
    q01_01 = input("회사에서 일하시겠습니까? 게임하겠습니까? > ")
    if q01_01 == "일":
        print("열심히 한 당신! 진급했습니다!")
    elif q01_01 == "게임":
        print("게임하다가 걸렸습니다. 해고!")
    else:
        print("회사에서 딴 짓 하다가 혼났습니다ㅠㅠ")    
else:
    print("백수시군요 집에 갑시다 ㅋㅋ")

    

# 반복문 예제
    # 01 반복문을 사용해서 0~10까지 출력해보세요
for i in range(11):
    print(i)

    # 02 입력받은 숫자만큼 반복을 돌면서 짝수일때만 숫자를 출력하고, 10번 반복했을 때 프로그램을 종료하는 코드를 만들어보세요.
def evenNumber(num):
    print(num)
    for i in range(0, num):
        if i % 2 == 0:
            print(i, end = " ")
        elif i == 10 - 1:
            print("finished!")
            break

evenNumber(100)

def evenNumber02(num):
    print(num)
    for i in range(0, num):
        if i == 10:
            print("finished")
            break
        if i % 2 != 0:
            continue
        print(i, end = " ")

evenNumber02(100)


    # 03 숫자 하나를 입력받아 다음과 같이 출력해보세요
n01 = int(input())
for i in range(n01):
    print("*****")

print()

for i in range(n01 * n01):
    if (i + 1) % n01 != 0:
        print("*", end = "")
    else:
        print("*")

print()

for i in range(n01 * n01):
    print("*", end = "")
    if (i + 1) % n01 == 0:
        print()

print()

def repeat():
    for j in range(n01):
        print("*", end = "")

for i in range(n01):
    repeat()
    print()

print()

for i in range(n01):
    for j in range(n01):
        print("*", end = "")
    print()


    # 04 - 08 숫자 하나를 입력받아 다음과 같이 출력해보세요
n = int(input())

for i in range(n):
    k = i + 1
    print("*" * k)

print()

for i in range(n):
    for j in range(i + 1):
        print("*", end ="")
    print()

print()

for i in range(n):
    for j in range(n - i):
        print("*", end ="")
    print()

print()

for i in range(n):
    for j in range(n - (i + 1)):
        print(" ", end ="")
    print("*" * (i + 1))

print()

for i in range(n):
    for j in range(n - (i + 1)):
        print(" ", end = "")
    for k in range(i + 1):
        print("*", end = "")
    print()

print()

for i in range(n):
    for j in range(n - (i + 1)):
        print(" ", end = "")
    for k in range(i + 1):
        print("*", end = "")
    for l in range(i):
        print("*", end ="")
    print()

print()

for i in range(n):
    for j in range(n - (i + 1)):
        print(" ", end = "")
    for k in range((2 * i) + 1):
        print("*", end = "")
    print()

print()

for i in range((2 * n) + 1):
    if i < n:
        for k in range(n - i):
            print(" ", end = "")
        print("*")
    if i == n:
        for j in range(i + 1):
            print("*", end = "")
        print()
    if i > n:
        for k in range(n - (i - 5)):
            print(" ", end = "")
        print("*")


# 09 문자를 입력하여 단어 하나씩 출력하는 코드를 만들어 보세요.

t = input()
tl = len(t)

for i in range(tl):
    print(t[i])

print()

for i in t:
    print(i)


# 10 여러가지 값이 담긴 리스트 변수를 생성하고 반복문을 이용하여 하나씩 출력해보세요

a = [1, 2, "A", "B"]
for i in a:
    print(i)

# 11 10번 변수로 해당 변수의 인덱스와 값을 출력해보세요

a = [1, 2, "A", "B"]
for x, y in enumerate(a):
    print(x, y)

print()

b = len(a)
for i in range(b):
    print(f"{i} {a[i]}")


# 12 dict로 해
a = {"aser" : "B", 2 : "C", 3 : "A"}

for i in a:
    print(i, a[i], sep = " : ")

for x, y in a.items():
    print(x, y)
for x, y in enumerate(a):
    print(x, a[y])

for x, (y, z) in enumerate(a.items()):
    print(x, y, z)

import time

i = 1
while i > 0:
    print(i)
    i += 1
    time.sleep(0.5)

    
# 13 while 문을 사용하여 10부터 1가지 줄어드는 코드를 작성해보세요
poison = 10
while poison > 0:
    print(poison)
    poison -= 1
else:
    print("창훈 is dead") 


# 14 입력한 숫자까지 3, 6, 9 게임을 진행해 보세요

er = int(input())
cr = 1

while er >= cr:
    if "3" in str(cr) or "6" in str(cr) or "9" in str(cr):
        print(f"({cr})짝!", end = " ")
        cr += 1
        continue
    print(cr, end = " ")
    cr += 1
else:
    print("게임 종료!")


# 15 여러가지 값이 담긴 dict 변수 생성, 입력한 값이 키로 존재하는지 확인, 존재하면 벨류값과 함께 출력하세요. 프로그램은 123을 누를때까지 반복한다.

a = {"C": 500, "C++": 700, "C#" : 900, "JAVA": 1000, "PYTHON": 5000}
t = input("입력하세요 >> ")

while t != "123":
    if t in a.keys():
        print(f"{t}는 존재합니다. value = {a[t]}")
    else:
        print(f"{t}는 존재하지 않습니다.")
    t = input("입력하세요 >> ")
else:
    print("프로그램을 종료합니다.")

a = {"C": 500, "C++": 700, "C#" : 900, "JAVA": 1000, "PYTHON": 5000}

while True:
    t = input("입력하세요 >> ")
    if t == "123":
        print("프로그램을 종료합니다.")
        break
    if t in a.keys():
        print(f"{t}는 존재합니다. value = {a[t]}")
    else:
        print(f"{t}는 존재하지 않습니다.")

'''
import time
a = ["안녕하세요", "반갑습니다", "제 이름은", "김진수입니다.", "너는 누구세요?"]
for j in a:
    for i in j:
        print(i, end = "")
        time.sleep(0.1)
    print()

time.sleep(1)
msg = input(">> ")

b = "안녕하살법"
for i in b:
    print(i, end = "")
    time.sleep(0.1)
print()
msg = input(">> ")