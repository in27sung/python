# 예외 처리
# try except를 사용하여 예외적으로 오류를 처리할 수 있다.

# 오류 발생 예
# 1. 디렉터리 안에 없는 파일을 열러고 시도했을 때 발생하는 오류
# f = open("나없는파일.txt", 'r')
# FileNotFoundError: [Errno 2] No such file or directory: '나없는파일.txt'

# 2. 0으로 다른 숫자를 나누느 경우 발생하는 오류
# 4 / 0
# ZeroDivisionError: division by zero

# 3. 리스트의 인덱스를 벗어나는 인덱싱 시 발생하는 오류
# a = [1, 2, 3]
# a[4]
# IndexError: list index out of range

# 오류 예외 처리 기법
# try-except 문
# <Syntax>
# try:
#     ...
# except[발생한 오류[as 오류메시지 변수]]:
#     ...
# - try 블록 수행 중 오류가 발생하면 except 블록이 수행됨
# 오류가 발생하지 않는다면 except 블록은 수행되지 않음

# except 구문 처리 방법
# 1. try except만 쓰는 방법
try:
    ...
except:
    ...
# - 이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행

# 2. 발생 오류만 포함한 except문
# try:
#     not ...
# except 발생 오류:
#     ...
# - 이 경우는 오류가 발생했을 때 except 문에 미리 정해 놓은
#   오류 이름과 일치할 때만 except 블록을 수행

# 3. 발생 오류와 오류 메시지 변수까지 포함한 except문
# try:
#     ...
# except 발생_오류 as 오류_변수:
#     ...
# - 이 경우 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용

# 1분 코딩
# list의 범위를 벗어나는 접근을 했을 시
# list index out of range가 출력되도록 작성

list = [1, 2, 3]
try:
    print(list[3])
except IndexError as e:
    print(e)
# - list index out of range








