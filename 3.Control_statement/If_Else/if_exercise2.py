# if문 연습문제2

# 1. 사용자로부터 입력받은 문자열을 두 번 출력하세요. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과입니다.
# ( input() 함수를 통해서 문자열을 입력 받을 수 있습니다.)
# 실행 예: 안녕하세요안녕하세요
str = input("입력해주세요: ")

if str == "안녕하세요":
    print("안녕하세요안녕하세요")

# 2. 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하세요.
num = input("숫자를 입력하세요: ")
if num.isdigit():
    print(int(num) + 10)
else:
    print("숫자를 입력해주세요.")


# 3. 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하세요.
# num = input("숫자를 입력하세요: ")
if int(num) % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 4. 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하세요. 단, 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 합니다.
# num = input("숫자를 입력하세요: ")
if int(num) < 255:
    print(int(num) + 20)
else:
    print("255")

# 5. 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하세요. 단, 출력 값의 범위는 0~255입니다.
# 예를 들어 결괏값이 0보다 작은 값이 되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 합니다.
# num = input("숫자를 입력하세요: ")
if 0 < int(num) < 255:
    print(int(num) - 20)
elif int(num) < 0:
    print("0")
elif int(num) > 255:
    print("255")

# 6. 사용자로부터 입력 받은 시간이 정각인지 판별하세요.
# 실행 예:
# 현재시간: 02:00
# 정각입니다.
# 현재시간: 02:10
# 정각이 아닙니다.
clock = input("시간을 입력하세요(예: 00:00): ")
print(clock[3:])
if clock[3:] == '00':
    print(f'현재시간: {clock}')
    print("정각입니다")
else:
    print(f'현재시간: {clock}')
    print("정각이 아닙니다")

# 7. 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하세요. 포함되었다면 "정답입니다."를 아닐 경우 "오답입니다."를 출력하세요.
fruit_list = ["사과", "포도", "홍시"]
fruit = input("과일을 입력하세요: ")
if fruit in fruit_list:
    print("정답입니다.")
else:
    print("오답입니다.")

# 8. 아래와 같이 fruit 딕셔너리가 정의되어 있습니다. 사용자가 입력한 값이 딕셔너리 키(key) 값에 포함되었다면 해당 value 값을 출력하고,
# 키 값이 없다면 "올바른 키 값을 입력하세요."를 출력하세요.
fruit_dict = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = input("계절을 입력하세요: ")
if season in fruit_dict:
    print(fruit_dict.get(season))
else:
    print("올바른 키 값을 입력하세요.")

# 9. 아래와 같이 fruit 딕셔너리가 정의되어 있습니다. 사용자가 입력한 값이 딕셔너리 value 값에 포함되었다면 해당 (key)값을 출력하고,
# value 값이 없다면 "올바른 키 값을 입력하세요."를 출력하세요.

fruit_dict = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
fruit = input("과일을 입력하세요: ")
fruit_value = list(fruit_dict.values())
fruit_key = list(fruit_dict.keys())

if fruit in fruit_value:
    print(fruit_key[fruit_value.index(fruit)])
else:
    print("올바른 키 값을 입력하세요.")

# 딕셔너리 내용을 튜플로 묶은 후 위치 변경
# switch_fruit = {v:k for k,v in fruit.items()}
# print(switch_fruit)