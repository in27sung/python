# 입출력과 인코딩

# 1. 입력으로 받은 바이트 문자열은 되도록 빨리 유니코드 문자열로 디코딩한다.
# 2. 함수나 클래스 등에서는 유니코드 문자열만 사용한다.
# 3. 입력에 대한 결과를 전송하는 마지막 부분에서만 유니코드 문자열을 바이트 문자열로 인코딩해서 반환한다.

# 1. euc-kr로 작성된 파일 읽기
with open('euc-kr.txt', encoding='euc-kr') as f:
   data = f.read() # 유니코드 문자열

# 2. unicode 문자열로 프로그램 수행하기
data += '\n' + "추가 문자열"

# 3. euc-kr로 수정된 문자열 저장하기
with open('euc-kr.txt', 'w', encoding='euc-kr') as f:
    f.write(data)

# 파일을 읽는 open() 함수에는 encoding을 지정하여 파일을 읽는 기능이 있다. 이때 읽은 문자열은
# 유니코드 문자열이 된다. 이와 마찬가지로 파일을 만들 때도 encoding을 지정하여 파일을 만들 수 있다.
# encoding 항목을 생략하면 기본값으로 utf-8이 지정된다.

