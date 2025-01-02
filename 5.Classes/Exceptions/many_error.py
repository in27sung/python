# 여러 개의 오류 처리하기
# -> try 문 안에서 여러 개의 오류를 처리할 때 사용
# <Syntax>
# try:
#     ...
# except 발생 오류1:
#     ...
# except 발생 오류2:
#     ...

print('-' * 80)

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except IndexError:
    print("인덱싱을 할 수 없습니다.")
# 두 오류 중 처음으로 만나는 인덱싱을 오류를 처리하게 되면
# 0으로 나누어서 발생하는 오류는 실행 되지 않게 된다.

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)


