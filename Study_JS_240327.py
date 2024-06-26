# 파이썬 기초
    # 세미콜론 (;) -> 다양한 프로그래밍 언어는 구문이 끝나면 ;을 통해서 끝을 표현해준다
        # 파이썬은 ;을 붙이지 않아도 오류가 발생하지 않는다
        # 한 줄에 여러개의 구문을 사용할 때는 구분을 위해서 ;을 사용
        # 한 줄에 여러개의 구문을 사용해도 결과는 줄바꿈이 된 형태로 나옴

    # 들여쓰기 -> 파이썬에서 들여쓰기는 하나의 문법이다
        # 하나의 구문 안에 속해있음을 표현하는 방법이다
        # 다른 프로그래밍 언어는 중괄호({})를 통해서 하나로 묶어주는 방식이지만, 파이썬은 들여쓰기를 통해서 묶어주는 작업을 진행한다
        # 반복문, 함수제작 같은 곳에서 많이 사용하게 됨
        # 가장 밖에 있는 구문은 들여쓰기를 사용하지 않음 -> 에러 발생
        # 들여쓰기 정도에 따라서 다르게 인식
        # Tab 키를 이용해서 들여쓰기

    # 주석(comment) -> 컴퓨터가 프로그램을 실행했을 때, 실행코드로 판단하지 않게 만드는 부분 -> 지금 #(샵)걸어서 쓰고 있는 이 문장들을 의미함

    # 변수 -> 데이터 정보를 담아두는 공간
        # 코딩이란 다양한 데이터를 가지고 여러가지 상황을 만들어내는 것
        # 데이터를 다루기 위해서는 어떤 공간에 원하는 데이터를 보관했다가 필요할때마다 사용할 수 있어야 함
        # 특정 공간에 데이터를 넣을 때, 그 "공간의 이름을 명명"하여 나중에 컴퓨터에게 해당 공간에 들어있는 데이터를 가져오라고 할 수 있음. 이 때, 그 공간을 변수라고 하고, "공간을 명명하는 것을 변수 지정"이라고 함
        # 변수 규칙
            # 특수문자는 _(underbar)만 가능
            # 숫자로 시작할 수 없음
            # 공백을 포함할 수 없음 -> 공백이 발생하면 컴퓨터는 끊어진 것으로 판단함
            # 가급적 알파벳 사용
            # 내가 사용할 변수의 이름은 알아볼 수 있게 만들어주면 좋음(단, 반복문에서 자주 사용하는 i, j, k 등은 임시로 만들어주는 변수이기 때문에 괜찮음)
            # 키워드를 사용할 수 없음
                # 키워드는 파이썬에서 이미 기능적으로 존재하는 이름들
                # 키워드 확인 방법
                    # import keyword
                    # print(keyword.kwlist)
                # 결과 : [‘False’, ‘None’, ‘True’, ‘and’, ‘as’, ‘assert’, ‘async’, ‘await’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘nonlocal’, ‘not’, ‘or’, ‘pass’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]
        # 변수 종류
            # 같은 지역(위계)에서 같은 이름을 가진 변수는 하나뿐
                # ex) 만약 함수 F 내에서 전역변수 a를 선언했으면, 다시 a라는 변수를 사용 불가
            # 전역 변수 = 전(체영)역 변수
                # 스크립트 전체에서 접근이 가능한 변수
            # 지역 변수
                # 특정 범위에서만 사용하는 변수
                # 클래스 혹은 함수 내부에서 선언하는 변수들은 지역변수로 취급
                # 전역변수와 같은 이름으로 지역변수 선언 -> 가능, 그러나 지역변수가 지역 내에서 우선적으로 사용됨 / 사실상 생김새만 같고 다른 변수
                # 기본적으로 전역변수를 내부에서 사용할대는 "global" 키워드를 통해서 전역변수인 것을 명시해주는 것이 좋음
                    # 전역변수 값을 낮은 위계에서 변경하려면 global 키워드로 선언한 후 변경해야 함
            # nonlocal 변수
                # 함수 또는 클래스의 하위(함수 안의 함수 개념)에서, 상위 함수 또는 클래스에서 선언한 변수를 사용하고 싶을때 global 대신 사용
    # print(출력) -> 프로그램을 실행했을 때 결과를 출력하는 기본적인 함수
        # print라는 기능은 기본적으로 언어에 탑재된 출력 기능이라고 이해하면 좋음
        # 기본 사용 형식은 "print(somthing)" 형식
        # print문 안에 여러가지 내용을 함께 넣어주고 싶으면 ","로 구분함. 이때 기본적으로 ","를 사용하면 스페이스가 포함됨
        # 여러가지 값을 함께 사용할 때, 값 사이에 들어가는 스페이스를 변경하고 싶으면 "sep" 이용
        # print문이 끝나고 난 뒤에는 '\n(줄바꿈)'이 자동으로 붙음 -> "end" 이용해서 "\n" 대신 다른 값을 넣을 수 있음
        # "f-string"을 이용해서 print하는 방식
            # 문자열 안에 다른 것들도 넣는 방식
            # 작성 방법 -> f'원하는 문자열'
            # 변수나 함수의 경우 "{}" 안에서 호출하면 문자열 안에 값이 들어감
            # "" 앞에 f를 붙이면 f-string 방식을 사용할 수 있음
            # 이때, 사용하고 싶은 변수를 {} 안에 넣으면 "" 내부에서 변수를 가져와서 사용할 수 있음

    # input(입력) -> 프로그램 실행시 내부가 아닌 외부에서 값을 받는 함수
        # 항상 프로그램에 직접 값을 넣어가면서 실행할 수는 없음... 그럼 매번 다른 데이터를 가지고 실행하기 위해서 코드를 수정해야 하는데 굉장히 비효율적임
        # 따라서 우리가 프로그램을 실행한 상태에서 키보드를 통해 프로그램에 값을 집어넣을 수 있어야 함
        # 기본 사용형식은 "input()"
            # input을 통해 입력받은 값들은 모두 문자열
            # 입력받은 값을 변수에 집어넣어 프로그램 진행
            # 만약 입력받을 때 문구를 넣고 싶다면 input("씨부려봐") 형식을 사용하면 됨
            # input을 문자열로 받고 싶지 않다면 "캐스팅"을 통해서 변환해줄 수 있음

    # casting(형변환)
        # 대표적으로 입력해서 만들어진 데이터는 기본적으로 문자열로 이루어져 있음
        # 우리가 사용하는 데이터는 숫자도 있고, 여러가지 형태의 데이터가 존재함
        # 코드를 제작하면서 해당 데이터의 형태를 변형시켜야 하는 경우가 발생함
        # 해당 변수의 타입을 알고 싶으면 "type(변수이름)"
            # int(data) -> 정수형으로 캐스팅
            # float(data) -> 실수형으로 캐스팅
            # str(data) -> 문자형으로 캐스팅
            # 기타 리스트, 튜플, 딕셔너리 등 다양한 형식으로 형변환 가능
            # 각 형변환 진행 시, 원하는 형식에 맞춰져 있지 않으면 캐스팅이 되지 않고 에러 발생
                # if int(3.5) -> 정수의 문자형만 정상적으로 캐스팅(에러)
                # 딕셔너리는 key, value로 이루어져 있으므로 에러가 발생하지 않게 형식을 잘 맞춰주자

    # import(모듈 가져오기)
        # 외부에서 만들어진 파이썬 파일, 라이브러리 등을 사용할 수 있게 만드는 기능
        # 기본적으로 제공하는 파이썬 함수들이 아닌 여러사람들이 만든 기능, 혹은 내가 다른 파일에서 만들어놨던 기능들을 현재 프로그램에서 사용할 수 있게 함
        # 머신러닝, 딥러닝 등의 엄청난 기능들도 전부 이런 import로 가져와서 실행함
        # 기본 형식은 import 파일명(라이브러리)
            # 가져온 파일(라이브러리)의 기능을 사용하기 위해서는 파일명.함수(라이브러리.함수)를 사용해야 함
            # 매번 "파일명.함수"와 같은 방식을 사용하기 싫으면 "from"을 이용함
                # from 파일명(라이브러리) import a -> 파일(라이브러리)에 있는 a라는 함수를 가져온다
                # from 파일명(라이브러리) import * -> 파일(라이브러리)에 있는 모든 함수를 가져온다
        # __name__ & __main__
            # __name__
                # 해당 모듈의 이름을 가져오는 변수
                # 해당 파일을 실행하면 __name__의 이름은 __main__이 됨
                # import를 통해서 모듈을 가져오면 __name__은 해당 모듈의 이름이 됨
            # __main__
                # 프로그램이 실행될 때 메인으로 실행되는 모듈
                # C언어에서 "main()"과 같은 역할

    # 파이썬 실행
        # 파이썬 코드를 실행하는 방법에는 여러가지가 있음
            # IDE(Integrated Development Environment, 통합개발환경)
                # 가장 간단한 방법
                # 자동 완성 기능을 통해 빠른 개발을 이뤄낼 수 있음
                # 바로바로 실행해볼 수 있고, 오류를 로그를 통해서 알려줌
            # 터미널
                # 기본적인 코딩 방식
                # 터미널을 통해서 파이썬 코딩의 모든 방식을 할 수 있음
            # 파일 직접 제작(메모장도 가능)
                # 실행 능력은 없지만 문법에 맞춰서 파일을 만들면 가능
            # 주피터
                # 코드를 한칸씩 단계별로 개발이 가능
                # UI 적용이 되어 실시간으로 확인 할 수 있음

