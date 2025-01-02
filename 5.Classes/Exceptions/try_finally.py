from ast import Index

# try-finally 문
# finally 절은 try문 수행 도중 예외 발생 여부에 상관 없이 항상 수행된다.
# 보통 finally절은 사용한 리소스를 close해야 할 때 많이 사용한다.

try:
    f = open('foo.txt', 'w')
    # 파일 수행
finally:
    f.close()
    # 중간에 오류가 발생하더라도 무조건 실행

