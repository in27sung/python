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
for i in range(10):
    print(i)
    time.sleep(0.5) # 0.5초 간격

# 인수 없이 time 함수 사용하기
# time.localtime, time.asctime, time.strftime 함수는 입력 인수 없이 사용할 수 있다. 이럴 경우
# 현재 시각을 기준으로 함수가 수행된다.
print(time.localtime())

print(time.asctime())

print(time.strftime('%c'))