# 기본 문법
    # 기본 연산자
        # 산술 연산자
            # 사칙연산은 기본적인 수학을 따라감
            # ** : 거듭제곱
            # // : 몫
            # % : 나머지
        # 할당 연산자
            # a = b : b 값을 a에 적용
            # a += b : a = a + b(+, -, *, / 등 모든 산술연산자에 적용, 산술할 기호가 "=" 앞에 붙는다고 생각하면 됨)
        # 비교 연산자
            # >, >=, <, <= 기본인거 아시죠?
            # == : 간다(수학에서 생각하는 "=")
            # != : 다르다
        # 논리 연산자
            # and : 곱연산
                # True and True : True
                # True and False : False
                # False and True : False
                # False and False : False
            # or : 합연산
                # True or True : True
                # True or False : True
                # False or True : True
                # False or False : False
            # not(A) : not 연산, A의 반대 연산
                # not(True) : False
                # not(False) : True
        # 멤버 연산자
            # A in List -> A가 List 안에 존재하는지 여부, 존재하면 True
            # A not in List -> A가 List 안에 존재하지 않는지 여부, 존재 안하면 True
        # 식별 연산자
            # 두 데이터의 메모리 위치를 비교
            # A is B -> A와 B의 메모리 위치가 같은지 비교
            # A is not B -> A와 B의 메모리 위치가 다른지 비교
            # "==, !=" 와의 차이점
                # ==는 데이터의 값의 일치 여부를 비교 : 3.0과 3은 같다
                # is는 데이터 자체를 비교 : 3.0과 3은 다르다
    # 자료형
        # 기존의 프로그래밍 언어들은 변수에 값을 넣기 위해서 변수 앞에 어떤 형인지 선언을 해줘야 컴퓨터가 인식할 수 있었지만, 파이썬은 입력하는 값을 자동으로 잡아줌
        # 자료형의 종류
            # Number(숫자형)
                # int(정수형)
                # float(실수형)
                # complex(복소수형) -> 많이 안쓰겠죠..?
            # str(문자열)
                # 우리가 일상적으로 사용하는 문자들의 나열
                # "" or ''을 사용하여 문자열을 나타냄
                # 문자열과 문자열 사이에 "+"을 사용할 경우, 문자열이 붙어서 나옴
                # 여러줄의 문장을 구현하고 싶으면 """ """, ''' '''를 사용할 수 있음
                # 여러줄의 문자열 방식을 이용해서 모든 코드를 문자열의 나열로 처리해버릴 수 있음 -> 특정 코드의 일시적인 비활성화 등으로 활용
                # "[]", "[:]"을 이용해 일부를 가져올 수 있음
                    # 이런 형식의 범위를 지정할 때, [a:b]같은 형식이면 "a부터 b-1" 까지라는 뜻임
                    # 실제 카운트한 index가 a를 포함하기 때문에, 구간 개수가 b-a와 동일하도록 하기 위해서가 아닐까?
                # "+"을 통해 문자열을 합칠 수 있고, "*"을 통해서 문자를 반복시킬 수 있음
                # 탈출 문자열 : 엔터나 키보드에 있는 문자 외의 기능을 사용
                    # "\n" : 줄바꿈
                    # "\"" : " 출력
                    # "\'" : ' 출력
                    # "\\" : \ 출력
                    # "\r" : 커서를 맨 앞으로 이동
                    # "\b" : 한 글자 삭제
                    # "\t" : tab
            # bool(불형)
                # 참과 거짓을 표현하는 자료형
                # True / False로 이루어져 있음
                # 내용이 비어있을 경우 False, 내용이 존재하면 True
                    # True -> "python", [1, 2, 3], (1, 2, 3), {"a" : 1}, 1
                    # False -> "", [], {}, (), 0, None
            # List(리스트)
                # 여러가지 데이터의 묶음(군같은 개념)
                # 리스트 내 데이터 구분은 "," 이용
                # "[]"으로 묶음 처리
                # 리스트의 index는 "0"부터 시작함
                # index가 "-1"인 경우 마지막 index item을 가져옴
            # Tuple(튜플)
                # List와 비슷한 형식, 그러나 내부의 값을 변경할 수 없음
                # ()로 둘러싸여 있으며, 1개의 요소만을 담을 때는 뒤에 ","를 써야 함
                # 반드시 ()를 사용하지 않고 생략 가능
                # 튜플 내 요소 삭제 불가능
            # set(세트)
                # 집합 자료형
                # "set" 키워드를 통해서 만들 수 있음
                # 문자열을 세트로 만들 수 있음
                    # 세트는 중복되는 부분을 제거하고 무작위로 순서가 배치됨
                # 세트는 요소가 존재하지 않음
                    # index를 통해서 값을 가져올 수 없음
                    # index로 접근하기 위해서는 리스트나 튜플로 변환하여야 함
                # 세트는 교집합, 합집합, 차집합을 구할때 간편함(like boolean 연산)
                    # 교집합
                        # a & b / a.intersection(b)
                    # 합집합
                        # a | b / a.union(b)
                    # 차집합
                        # a - b / a.difference(b)
                # 세트는 값을 추가하거나 뺄 수 있음
                    # a.add(b) / a.update([1, 2, 3]) / a.remove(2)
            # dict(딕셔너리)
                # 순서는 없음, "key"와 "value"를 한 쌍으로 갖는 데이터 구조체(그래스호퍼에 저런 컴포넌트 구조 많죠?)
                # "{}"로 구성됨, key와 value는 ":" 로 구분
                # key는 중복될 수 없음
                # key는 불변 값으로 사용해야 함
                # value는 중복될 수 있으며, 어떤 데이터 타입도 가능
                # key값을 이용하여 value를 얻을 수 있음
                # 사용 방법
                    # dict[x] -> x key에 연결된 value 반환 / x가 없으면 에러
                    # dict.get(x) -> x key에 연결된 value 반환 / x가 없으면 None
                    # dict.get(x, y) -> x key에 연결된 value 반환 / x가 없으면 y 반환
                    # dict.keys() -> dict에 속한 keys 반환
                    # dict.values() -> dict에 속한 values 반환
                    # dict.items() -> dict에 속한 (keys, values) 반환
                    # x in dict -> x가 dict 안에 key로 존재하는지 판별
                    # dict[x] = y -> 마지막 index에 (x, y) key와 value 값 추가
                    # del dict[x] -> (x, value)로 구성된 x key와 해당 value값 삭제
                    # dict.clear() -> dict 초기화
    # 조건문
        # if 문
            # 조건식을 만족하면 하위에 있는 구문 실행
            # 조건식이 거짓일 때 다른 식을 사용하는 방법
                # else : 이전 조건들이 모두 거짓일 경우의 조건
                # elif : 이전 조건이 아닐 때 그럼 이건 어때? 개념
                # if... elif... elif... ... else
                    # if~ 아니면 elif~ 아니면 elif~ ... 전부 아닐경우 else~
            # 조건식 만들어내는 방법 -> 비교 연산자
                # >, <, >=, <=, ==, !=
            # 여러가지 조건을 함께 사용하고 싶을 때 -> 논리 연산자 사용
    # 반복문
        # range
            # range(a, b, c)
            # a = 단독으로 쓰일 경우 0부터 a-1까지 범위, b or c 존재할 경우 시작값
            # b = 종료값
            # c = 공차
        # for문
            # 반복문
    # 함수
    # 클래스
    # 모듈
    # 패키지
