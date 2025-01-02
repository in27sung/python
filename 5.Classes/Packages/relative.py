
# relative 패키지
# graphic 패키지의 render.py 모듈이 sound 패키지 echo.py 모듈을 사용하고 싶다면?
# render.py 파일을 수정
# render.py-------------------------------------------------------------------
# from game.sound.echo import echo_test
# def render_test():
#     print("render")
#     echo_test()
# ----------------------------------------------------------------------------
# 다른 디렉터리(패키지)에 있는 함수는 import를 하지 않고는 사용할 수 없다.

from game.graphic.render import render_test
render_test()

# 만약, 상대 경로를 통해 relative하게 import를 하려면
# render.py 파일을 수정
# from ..sound.echo import echo_test 으로 수정하면
# 상대 경로를 사용하여 .. 를 통해 game 디렉터리로 이동하고 sound.echo 모듈에 접근 
