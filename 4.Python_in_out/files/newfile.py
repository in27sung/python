# 파일 읽고 쓰기

# 파일 생성하기
f = open("새파일.txt", 'w')
f.close()
# -> 프로그램을 실행한 디렉토리에 새로운 파일이 하나 생성됨
# -> 파이참의 경우 python 경로에 새파일이 생성됨

# open 내장함수
# 파일 객체 = open(파일이름, 파일 열기 모드)
# 파일 열기 모드 r - 읽기모드, w - 쓰기모드, a - 추가모드
# 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용은 모두 사라지고,
# 해당 파일이 존재하지 않으면 새로운 파일 생성

# 파일 경로를 지정하여 파일 생성
f = open("/Users/Insung/Desktop/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)
f.close()

# 만약, Desktop 폴더가 없으면 에러가 발생

# 프로그램 외부에 저장된 파일을 읽는 여러 가지 방법
# 1) readline 함수 사용하기
# -> 파일에서 한 줄을 읽어옴
f = open("/Users/Insung/Desktop/새파일.txt", 'r')
line = f.readline()
print(line)
# 1번째 줄 입니다.


line = f.readline()
print(line)
# 2번째 줄 입니다.

f.close()

# 만약, 모든 줄을 읽어서 화면에 줄력하고 싶다면?
f = open("/Users/Insung/Desktop/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line : break # line 변수가 'flase'인지 판별
    # 빈 문자열이나 None이 반환되면 if not line은 'True'가 되어
    # 더 이상 읽을 내용이 없을 때 이 조건은 참이 된다.
    print(line)
f.close()

# 2. readlines 함수 사용하기
# 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
f = open("/Users/Insung/Desktop/새파일.txt", 'r')
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
print(lines[0]) # 1번째 줄입니다. 출력

# 줄 바꿈(\n) 문자 제거하기
# 파일을 읽을 때 줄 끝의 줄 바꿈(\n) 문자를 제거하고 사용해야 할 경우가 많다. 다음처럼 strip 함수를 사용하면 줄 바꿈 문자를 제거할 수 있다.

for line in lines:
    line = line.strip()
    print(line)
f.close()

print("-" * 80)
# 3. read 함수 사용하기
# f.read()는 파일의 내용 전체를 문자열로 리턴한다. 따라서 data는 파일의 전체 내용이다.
f = open("/Users/Insung/Desktop/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

print("-" * 80)
# 4. 파일 객체를 for 문과 함께 사용하기
f = open("/Users/Insung/Desktop/새파일.txt", 'r')
for line in f:
    print(line)
f.close()
# 파일 객체(f)는 기본적으로 위와 같이 for문과 함께 사용하여 파일을 줄 다누이로 읽을 수 있다.

# 파일에 새로운 내용 추가하기
# 쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다.
# 하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있다. 이런 경우에는
# 파일을 추가 모드('a')로 열면 된다.
f = open("/Users/Insung/Desktop/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()



