# 1. 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자일 경우,
# 소문자로 변경해서 출력하세요.
# (참고. islower()함수는 문자의 소문자 여부를 판별합니다.
# 소문자일 경우 True를 대문자일 경우 False를 반환합니다.)

import qrcode

qr = qrcode.make("http://naver.com")


str = input("알파벳을 입력해주세요: ")

if str.isalpha() and len(str) == 1:
    if str.islower():
        print(str.upper())
    elif str.isupper():
        print(str.lower())
else:
    print("알파벳 혹은 한글자가 아닙니다.")

# 2. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있습니다.
# 사용자로부터 score를 입력받아 학점을 출력하세요.
# 점수 	| 학점
# 81~100| A
# 61~80	| B
# 41~60	| C
# 21~40	| D
# 0~20	| E
# 실행 예: 83
# grade is A
score = int(input("점수를 입력하세요: "))

if 0 <= score <= 100 :
    if score > 80:
        print("A")
    elif score > 60:
        print("B")
    elif score > 40:
        print("C")
    elif score > 20:
         print("D")
    elif score > 0:
        print("E")
else:
    print("잘못된 입력 값 입니다.")

# 3. 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하세요.
# 각 통화별 환율은 다음과 같습니다.

# 통화명 	| 환율
# 달러	| 1167
# 엔	| 1096
# 유로	| 1268
# 위안	| 171
# 실행 예: 100달러
# 116700.00 원
# genspark.ai

exchange_dict = {"달러": 1167, "엔": 1096, "유료": 1268, "위안": 171}
exchange = input("환전할 통화명을 입력해주세요: ")

if exchange[:] in exchange_dict:
    amount = int(input("금액을 입력해주세요: "))
    print(amount * exchange_dict.get(exchange), end="원")
else:
    print("등록되지 않은 통화 입니다.")


# 4. 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하세요.
# input number1: 10
# input number2: 9
# input number3: 20
# 20
num_list = [1, 2, 3]
number_list = []
for i in num_list:
    number = int(input(f"숫자를 입력해주세요{i}: "))
    number_list.insert(i, number)

number_list.sort
print(number_list[2])




# 여기서 부터 복습하기
# 5. 전화번호 앞자리에 따라 지역이 아래와 같이 구분됩니다. 사용자로부터 휴대전화 번호를 입력 받고, 지역명을 출력하는 프로그램을 작성하세요.
# 번호	| 지역명
# 02	| 서울
# 051	| 부산
# 052	| 울산
# 064	| 제주
# 실행 예: 051-111-2222
# 부산 지역 번호 입니다.
tel = input("전화 번호를 입력하세요: ")
tel_list = tel.split('-')
print(tel_list)
tel_dict = {'02':'서울', '051': '부산', '052': '울산', '064': '제주'}

if tel_list[0] in tel_dict:
    print(f'{tel_dict[tel_list[0]]} 지역 번호 입니다.')
else:
    print("알 수 없는 지역명입니다.")


# 6. 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타냅니다. 예를 들어, 강북구의 경우 010, 011, 012 세 자리로 시작합니다.
# 강북구: 010, 011, 012
# 도봉구: 013, 014, 015
# 노원구: 016, 017, 018
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하세요.

postal_number = input("우편번호를 입력해주세요: ")
postal_num = postal_number[:3]
postal_len = len(postal_number)

postal_dict = {"강북구": ['010', '011', '012'], "도봉구": ['013', '014', '015'], "노원구": ['016', '017', '018']}

# if len(postal_number) == 5:
#     if postal_num in postal_dict



# 7. 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데 1,3은 남자 2,4는 여자를 의미합니다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하세요.

jumin = input("주민등록 번호를 입력해주세요: ")

if jumin in ['-'] and len(jumin.split('-')[0]) == 6 and len(jumin.split('-')[1]) == 7:
    identifier = jumin.split('-')[1][0]
    if identifier in ['1', '3']:
        print("남자입니다.")
    elif identifier in ['2', '4']:
        print("여자입니다.")
    else:
        print("주민등록번호 뒷자리는 1 ~ 4로 시작합니다.")
else:
    print("XXXXXX-XXXXXXX 형태로 입력해주세요.")



# 8. 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민등록번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하세요.
# 지역코드 |  출생지
# 00 ~ 08  |  서울
# 09 ~ 12  |  부산

id = input("주민등록번호를 입력하세요?")



#
# 9. 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용됩니다.
# 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더하고,
# 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 됩니다.
#
# 예를들어
# 821010-1635210 이라는 주민번호가 있다면
# 1차계산: 8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = 128
#            128 % 11 = 7(나머지)
# 2차계산: 11 - 7 = 4
# 따라서 마지막 자리가 4여야 유효한 주민등록번호가 됩니다.
# 즉, 위의 주민번호는 유효하지 않은 주민등록번호라는 얘기가 됩니다.
#
# 주민등록번호를 입력받아 입력한 주민등록번호가 유효한지를 확인하는 프로그램을 작성하세요.
#

id = input("주민등록번호를 입력하세요: ")
if len(id) == 14 and id[6] == '-':
    step1 = int(id[0]) * 2 + int(id[1]) * 4 + int(id[3]) * 5 + int(id[4]) * 6 + int(id[5]) * 7 + int(id[7]) * 8 + int(id)
    step2 = 11 - (step1 % 11)
    last_str = str(step2)
    if id[-1] == last_str:
        print("유효한 주민등록번호 입니다.")
    else:
        print("유효하지 않은 주민등록번호 입니다.")
else:
    print("XXXXXX-XXXXXX 형태로 입력하세요")