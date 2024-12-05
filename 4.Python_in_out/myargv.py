# Q8 입력값을 모두 더해 출력하기
# 다음과 같이 실행할 때 입력값을 모두 더해 출력하는 스크립트(/myargv.py)를 작성해보자

import sys

args = sys.argv[1:]
sum = 0
for i in args:
    sum += int(i)
print(sum)