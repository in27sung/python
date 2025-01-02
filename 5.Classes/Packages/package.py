
# 패키지(Packages)는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로
# 관리할 수 있게 해준다.
# 모듈 이름이 A.B 인 경우 A는 패키지 이름이 되고, B는 A 패키지의 모듈이 된다.
# 파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어 진다.

# 패키지 만들기(p.216)
# /Users/Insung/Documents/doit/game
# /Users/Insung/Documents/doit/game/graphic
# /Users/Insung/Documents/doit/game/play
# /Users/Insung/Documents/doit/game/sound
# /Users/Insung/Documents/doit/game/__init__.py

import sys

from game.graphic.render import render_test

sys.path.append("/Users/Insung/Documents/doit")
print(sys.path)

# 패키지 안의 함수 실행하기
# 1. echo 모듈을 import 하여 실행하는 방법
import game.sound.echo
game.sound.echo.echo_test()

# 2. echo 모듈이 있는 디렉터리까지 from ... import 하여 실행하는 방법
from game.sound import echo
echo.echo_test()

# 3. echo 모듈의 echo_test 함수를 직접 import 하여 실행하는 방법
from game.sound.echo import echo_test
echo_test()

# 불가능한 경우
# 1) import game만 수행하면 game 디렉터리의 모듈 또는 game 디렉터리의 __init__.py 에
#    정의한 것만 참조할 수 있다.
# import game
# game.sound.echo_test()
# 오류 발생! AttributeError: module 'game' has no attribute 'sound'

# 2. echo_test 함수를 한 번에 직접 import 하는 경우도 불가능
# import game.sound.echo.echo_test
# 오류 발생! No module named 'echo_test'
# 도트 연산자(.)를 사용해서 import a.b.c 처럼 import할 때 가장 마지막 항목 c는
# 반드시 모듈 또는 패키지여야만 한다.
# import 마지막이 '함수'면 안됨





