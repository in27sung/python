# shutil
# shutil은 파일을 복사(copy)하거나 이동(move)할 때 사용하는 모듈
# 작업 중인 파일을 자동으로 백업하는 기능을 구현하고자 Users/Insung/Documents/doit/a.txt를 Users/Insung/Documents/temp/a.txt.bak
# 이라는 이름으로 복사하는 프로그램을 만들고자 함
# 백업용으로 사용할 temp 폴더가 없으면 shutil.copy() 함수가 동작하지 않을 수 있다.

print('a.txt를 생성하고 a.txt.bak 백업파일도 생성합니다.')

# Users/Insung/Documents/temp/a.txt를 생성
f = open("/Users/Insung/Documents/doit/a.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄 입니다. \n" %i
    f.write(data)
f.close()

# 백업 파일이 저장될 temp 폴더 생성

# 백업 기능 구현
import shutil

shutil.copy('/Users/Insung/Documents/doit/a.txt', "/Users/Insung/Documents/temp/a.txt.bak")