# 파이썬 지식
# 자주사용하는 함수


"""
# print 기본형
print('hello') # hello
print('hello', 'world') # hello world
# sep
print(1, 2, 3, sep = ' ') # 1 2 3
print(1, 2, 3, sep = ', ') # 1, 2, 3
# end
print(1, 2, 3, end = '@\n') # 1, 2, 3@ -> "\n"을 "@"로 변경한 뒤에 생략된 "\n"을 넣어줌으로써 줄바꿈까지 포함시켜줌
# 변수와 함께
name = 'python'
age = 20
print('name is', name, 'and age is', age) # name is python and age is 20
# f-string 방식
code = 'world'
print(f'hello {code}') # hello world

def function():
    return 'hi'
print(f'say {function()}') # say hi
# f-string 방식 02
name = "Jinsoo"
age = 30

print(f"{name}의 나이는 {age}살 입니다.")

# input
v = input()
t = input("씨부려봐!\n") # string 뒤에 바로 대답이 들어가는게 싫어서 "\n"을 넣어줬더니 예상대로 줄바뀜이 되는군 좋아용~
print(v)
print(t)
int(input('숫자를 입력하세요 -> '))
float(input('실수를 입력하세요 -> '))

# import
import calendar
calendar.prmonth(2024, 4)

# str [], [:] test
str = "Hello World!"

print(str[0])
print(str[2:])
print(str[2:7])

# str "+", "*" test
str = 'hello world'
print(str + " example python" + " is F U N !")
print(str * 2)
"""

