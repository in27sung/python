# traceback
# traceback은 프로그램 실행 중 발생한 오류를 처적하고자 할 때 사용하는 모듈이다.

def a():
    return 1 / 0
def b():
    a()
def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")

main()

# main() 함수가 시작되면 b() 함수를 호출하고 b() 함수에서 다시 a() 함수를 호출하여 1을 0으로
# 나누므로 오류가 발생하여 "오류가 발생했습니다." 라는 메시지를 출력했다.

import traceback

def a():
    return 1 / 0
def b():
    a()
def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())

main()