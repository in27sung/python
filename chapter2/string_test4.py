
#1. 아래의 전화번호에서 하이픈('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))

# 2. 1번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
print(phone_number.replace('-',''))

# 3. url에 저장된 웹페이지 주소에서 도메인주소 중 'kr'을 출력하세요.
url = "http://www.itwillbs.co.kr"
print(url.split('.')[3])

# 4. 문자열의 문자를 인덱싱을 통해 직접 변경할 수 없지만 replace 메서드를 사용하여 이를 해결 할 수 있습니다.
string = 'abcdfe2a354a32a'
# 소문자 'a'를 대문자 'A'로 변경하려면 어떻게 해야 할지 생각해보세요.
print(string.replace('a','A'))

# 5. 아래의 코드를 실행하고 결과에 대해서 생각해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string)

# 6. 문자열의 좌우의 공백이 있을 때 이를 제거하고 출력해보세요.
data = "  itwill  "
print(data.strip())

# 7. 다음과 같은 문자열이 있을 때 이를 대문자 ITWILL_BUSAN으로 변경하세요.
a = "itwill_busan"
print(a.upper())