"""
# list test
a = [1, 1, 1, 2, 3, 4]
b = [1, 'a', "hello world", 5.0] # 여러가지 형식의 데이터 list
c = [] # 빈 리스트 만들기("c = list()"로도 만들 수 있음)

print(a + b)
print(a * 2)
print(len(a)) # len(list) -> 리스트의 길이 반환
print(a.count(1)) # list.count(A) -> 리스트 내부 "A"의 개수 반환

a[1] = 29 # list[i] = A -> 리스트 내부 i번 index item을 "A"로 변환

print(a)

del a[1:3] # del list[i] -> 리스트 내부 i번 index item을 삭제

print(a)

a.remove(1) # list.remove(A) -> 리스트 내부 "A" 삭제 / del은 index기준으로 판단, remove는 item 기준으로 판단 / "A"가 복수일 경우, 첫번째 index만 삭제

print(a)

a += b
a.pop()

print(a)
print(a.pop(4))
print(a)

a_remove_failed = a.remove(3)

print(a_remove_failed) # list.remove(A) -> remove는 삭제라는 행위만 해주고, 결과를 반환하지 않기 때문에, 해당 식은 "None"의 결과로 나타남, 어떤 기능이 반환값이 존재하고 어떤 기능이 반환하지 않는지는 외워야함
print(a)

a.append(3) # list.append(A) -> list에 A 추가(마지막 index로 추가) / 단일 item 추가
a.append([5, 6])
a.extend([5]) # list.extend([B]) -> list에 B(list) 추가 / 복수의 item 추가 가능
a.extend([5, 6])
a.insert(1, 10) # list.insert(i, j) -> x번째 index에 j라는 item을 추가 / 기존 x번째 index부터 전부 +1씩 index 뒤로 밀림

c = [4, 2, 3, 10]
c.sort() # list.sort() -> (if list - int) list의 item 값이 작은 순서대로 index 재정렬

b = ["abc", "a", "1", "_a", "a-C-BAL", "123", "11"] # (if list - str) hierarchy : number > special > general
b.sort()
b.reverse() # list.reverse() -> index 반대로
d = b.index("123") # list.index(A) -> list 내부의 A라는 item이 있을 경우, 해당 index를 반환 / 없으면 오류 발생

print(a)
print(c)
print(b)
print(d)
"""

