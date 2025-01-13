# zipfile
# zipfile은 여러 개의 파일을 zip 형식으로 합치거나 이를 해제할 때 사용하는 모듈이다.
# 다음과 같은 3개의 텍스트 파일이 있다고 가정해 보자.

# zip 형식으로 합치기 위한 a.txt, b.txt, c.txt 생성

# 이 3개의 텍스트 파일을 하나로 합쳐 'mytext.zip'이라는 파일을 만들고 . 파일을 원래의 텍스트 파일 3개로
# 해제하는 프로그램을 만들려면 어떻게 해야 할까?

import os
print(os.getcwd())

import zipfile

with open("a.txt", 'w') as f:
    f.write("a.txt")

with open("b.txt", 'w') as f:
    f.write("b.txt")

with open("c.txt", 'w') as f:
    f.write("c.txt")

# 파일 합치기
with zipfile.ZipFile('mytext.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')
# with ... as 임시변수는 동작이 끝난 후 자동으로 자원을 반환한다.
# mysip은 임수 변수로 zipfile.Zipfile()의 결과를 myzip 변수로 받아 사용

# 해제하기
# with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()

# txt 파일 삭제하기
os.remove('a.txt')
os.remove('b.txt')
os.remove('c.txt')

# ZipFile 객체의 write() 함수로 개별 파일을 추가할 수 있고 extractall() 함수를 사용하면 모든
# 파일을 해제할 수 있다.

# 합친 파일에서 특정 파일만 해제하고 싶다면 다음과 같이 extract() 함수를 사용하면 된다.
# 특정 파일만 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extract('a.txt')

# zipfile 삭제하기
os.remove('mytext.zip')

# 만약 파일을 압축하여 묶고 싶은 경우에는 compression, compresslevel 옵션을 사용할 수 있다.

# 압축하여 묶기
with zipfile.ZipFile('mytext.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:
    myzip.write('a.txt')

# compression에는 4가지 종류가 있다.

# ZIP_STORED: 압축하지 않고 파일을 zip으로만 묶는다. 속도가 빠르다.
# ZIP_DEFLATED: 일반적인 zip 압축으로 속도가 빠르고 압축률은 낮다(호환성이 좋다).
# ZIP_BZIP: bzip2 압축으로 압축률이 높고 속도가 느리다.
# ZIP_LZMA: lzma 압축으로 압축률이 높고 속도가 느리다(7zip과 동일한 알고리즘으로 알려져 있다).

# compressionlevel은 압축 수준을 의미하는 숫자값으로, 1~9를 사용한다.
# 1은 속도가 가장 빠르지만 압축률이 낮고, 9는 속도는 가장 느리지만 압축률이 높다.





