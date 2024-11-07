
#1. 아래의 전화번호에서 하이픈('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
print("1번 문제 정답:",phone_number.replace('-',' '))

# 2. 1번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
print(f'2번 문제 정답: {phone_number.replace("-","")}')

# 3. url에 저장된 웹페이지 주소에서 도메인주소 중 'kr'을 출력하세요.
url = "http://www.itwillbs.co.kr"
print("3번 문제 정답: %s" % url.split('.')[3])

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

# 8. 다음과 같은 문자열이 있을 때 이를 소문자 class4로 변경하세요.
a = "CLASS4"
print(a.lower())

# 9. 문자열 'itwill_busan'을 'Itwill_busan'으로 변경하세요.
a = "itwill_busan"
print('I' + a[1:])
print(a.capitalize()) #첫글자가 대문자로 변경

# 10. endswith 함수를 사용해서 파일이름의 확장자가 xlsx 또는 xls 인지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))

# 11. startswith 함수를 사용해서 파일이름이 2021로 시작하는지 확인해보세요.
file_name = "2021_보고서.xlsx"
print(file_name.startswith('2021',0,4))

# 12. 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "itwill busan"
print(a.split())

# 13. 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나누고
# 문자열 슬라이싱을 활용하여 다음의 문장을 완성하세요. "오늘은 2024년 11월 06일 입니다."
date = "2024-11-06"
datePro = date.split("-")
print(datePro)

year = datePro[0]
month = datePro[1]
day = datePro[2]
print("오늘은 %s년 %s월 %s일 입니다." %(year, month, day))
print('오늘은 {0}년 {1}월 {2}일 입니다.'.format(year, month, day))
print(f'오늘은 {year}년 {month}월 {day}일 입니다.')

# 14. 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490      "
print(data.strip())