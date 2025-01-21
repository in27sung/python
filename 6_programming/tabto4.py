import sys

# 문서 파일을 읽어서 그 문서 파일 안에 있는 탭 문자(Tab)를 공백 문자로(Spacebar) 4개로
# 바꿔주는 스크립트를 작성해보자.

# 필요한 기능은? 문서 파일 읽어 들이기 문자열 변경하기
# 입력 받는 값은? 탭을 포함한 문서 파일
# 출력하는 값은? 탭이 공백으로 수정된 문서 파일

src = sys.argv[1]
dst = sys.argv[2]

# print(src)
# print(dst)

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " " * 1)

f = open(dst, 'w')
f.write(space_content)
f.close()
# python tabto4.py a.txt b.txt


