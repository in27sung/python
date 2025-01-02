# 내장 함수
# -> 외부 모듈과는 달리 import가 필요로 하지 않는 함수를 말함
#  -> 이미 만들어진 프로그램은 테스트 과정을 수 없이 거쳤기 때문에 충분히 검증되어 있다.
from idlelib.macosx import hideTkConsole

# 내장 함수 살펴보기
# abs
# -> abs(x)는 어떤 숫자를 입력받을 때 그 숫자의 절대값을 리턴한느 함수이다.
print(abs(3)) # 3
print(abs(-3)) # 3
print(abs(-1.2)) # 1.2

print('-' * 80)

# all
# all(x)는 반복 가능한 데이터 x를 입력밧으로 받으며 이 x의 요소가 모두 참이면 True,
# 거짓이 하나라도 있으면 False를 리턴
# 여기서 반복 가능한 데이터란 for문에서 사용할 수 있는 자료형을 말하며
# 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.

result = all([1, 2, 3])
print(result)
# 리스트 [1, 2, 3]은 모든 요소가 참이므로 True 리턴

result = all([1, 2, 3, 0])
print(result) # False
# 리스트[1, 2, 3, 0] 중에서 요소 0은 거짓이므로 False를 리턴한다.

result = all([])
print(result) # True
# all의 입력 인수가 빈 값인 경우에는 Treu를 리턴한다.

# any
# any(x)는 반복 가능한 데이터 x를 입력 받아 x의 요소 중 하나라도 참이 있으면 True를 리턴하고 x가
# 모두 거짓일 때만 False를 리턴한다. 즉, all(x)의 반대로 작동한다.
result = any([1, 2, 3, 0])
print(result) # True

result = any([0, ""])
print(result) # False

result = any([])
print(result)
# 만약 any의 입력 인수가 빈 값인 경우에는 False를 리턴한다.

# chr
# chr(i)는 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수이다.
print(chr(97))

print(chr(44032))

# dir
# dir은 객체가 지닌 변수나 함수를 보여 주는 함수이다. 다음 예는 리스트와 딕셔너리가 지닌
# 함수(메서드)를 보여주는 예이다.
print(dir([1, 2, 3]))
# 리스트가 지닌 함수(메서드)를 보여준다.

print(dir({}))
# 딕셔너리가 지닌 함수(메서드)를 보여준다.

# divmod
# divmod(a,b)는 2개의 숫자 a,b를 입력으로 받는다. 그리고 a를 b로 나눈 몫고 나머지를 튜플로 리턴한다.
print(divmod(7,3))

