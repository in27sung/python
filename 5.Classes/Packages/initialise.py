# __init__.py 의 용도
# 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 함.
# 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면
# 패키지로 인식되지 않는다.

# 패키지 변수 및 함수 정의
# game 패키지의 __init__.py 파일에 공통 변수나 함수를 정의할 수 있다.
# game 패키지의 __init__.py에 VERSION 변수와 print_version_info() 함수를 정의

import game
print(game.VERSION) # 3.5 출력
game.print_version_info()

# 패키지 내 모듈을 미리 import
# __init__.py 파일에 패키지 내의 다른 모듈을 미리 import하여 패키지를 사용하는
# 코드에서 간편하게 접근할 수 있게 함.
# game 패키지의 __init__.py 파일에 from.graphic.render import render_test 추가
game.render_test()

# render_test()

# 패키지 초기화
# __init__.py 파일에 패키지를 처음 불러올 때 실행되어야 하는 코드를 작성할 수 있음.
# game 패키지의 __init__.py에 print("Initializing game...) 를 추가하면
# import game 시 "Initializing game ...' 출력됨

# game 패키지의 하위 모듈의 함수를 import할 경우에도 실행됨
from game.graphic.render import render_test
render_test()
# Initializing game...
# render
# -> 단, 초기화 코드는 한 번 실행된 후에는 다시 import를 수행하더라도 실행되지 않는다.



