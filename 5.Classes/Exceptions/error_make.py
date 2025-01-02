
# 예외 만들기
# - Exception 클래스를 상속하여 직접 예외를 만들어 사용할 수 있다.
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

    say_nick('천사')
    # say_nick('바보')
# 예외 처리 기법을 사용하여 MyError 발생을 예외 처리

# try:
#     say_nick('천사')
#     say_nick('바보')
# except MyError as e:
#     print(e)

try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print("허용되지 않는 별명입니다.")


print('-' * 80)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)

# 오류 메시지를 출력했을 때 오류 메시지가 출력되지 않는다.
# 오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면 오류 클래스에 __str__ 메서드를 구현

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)
# "허용되지 않는 별명입니다. 라는 오류 메시지가 출력됨