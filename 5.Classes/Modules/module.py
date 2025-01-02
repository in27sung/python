# 모듈이란?
# 함수나 변수 또는 클래스를 모아놓은 파일을 말함
# 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일 이라고도 할 수 있다.
from urllib.response import addbase

# 모듈 만들기
# mod1.py 생성

# 모듈 불러오기
import mod1
from mymod import mod3

print(mod1.add(3, 4))

print(mod1.sub(4, 2))

# 모듈 이름 없이 함수 이름만 사용하기
# -> from 모듈이름 import 모듈함수
from mod1 import add
print(add(3, 4))


# add 함수와 sub 함수를 둘 다 사용하고 싶다면
from mod1 import add, sub
print(add(3, 4))
print(sub(4, 3))

print('-' * 80)

# 모든 함수를 사용하고 싶을 때
from mod1 import *
print(add(3, 4))
print(sub(100, 50))

print('-' * 80)

# mod1.py 수정
# mod1.py 에 있는 print(add(1, 4)) print(sub(4, 2))를 추가하고
# mod1.py에 있는 add와 sub 함수를 사용하려고 import를 하면 print문이 실행

# __name__ 변수
# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
# mod1.py를 직접 실행할 경우 __name__ 변수에는 __main__ 값이 저장된다.
# 하지만 다른 파이썬 모듈에서 mod1을 import 할 경우에는 __name__ 변수에
# mod1.py의 모듈 이름 값인 mod1이 저장된다.

import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4)) # add 함수 사용

circle_area = mod2.Math()
print(circle_area.solv(5))
print(mod2.Math.solv(mod2.Math, 5))

# 다른 디렉터리에 있는 모듈을 불러오는 방법
# -> 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법

# /Users/Insung/Documents/doit/mymod 폴더를 생성하고 mod2.py를 mod3.py 이름으로 복사

# 터미널 실행 -> python 실행
# import sys 입력 -> sys.path
# 현재 파이썬 라이브러리가 설치되어 있는 디렉터리 경로를 보여준다.
# 이 디렉터리 안에 저장된 파이썬 모듈은 모듈이 저장된 디렉터리로 이동할 필요없이 바로
# 불러와서 사용할 수 있다.

# sys.path에 경로 추가하기
# sys.path.append(("/Users/Insung/Documents/doit/mymod")
# 마지막에 '/Users/Insung/Documents/doit/mymod'가 추가되어 있다.
# import mod3 -> print(mod3.add(3, 4) 확인
# 현재 파이썬 라이브러리가 설치되어 있는 디렉터리 목록을 보여준다.
# 이 디렉터리 안에 저장된 파이썬 모듈은 모듈이 저장된 디렉터리로 이동할 필요없이 바로

# [ PYTHONPATH 환경 변수 사용하기 ]
# 시스템 환경 변수인 'PYTHONPATH'에 모듈의 위치를 추가하는 방법으로
# 윈도우 시스템 -> 고급 시스템 설정 -> 환경변수 -> 시스템 변수 목록에 'PYTHONPATH'를 검색
# 없으면 새로 만들고 변수 값에 /doit/mymod를 추가
# export PYTHONPATH=/Users/Insung/Documents/doit/mymod 터미널 입력 후 python 실행

# module.py 에 sys.path.append 추가
import sys
sys.path.append("/Users/Insung/Documents/doit/mymod")

import mymod.mod3
print(mod3.add(1, 1))
