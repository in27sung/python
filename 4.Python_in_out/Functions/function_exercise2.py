# 1. 함수의 호출 결과를 예측해보세요.
#
def 함수(문자열) :
  print(문자열)

함수("안녕")
함수("Hi")


# 2. 함수의 호출 결과를 예측해보세요.
def 함수(a,b):
  print(a+b)

함수(3,4)
함수(7,8)

# 3. 아래의 코드는 에러가 발생합니다. 원인을 설명해보세요.
# def 함수(문자열):
#   print(문자열)
#
# 함수()
# 인자값을 입렵하지 않아서 에러가 발생합니다.

# 4. 아래의 코드는 에러가 발생합니다. 원인을 설명해보세요.
# def 함수(a,b):
#   print(a+b)
#
# 함수("안녕",3)
# typeError가 발생합니다.

# 5. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여
#    출력하는 print_with_sime 함수를 정의하세요.
def print_with_smile(s):
    print(s, end=":D \n")



# 6. 5번에서 정의한 함수를 이용하여 "안녕하세요"를 출력하세요.
print_with_smile("안녕하세요")

print('-' * 80)
# 7. 현재 가격을 입력 받아 상한가(30%)를 출력하는 print_upper_price 함수를 정의하세요.
def print_upper_price(price):
    print(f'상한가는 {price + (price * 0.3)}')

print_upper_price(100)

# 8. 두 개의 숫자를 입력받아 두 수의 함을 출력하는 print_sum 함수를 정의하세요.
def print_sum(a, b):
    print(f'{a} + {b} = {a+b}')

print_sum(3,9)

# 9. 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는
#    print_arithmetic_operation 함수를 작성하세요.
# 예시) print_arithmetic_operation(3,4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75
def print_arithmetic_operation(a, b):
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {round(a / b, 2)}')

print_arithmetic_operation(3, 4)
# 10. 세 개의 숫자를 입력받아 가장 큰 수를 출력하는 print_max 함수를 정의하세요.
#     단 if문을 사용해서 수를 비교하는 과정이 들어갑니다.

def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    if b > a and b > c:
        print(b)
    else:
        print(c)

print_max(19, 199, 23)