print(7 // 3)
print(7 % 3)

# enumerate
# enumerate는 '열거하다'라는 뜻이다. 이 함수는 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval
# eval(expression)은 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값
# 을 리턴하는 함수이다.

print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

# hex
# hex(x)는 정수를 입력받아 16진수(hexadecimal) 문자열로 변환하여 리턴하는 함수이다.
print(hex(234)) # '0xea'

print(hex(3)) # '0x3'

# id
# id(object)는 객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 리턴하는 함수이다.
a = 3
print(id(3)) # 4356268224
print(id(a)) # 4356268224

b = a
print(id(b)) # 4356268224

print(id(4)) # 4356268256

# input
# input([prompt])는 사용자 입력을 받는 함수이다. 입력 인수로 문자열을 전달하면 그문자열
# 은 프롬프트가 된다. //[]는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이라는 것을 기억하자
# a = input() # hi 입력
# print(a)
# b = input("Enter: ")
# print(b)

# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수이다. 만약 정수가 입력되면 그대로 리턴한다.

print(int('3'))
print(int(3.4))

# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴한다. 예를 들어 2진
# 수로 표현된 '11'의 10진수 값은 다음과 같이 구할 수 있다.
print(int('11', 2))
print(int('1A', 16))

# isinstance
# isinstance(object, class) 함수는 첫 번째 인수로 객체, 두 번째 인수로 클래스를 받는다. 입력으로
# 받은 객체가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 리턴한다.

# 아무런 기능이 없는 Person 클래스 생성
class Person: pass

# Person 클래스의 인스턴스 a 생성
a = Person()

# a가 Person 클래스의 인스턴스인지 확인
print(isinstance(a, Person))

b = 3
# b가 Person 클래스의 인스턴스인지 확인
print(isinstance(b, Person))

# len
# len(s) 는 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수
result = len("python")
print(result) # 6

result = len([1, 2, 3])
print(result) # 3

result = len((1, 'a'))
print(result) # 2

print('-' * 80)

# list
# list(iterable)은 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴하는 함수이다.
print(list("python"))
print(list((1, 2, 3)))

a = [1, 2, 3]
b = list(a)
print(b)

# map
# map(f, iterable)은 함수(f)와 반복 가능한 데이터를 입력으로 받는다. map은 입력받은 데이터의
# 각 요소에 함수 f를 적용한 결과를 리턴하는 함수이다.
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times(x):
    return x * 2

print(list(map(two_times, [1, 2, 3, 4])))

# 먼저 리스트의 첫 번째 요소인 1이 two_times 함수의 입력값으로 들어가고 1 * 2의 과정을 거쳐서 2가 된다.
# 다음으로 리스트의 두 번째 요소인 2가 2 * 2의 과정을 거쳐 4가 된다. 따라서 결괏값은 이제 [2, 4]가 된다.
# 총 4개의 요솟값이 모두 수행되면 [2, 4, 6, 8]이 된다.

# lambda
list(map(lambda a: a*2, [1, 2, 3, 4]))

# max
# max(iterable)은 이수로 반복 가능한 데이터를 입력받아 그 최댓값을 리턴하는 함수이다.
print(max([1, 2, 3])) # 3

print(max("python")) # y

# min
# min(iterable)은 max 함수와 반대로, 인수로 반복 가능한 데이터를 입력받아 그 최솟값을
# 리턴하는 함수이다.

print(min([1, 2, 3])) # 1
print(min("python")) # h

# oct
# oct(x)는 정수를 8진수 문자열로 바꾸어 리턴하는 함수이다.
print(oct(34))
print(oct(12345))

# open
# open(filename, [mode])은 '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 리턴하는
# 함수이다. 읽기 방법(mode)을 생략하면 기본 값인 읽기 모드(r)로 파일 객체를 만들어 리턴한다.
# b는 w, r, a와 함께 사용한다. 예를 들어 rb는 '바이너리 읽기 모드'를 의미한다.
# ---------------------------------------------
#       mode           |           설명
#       w                쓰기 모드로 파일 열기
#       r                읽기 모드로 파일 열기
#       a                추가 모드로 파일 열기
#       b                바이너리 모드로 파일 열기
# ---------------------------------------------


# f = open("binary_file", "rb")

# ord
# ord(c)는 문자의 유니코드 숫자 값을 리턴하는 함수이다.
print(ord('a')) # 97

print(ord('가')) # 44032

# pow
# pow(x, y)는 x를 y제곱한 결괏값을 리턴하는 함수이다.
print(pow(2, 4))

print(pow(3, 3))

# range
# range([start,] stop [,step])은 for 문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에
# 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴한다.

# 인수가 하나일 경우
# 시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.
print(list(range(5)))

# 인수가 2개일 경우
# 입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타낸다. 단, 끝 숫자는 해당 범위에 포함되지 않는다는 것에 주의하자.
print(list(range(5, 10)))

# 인수가 3개일 경우
# 세 번째 인수는 숫자 사이의 거리를 말한다.
print(list(range(1, 10, 2)))

# 0부터 -9까지, 숫자 사이의 거리는 -1
print(list(range(0, -10, -1)))

# round
# round(number [,ndigits])는 숫자를 입력받아 반올림해 리턴하는 함수이다.
print(round(4.6))

print(round(4.2))

# 실수 5.678을 소수점 2자리까지만 반올림하여 표시할 수 있다.
print(round(5.678, 2)) # 5.68
print(round(5.678, -1)) # 10.0

# round 함수의 두 번째 인수는 반올림하여 표시하고 싶은 소수점의 자릿수(ndigits)를 의미한다.

# sorted
# sorted(iterable)는 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴하는 함수이다.
print(sorted([3, 1, 2]))

print(sorted(['a', 'c', 'b']))

print(sorted("zero"))

print(sorted((3, 2, 1)))
# 리스트 자료형에도 sort 함수가 있다. 하지만 리스트 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 할 뿐,
# 정렬된 결과를 리턴하지는 않는다.

# str
# srt(object)는 문자열 형태로 객체를 변환하여 리턴하는 함수이다.
print(str(3))

print(str('hi'))

# sum
# sum(iterable)은 입력 데이터의 합을 리턴하는 함수이다.
print(sum([1, 2, 3]))

print(sum((4, 5, 6)))

# tuple
# tupe(iterable)은 반복 가능한 데이터를 튜플로 바꾸어 리턴하는 함수이다. 만약 입력이 튜플인
# 경우에는 그대로 리턴한다.
# 튜플 수정 불가
# 리스트 수정 가능
print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

# type
# type(object)은 입력값의 자료형이 무엇인지 알려주는 함수
print(type("abc")) # <class 'str'>
print(type([])) # <class 'list'>

result = type(open("test", 'w'))
print(result)

# zip
# zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수이다.
# *iterable은 반복 가능한 데이터를 여러 개 입력할 수 있다는 의미이다.

print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))





