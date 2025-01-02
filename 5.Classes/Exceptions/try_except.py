# 오류 처리의 예
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
# -ZeroDivisionError: division by zero