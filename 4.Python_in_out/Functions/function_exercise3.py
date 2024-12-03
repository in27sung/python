# 1. 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하세요.
# 예시) print_reverse("python")
# nothyp

def print_reverse(text):
    reversed_text = ''.join(reversed(text))
    print(reversed_text)

print_reverse("python")

# 2. 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하세요.
# 예시) print_score([1,2,3])
# 2.0
def print_score(list):
    print(sum(list) / len(list))

print_score([1,2,3])

# 3. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하세요.
# 예시) print_even([1,3,2,10,12,11,15])
# 2
# 10
# 12
list = [1,3,2,10,12,11,15]

def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)

print_even(list)

# 4. 하나의 딕셔너리를 입력받아 딕셔너리의 key값을 화면에 출력하는 print_keys 함수를 정의하세요.
# 예시) print_keys ({"이름":"강진석", "나이":30, "성별":"남"})
# 이름
# 나이
# 성별

def print_keys(dict):
    for keys in dict.keys():
        print(keys)

print_keys ({"이름":"강진석", "나이":30, "성별":"남"})

# 5. my_dict 에는 날짜를 키로 하여 리스트 형태의 값이 저장되어 있다.
# my_dict = {"10/26" : [100,130,100,100] , "10/27" : [10,12,10,11]}
# my_dict와 날짜 키 값을 입력받아 리스트를 출력하는 print_value_by_key 함수를 정의하세요.

my_dict = {"10/26" : [100,130,100,100] , "10/27" : [10,12,10,11]}

def print_value_by_key(date):
    if date in my_dict:
        print(my_dict.get(date))

print_value_by_key("10/26")

def print_value_by_key(dict, key):
    print(dict[key])

my_dict = {"10/26" : [100,130,100,100] , "10/27" : [10,12,10,11]}
print_value_by_key(my_dict, "10/27")

# 6. 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하세요.
# 예시) print_5xn("안녕하세요반갑습니다")
# 안녕하세요
# 반갑습니다
print("-" * 80)
def print_5xn(text):
    print(text[:5])
    print(text[5:])

print_5xn("안녕하세요반갑습니다")

print("-" * 80)
def print_5xn2(text):
    i = 0
    for char in text:
        if i < 5:
            print(char, end="")
            i = i + 1
        if i == 5:
            print()
            i = 0
    print()

print_5xn2("안녕하세요반갑습니다하하")

print("-" * 80)
def print_5xn3(text):
    chunk_num = int(len(text) / 5) # 입력되는 문자열을 5로 나눠서 몇 줄이 필요한지 파악

    for x in range(chunk_num + 1):
        print(text[x * 5: x * 5 + 5])

print_5xn3("안녕하세요반갑습니다하하")

print("-" * 80)
# 7. 문자열과 한줄에 출력될 글자 수를 입력받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하세요.
# 예시) printmxn("안녕하세요반갑습니다." , 3)
# 안녕하
# 세요반
# 갑습니
# 다

def print_max(text, num):
    print(text[:num])
    print(text[num:num+num:])
    print(text[num+num:num+num+num:])
    print(text[num+num+num:num+num+num+num:])
print_max("안녕하세요반갑습니다", 3)

print("-" * 80)
def print_max2(text, num):
    chunk_num = int(len(text) / num) # 입력되는 문자열을 5로 나눠서 몇 줄이 필요한지 파악

    for x in range(chunk_num + 1):
        print(text[x * num: x * num + num])

print_max2("안녕하세요반갑습니다", 3)

# 8. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하세요. 회사는 연봉을 12개월로 나누어 분할 지급하고, 이때 1원 미만은 버립니다.
# 예시) calc_monthly_salary(12000000)
# 1000000
print("-" * 80)
def calc_monthly_salary(annual_salary):
    print(round(annual_salary/12))

calc_monthly_salary(12000000)


# 9. 아래 코드의 실행 결과를 예측해보세요.
def my_print(a,b):
  print("왼쪽:",a)
  print("오른쪽:",b)

my_print(a=100, b=200)


# 10. 아래 코드의 실행 결과를 예측해보세요.
def my_print(a,b):
  print("왼쪽:",a)
  print("오른쪽:",b)

my_print(b=100, a=200)