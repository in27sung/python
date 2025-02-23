# 표준 라이브러리

# 파이썬 표준 라이브러리 - 전 세계 파이썬 고수들이 만든 유용한 프로그램을 모아 놓은 것
# 모든 라이브러리를 다 알 필요는 없으며 어떤 일을 할 때 어던 라이브러리를 사용해야 한다는
# 것 정도만 알면 된다.

# datetime.date
# datetime.date는 연, 월, 일로 날짜를 표현할 때 사용하는 함수이다.
# 만약 A 군과 B 양이 2021년 12월 14일부터 만나기 시작 했다면 2025년 1월 1일은
# 사귄 지 며칠째 되는 날일까?
import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2025, 1, 1)

diff = day2 - day1
print(diff.days)
# day2에서 day1을 빼면 datetime 모듈의 timedelta 객체가 리턴된다. 이 객체를 diff 변수에
# 대입하고 이 diff 변수를 이용하여 두 날짜의 차이를 쉽게 확인해 봤다.

# 요일은 datetime.date 객체의 weekday함수를 사용하면 쉽게 구할 수 있다.
day = datetime.date(2021, 12, 14)
print(day.weekday()) # 1
# 2021년 12월 14일은 화요일

# 0은 월요일을 의미하며 순서대로 1은 화요일, 2는 수요일, ..., 6은 일요일이 된다.
# 이와 달리 월요일은 1, 화요일은 2, ..., 일요일은 7을 리턴하려면 다음처럼 isoweekday 함수를 사용하면 된다.
print(day.isoweekday())

# time
# 시간과 관련된 time 모듈에는 함수가 매우 많다. 그중 가장 유용한 몇 가지만 알아보자.

# time.time
# time.time()은 UTC(universal time coordinated - 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 리턴하는
# 함수이다. 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴해 준다.
import time
print(time.time())

# time.localtime
# time.localtime은 time.time()이 리턴한 실숫값을 사용해서 연, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수이다.

print(time.localtime(time.time()))

# time.asctime
# time.asctime은 time.localtime가 리턴된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수이다.
print(time.asctime(time.localtime(time.time())))

# time.ctime
# time.asctime(time.localtime(time.time()))은 간단하게 time.ctime()으로 표시할 수 있다.
# ctime이 asctime과 다른 점은 항상 현재 시간만을 리턴한다는 점이다.
print(time.ctime())

# time.strftime
# strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.
# time.strtime('출력할_형식_포맷_코드', time.localtime(time.time()))

format_time = time.strftime('%x', time.localtime(time.time()))
print(format_time)

format_time = time.strftime('%c', time.localtime(time.time()))
print(format_time)

# time.sleep
# time.sleep 함수는 주로 루프 안에서 많이 사용한다. 이 함수를 사용하면 일정한 시간 간격을
# 두고 루프를 실행할 수 있다.
for i in range(3):
    print(i)
    time.sleep(0.5) # 0.5초 간격

# 인수 없이 time 함수 사용하기
# time.localtime, time.asctime, time.strftime 함수는 입력 인수 없이 사용할 수 있다. 이럴 경우
# 현재 시각을 기준으로 함수가 수행된다.
print(time.localtime())

print(time.asctime())

print(time.strftime('%c'))

print('-' * 80)

# math.gcd
# math.gcd 함수를 이용하면 최대 공약수(greatest common divisor)를 쉽게 구할 수 있다.
# 어린이집에서 사탕 60개, 초콜릿 100개, 젤리 80개를 준비했다. 똑같이 나누어 봉지에 담는다면
# 최대 몇 봉지까지 만들 수 있을까?
import math
snack = math.gcd(60, 100, 80)
print(snack) # 20

print(60/20, 100/20, 80/20)
# -> 3.0, 5.0, 4.0
# 한 봉지당 사탕 3개씩, 초콜릿 5개씩, 젤리 4개씩 담으면 된다.

# math.lcm
# math.lcm은 최소 공배수(least common multiple)를 구할 떄 사용하는 함수
# 정류장에 시내버스는 15분, 마을버스는 25분마다 도착한다고 한다.
# 오후 1시에 두 버스가 동시에 도착했다고 할 때 두 버스가 동시에 도착할 다음 시각을 알려면 어떻게
# 해야할까?

print(math.lcm(15, 25))
# 최소 공배수는 75이다. 즉, 1시 이후 75분 이후에 다시 두 버스는 동시에 정류장에 도착
# 2시 15분

print('-' * 80)

# random
# random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
# 먼저 random과 randint 함수에 대해 알아보자.
import random
print(random.random())
#  0.0 ~ 1.0 사이의 실수 중에서 난수값을 리턴

print(random.randint(1, 10))
# 1 ~ 10 사이의 정수 중에서 난수 값을 리턴

print(random.randint(1, 100))
# 1 ~ 100

import random_pop
data = [1, 2, 3, 4, 5]
while data:
    print(random_pop.random_pop2(data))

# glob
# 특정 디렉터리에 이쓴ㄴ 파일 이름 모두를 알아야 할 때가 있다. 이럴 때 사용하는 모듈이 바로 glob이다.

import glob
result = glob.glob("/Users/Insung/Documents/doit*")
print(result)

# pickle
# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여준다.

import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

# pickle.dump로 저장한 파일을 pcikle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예이다.
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)

# OS
# os 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해 주는 모듈이다.

# os.environ
# 내 시스템의 환경 변숫값을 알고 싶을 때
# 시스템은 제각기 다른 환경 변숫값을 가지고 있는데, os.environ은 현재 시스템의 환경 변숫값을 리턴한다.

import os
os.environ

# os.environ은 환경 변수에 대한 정보를 딕셔너리 형태로 구성된 environ 객체로 리턴한다.
# 자세히 보면 여러 가지 유요한 정보를 찾을 수 있다.

# print(os.environ['PATH'])

# os.chdir(디렉터리 위치 변경하기)
# os.chdir를 사용하면 다음과 같이 현재 디렉터리의 위치를 변경할 수 있다.
os.chdir("/Users/Insung/Documents/doit")

# os.getcwd(디렉터리 위치 돌려받기)
print(os.getcwd())

# os.system(시스템 명령어 호출하기)
# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다. os.system("명령어")처럼 사용한다.
# 다음은 현재 디렉터리에서 시스템 명령어 dir을 실행하는 예이다.

os.system("ls")

# os.popen(실행한 시스템 명령어의 결괏값 돌려받기)
# os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 리턴한다.
f = os.popen("ls")

# 읽어 들인 파일 객체의 내용을 보기 위해서는 다음과 같이 하면 된다.
print(f.read())

# tempfile
# 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다. tempfile.mkstemp()는
# 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴한다.

import tempfile
filename = tempfile.mkstemp()
print(filename)

# tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 리턴한다. 이 파일은
# 기본적으로 바이너리 쓰기 모드(wb)를 갖는다. f.close()가 호출되면 이 파일은 자동으로 삭제된다.

import tempfile
f = tempfile.TemporaryFile()
f.close()
