
# 함수를 사용하는 이유?
# 1. 반복적으로 사용하는 가치 있는 부분을 함수로 정의한다.
# 2. 프로그램 흐름을 일목요연하게 볼 수 있기 때문이다.

# 파이썬 함수 구조
# def 함수_이름(parameter):
#   수행할 문장1
#   수행할 문장2
#   ...

# 함수의 이름은 add이고 입력으로 2개의 값을 받으며 리턴값(출력값)은 2개의 입력값을 더한 값이다.
def add(a, b):
    return a + b

add(1, 2)

# 매개변수(parameter), 인수(arguments)
# 매개변수는 함수에 입력으로 전달될 값을 받는 변수
# 인수는 함수를 호출할 때 전달하는 입력값

# 함수의 형태 4가지
# 1. 일반적인 함수: 입력값 - O, 리턴값(결과값) - O
def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)
# 결과값을 받을 변수 = 함수이름(입력인수1, 입력인수2)

# 2. 입력값이 없는 함수 : 입력값 - X, 리턴값 - O
def say():
    return 'Hi'

a = say()
print(a)

# 3. 리턴값이 없는 함수: 입력값 - O, 리턴값 - X
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))

add(3, 4)

#  4. 입력값도 리턴값도 없는 함수: 입력값 - X, 리턴값 - X
def say():
    print("Hi")

say()

# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)

# 매개변수를 지정하면 다음과 같이 순서에 상관없이 사용할 수 있다.
result = sub(b=5, a=3)
print(result)

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
# def 함수_이름(*매개변수):
#     수행할_문장
#     ...

# 여러 개의 입력값을 받는 함수 만들기
# args는 인수를 뜻하는 영어 단어 arguments의 약자이며 관례적으로 자주 사용한다.
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

print('-' * 80)
# 키워드 매개변수, kwargs
# 매개변수 이름 앞에 ** 두 개를 쓰면 딕셔너리가 되고 key=value 형태의 결괏값이 저장됨
#  kwargs: keyword arguments
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name='foo', age=3)

# 함수의 리턴값은 언제나 하나이다.
def add_and_mul(a, b):
    return a+b, a*b

# 오류가 발생하지 않고 함수의 리턴값이 튜플로 저장되었다 (a+b,a*b)
result = add_and_mul(3, 4)
print(result)
print(type(result))

result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)

def add_and_mul(a, b):
    return a + b # 첫 return문을 만나는 순간, 리턴값을 돌려 준 다음 함수를 빠져나가게 된다.
    return a * b

result = add_and_mul(2, 3)
print(result)

# return의 또 다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)

say_nick('야호')
# return 문이 실행되어 함수를 빠져나왔다.
say_nick('바보')

# 매개변수에 초깃값 미리 설정하기
# 매개변수에 들어갈 값이 항상 변하는 것이 아닐 경우 초깃값을 미리 설정할 수 있음

print('-' * 80)
def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)

say_myself("황인성", 27, True)


# Error: non-default parameter follows default parameter
# def say_myself(name, man=True, age):
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 %d살입니다." % age)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
# -> 초깃값을 설정한 매개변수의 위치는 항상 뒤쪽에 놓아야 한다

print('-' * 80)
# 함수 안에서 선언한 변수의 효력 범위
a = 1 # 한수 밖의 변수 a
def vartest(a): # vartest 함수 선언
    a = a + 1

vartest(a) # vartest 함수의 입력값으로 a를 대입
print(a) # a 값 출력

def vartest(hello):
    hello = hello + 1

vartest(a) # vartest 함수의 입력값으로 a를 대입
print(a)

print('-' * 80)
# 한수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a) # vartest(a)의 결괏값을 함수 밖의 변수 a에 대입
print(a)

# 2. global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a + 1
vartest()
print(a)
# global 명령어는 함수 밖의 변수를 직접 사용하겠다는 의미
# global 명령어는 사용하지 않는 것을 추천 - 함수는 독립적으로 존재하는 것이 좋기 때문
# 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아님

print('-' * 80)
# lambda
# 함수를 한줄로 간결하게 만들 때 사용
# lambda 매개변수1, 매개변수2, ...: 매개변수를 이용한 표현식
add = lambda a, b: a + b
result = add(3, 4)
print(result)
