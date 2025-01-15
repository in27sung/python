# 클래스 상속받고 메서드 추가하기 1
# 다음은 Calculator 클래스이다.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

# 이 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자. 즉,
# 다음과 같이 동작하는 클래스를 만들어야 한다.

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# 클래스 상속받고 메서드 추가하기 2
# 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.
# 즉, 다음과 같이 동작해야 한다.

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val

        if self.value > 100:
             self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# 참과 거짓 예측하기
# 다음 결과를 예측해 보자.
all([1, 2, abs(-3)-3]) #[1, 2, 0]
# False
# 요소 0은 거짓이므로 False를 리턴한다.

chr(ord('a')) == 'a'
# True
# ord(c)는 문자의 유니코드 숫자 값을 리턴하는 함수. ord('a')는 97를 리턴
# chr(i)는 유니코드 숫자값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수.
# chr(97)은 'a'를 리턴한다.

# 음수 제거하기
# filter와 lambda를 사용하여 리스트[1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
list_num = [1, -2, 3, -5, 8, -3]

def positive(x):
    if x > 0:
        return x
filter_value = filter(positive, list_num)
print(list(filter_value))

print(list(filter(lambda x:x > 0, [1, -2, 3, -5, 8, -3])))

# 16진수를 10진수로 변경하기
# 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
print(hex(234))

print(int('0xea', 16))

# 리스트 항목마다 3 곱하여 리턴하기
# map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.

print(list(map(lambda x: x * 3, [1, 2, 3, 4])))

# 최댓값과 최솟값의 합
# 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
num_list = [-8, 2, 7, 5, -3, 5, 0, 1]

max_value = max(num_list)
min_value = min(num_list)

print(f'최댓값: {max_value}')
print(f'최솟값: {min_value}')
print(f'최댓값과 최솟값의 합: {max_value + min_value}')

# 소수점 반올림하기
# 17/3의 결과는 다음과 같다.
print(round(17 / 3, 4))

# 디렉터리 이동하고 파일 목록 출력하기
# os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
import os
# 1. /Users/Insung/Documents/doit 디렉터리로 이동한다.
os.chdir("/Users/Insung/Documents/doit")
print(os.getcwd())
# 2. dir 명령을 실행하고 그 결과를 변수에 담는다.
result = os.popen("ls")

# 3. dir 명령의 결과를 출력한다.
print(result.read())
print(type(result))

# 파일 확장자가 .py인 파일만 찾기
# glob 모듈을 사용하여 /doit 디렉터리의 파일 중 확자앚가 .py인 파일만 출력하는 프로그램을 작성해보자.
import glob
print(glob.glob("/Users/Insung/Documents/doit/*.py"))

# 날짜 표시하기
# time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
import time

strftime = time.strftime('%x %X', time.localtime(time.time()))
print(strftime)

# 로또 번호 생성하기
# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단, 중복된 숫자가 있으면 안 됨).
import random
def lotto():
    return sorted(random.sample(range(1, 46), 6))

print(lotto())

# 누나는 영철이보다 며칠 더 먼저 태어났을까?
# 영철이 누나의 생일은 1995년 11월 20일이고 영철이의 생일은 1998년 10월 6일이다. 영철이 누나는
# 영철이보다 며칠 더 먼저 태어났을까?
import datetime

birth1 = datetime.date(1995, 11, 20)
birth2 = datetime.date(1998, 10, 6)

difference = birth2 - birth1
print(f'영철이 누나는 영철이보다 {difference.days}일 먼저 태어났다.')

# 기록순으로 정렬하기
# 다음은 1학년 3반 학생들의 100m 달리기 기록이다.
# 기록순으로 data를 정렬해 보자.

from faker import Faker
faker = Faker('ko-KR')
test_data

data = [('윤서현', 15.25),
        ('김예지', 13.31),
        ('박예원', 15.34),
        ('송순자', 15.57),
        ('김시우', 15.48),
        ('배숙자', 17.9),
        ('전정웅', 13.39),
        ('김혜진', 16.63),
        ('최보람', 17.14),
        ('한지영', 14.83),
        ('이성호', 17.7),
        ('김옥순', 16.71),
        ('황민지', 17.65),
        ('김영철', 16.7),
        ('주병철', 15.67),
        ('박상현', 14.16),
        ('김영순', 14.81),
        ('오지아', 15.13),
        ('윤지은', 16.93),
        ('문재호', 16.39)]

from operator import itemgetter

result = sorted(data, key=itemgetter(1))
print(result)

# 청소 당번 2명 뽑기
# 다음 4명의 학생 중 청소 당번 2명을 뽑을 수 있는 경우의 수를 모두 나열하시오.
import itertools
students = ['나지혜', '성성민', '윤지현', '김정숙']

# 2명의 조합을 생성
combinations = list(itertools.combinations(students, 2))

# 출력
print(combinations)

# 문자열 나열하기
# "abcd" 문자열을 나열하는 경우의 수를 다음과 같이 모두 출력하시오.

# 5명에게 할 일 부여하기
# 다음 3명이 있다.
['김승현', '김진호', '강춘자', '이예준', '김현주']