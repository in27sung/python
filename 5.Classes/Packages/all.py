# __all__
from game.sound import *
echo.echo_test()
# 오류 발생! NameError: name 'echo' is not defined
# 특정 디렉터리의 모듈을 '*'를 사용하여 import 할 때는 해당 디렉터리의 __init__.py 파일에
# __all__ 변수를 설정하고 import할 수 있는 모듈을 정의해야 한다.
# /Users/Insung/Documents/doit/game/sound/__init__.py 파일에 __all__ = ['echo'] 추가 저장
# 다시 echo.echo_test()를 실행하면 오류가 발생하지 않는다.
from game.sound import*
echo.echo_test()

# from game.sound.echo import * 와 from game.sound import * 는 다르다.
# __all__과 상관없이 무조건 import 되는 경우는 from a.b.c import * 에서
# from의 마지막 항목인 c 가 모듈인 경우이다.
# - sound는 패키지이다.

# 1분 코딩
# '*'를 사용하여 render.py 파일 안의 render_test 함수 사용하기!
from game.graphic.render import *
render_test()
# 또는
# game.graphic의 패키지의 __init__.py에 __all__=['render'] 추가 후
from game.graphic import *
# render.render_test()

