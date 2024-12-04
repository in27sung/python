# with 문과 함께 사용하기
f = open("foo.txt", 'w') # 파일 열기
f.write("Life is too short, you need python \n")
f.close() # 파일 닫기

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python \n")