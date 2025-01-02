
# 오류 회피하기
# 특정 오류가 발생할 경우 그냥 통과시킬 때 사용

try:
    f = open("나없는파일", "r")
except FileNotFoundError: # 파일이 없더라도 오류가 발생하지 않고 통과
    pass

