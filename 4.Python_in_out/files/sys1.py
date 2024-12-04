
# 파이썬에서는 sys 모듈을 사용하여 매개변수를 직접 줄 수 있다.
# sys 모듈을 사용하려면 import 명령어를 사용한다.
import sys

args = sys.argv[1:]
print(type(args))
for i in args:
    print(i)
# 입력 받은 인수를 for문을 통해 하나씩 차례대로 출력
# sys 모듈의 argv는 명령차에서 입력한 인수를 의미함.

# 왼쪽 항목의 >_ 버튼을 클릭 터미널창을 열기
# 프로젝트 경로가 시작 경로이고, 'cd /4.Python_in_out' 명령어로
# sys1.py 파일이 있는 위치로 이동

# python    sys1.py    aaa      bbb     ccc
#           argv[0]  argv[1]  argv[2]  argv[3]