"""
# 다양한 변수 선언 관련 test
b = 1
def Outer():
    a = 3

    def Inner():
        global a
        a = 2
        print("Inner 내부 함수 a:" , a)
    
    Inner()
    print("Outer 내부 함수 a :" , a)

Outer()
print("전역변수 a : " , a)

def Function01():
    c = 3

    def Inner02():
        global b
        nonlocal c
        d = 4
        print(b)
        print(c)
        print(d)
    
    Inner02()

Function01()

# Tuple example
a = ()
b = (1, )
c = (1, 2, 3)
d = 1, 2, 3
e = b + c # (1, 1, 2, 3)
f = d + e

print(f) # (1, 2, 3, 1, 1, 2, 3)
print(len(f))

# set test
a = set()
b = set([1, 2, 3])
c = set("Hello")
d = set([1, 4, 2, 6, 8])

print(a)
print(b)
print(c)
print(b & d)
print(b.intersection(d))
print(b | d)
print(b.union(d))
print(d - b)
print(d.difference(b))

a.add(1)
a.update([1, 2, 3])
b.remove(1)
print(a)
"""

# dict test
a = {}
b = {"a" : 1, "b" : 2, "d" : 4}
c = dict(d = 1, e = 2, f = 3)

print(b["a"])
print(b.get('d'))
print(b.get("d", 0))
print(b.keys())
print(b.values())
print(b.items())

del b["a"]
print(b)

b["c"] = 3
print(b)

a["a"] = 1
a["b"] = [1, 2, 3]
a["c"] = "Hello"
a["d"] = {"e" : 4, "f" : 5}
a["e"] = (1, 2, 3)

print(a)
print("a" in a) # True -> "a" key 존재
print("f" in a) # False -> "f" key 존재X
print(a.clear())
print(a)
