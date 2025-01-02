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








