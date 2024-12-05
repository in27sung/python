from select import select

#
result = 0

def add(num):
    global result # 이전에 계산한 결괏값을 유지하기 위해서 result 전역 변수(global)를 사용
    result += num # 결괏값(rusult)에 입력값(num) 더하기
    return result # 결괏값 리턴

print(add(3))
print(add(4))


print('-' * 80)
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

print('-' * 80)
# 클래스 정의
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    # 빼기 기능 추가
    def sub(self, num):
        self.result -= num
        return self.result


# 객체 생성
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal1.sub(10))
print(cal2.sub(8))

# 객체와 인스턴스
class Cookie:
    pass

a = Cookie()
b = Cookie()
# Cookie()의 결괏값을 리턴받은 a와 b가 바로 객체이다.

# 사칙 연산 클래스 만들기
# 1. 클래스를 어떻게 만들지 먼저 구상하기
# -> 어떤 클래스를 만들지 그림을 그려보자.

# 2. 클래스 구조 만들기
# 일단은 아무 기능이 없는 클래스를 만든다.

class FourCal:
    pass

a = FourCal() # a 객체를 생성, a는 FourCal 클래스의 인스턴스이다.
print(type(a)) # 객체 a의 타입은 FourCal 클래스 이다.
# <class '__main__.Fourcal'>

# 3. 객체에 숫자를 지정할 수 있게 만든다.
class FourCal:
    def setdata(self, first, second): # 메서드의 매개변수
        self.first = first
        self.second = second
    # -> 파이썬에서는 클래스 안에 정의된 함수를 메서드(Method)라고 부른다.

# 3-1. setdata 메서드의 매개변수
a = FourCal()
a.setdata(4, 2)
# 객체를 통해 클래스의 메서드를 호출하려면 도트(.) 연산자를 사용
# setdata 메서드의 파라미터는 self, first, second, 3개인데, 인자값 2개를 쓰는 이유는
# 첫번째 매개변수 self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달되기 때문
# 즉, a.setdata(4, 2)에서 self: a, first: 4, second: 2)

# 메서드의 또 다른 호출 방법
# 파이썬 메서드의 첫번째 매개변수 이름은 관례적으로 self를 사용한다.
# 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self를 사용하는 것인데
# self 말고 다른 이름을 사용해도 된다.

# 만약, '클래스이름.메서드' 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해줘야 한다.
a = FourCal()
FourCal.setdata(a, 4, 2)

# 반면, '객체.메서드' 형태로 ㅊ호출할 때는 self를 반드시 생략해서 호출해야 한다.
a = FourCal()
a.setdata(4, 2)

# 3-2. setdata 메서드의 수행문
def setdata(self, first, second): # 메서드의 매개변수
    self.first = first # 메서드의 수행문
    self.second = second # 메서드의 수행문
# 메서드의 ':' 아래를 '메서드의 수행문' 이라고 함
# a.setdata(4, 2) 처럼 호출하면 setdata 메서드의 매개변수 first, second에는 각각 값 4와 2가 전달되어 setdata 메서드의
# 수행문이 다음과 같이 해석된다.

# self.first = 4
# self.second = 2

a.first = 4
a.second = 2

print('-' * 80)

a = FourCal()
a.setdata(4, 2)
a.first

a.second

# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.
# 아래의 코드에서 b 객체의 객체변수 first 값을 변경해도 a 객체의 first에는 아무런 변화가 없다.
# 독립적이다.
a = FourCal()
b = FourCal()

a.setdata(4, 2)
print(a.first)
print(id(a.first))

b.setdata(3, 7)
print(b.first)
print(id(b.first))
# id 함수는 객체의 주소를 return하는 파이썬 내장 함수



