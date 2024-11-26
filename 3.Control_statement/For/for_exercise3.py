
# 1. 리스트에는 네 개의 정수가 저장돼 있습니다.
# list = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하세요.

list1 = [3, -20, -3, 44]
for negative in list1:
    if negative < 0:
        print(negative)

# 2. for문을 사용해서 3의 배수만을 출력하세요.
# list = [3, 100, 23, 44]
# 실행 예: 3
print("#" * 80)
list2 = [3, 100, 24, 44]

result = [print(num) for num in list2 if num % 3 == 0]

# 3. 리스트에서 20 보다 작은 3의 배수를 출력하세요.
# list = [13, 21, 12, 14, 30, 18]
# 실행 예:
# 12
# 18
print("#" * 80)
list3 = [13, 21, 12, 14, 30, 18]

result = [print(num) for num in list3 if num % 3 == 0 and num < 20]

# 4. 리스트에서 세 글자 이상의 문자를 화면에 출력하세요.
# list = ["I", "study", "python", "language", "!"]
# 실행 예:
# study
# python
# language
print("#" * 80)
list4 = ["I", "study", "python", "language", "!"]
result = [print(word) for word in list4 if len(word) >= 3]

# 5. 리스트에서 대문자만 화면에 출력하세요.
# list = ["A", "b", "c", "D"]
# 실행 예:
# A
# D
print("#" * 80)
list5 = ["A", "b", "c", "D"]
result = [print(upper) for upper in list5 if upper.isupper()]

# (참고) isupper() 메서드는 대문자 여부를 판별합니다.
# 변수 = "A"
# 변수.isupper()
# => True
# 변수 = "a"
# 변수.isupper()
# => False

# 6. 리스트에서 소문자만 화면에 출력하세요.
# list = ["A", "b", "c", "D"]
# 실행 예:
# b
# c
print("#" * 80)
list6 = ["A", "b", "c", "D"]
result = [print(lower) for lower in list5 if lower.islower()]

# 7. 이름의 첫 글자를 대문자로 변경해서 출력하세요.
# list = ['dog', 'cat', 'parrot']
print("#" * 80)

list7 = ['dog', 'cat', 'parrot']

result = [print(capitalise.capitalize()) for capitalise in list7]


# 8. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하세요.
#    (힌트: split() 메서드 사용)
# list = ['hello.py', 'ex01.py', 'intro.hwp']
# 실행 예:
# hello
# ex01
# intro
print("#" * 80)

list8 = ['hello.py', 'ex01.py', 'intro.hwp']
result = [print(name.split('.')[0]) for name in list8]

# 9. 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하세요.
# list =  ['intra.h', 'intra.c', 'define.h', 'run.py']
# 실행 예:
# intra.h
# define.h
print("#" * 80)

list9 =  ['intra.h', 'intra.c', 'define.h', 'run.py']
result = [print(file) for file in list9 if file.split('.')[1] == 'h']

# 10. 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하세요.
# list =  ['intra.h', 'intra.c', 'define.h', 'run.py']
# 실행 예:
# intra.h
# intra.c
# define.h

print("#" * 80)

list10 =  ['intra.h', 'intra.c', 'define.h', 'run.py']
result = [file for file in list10 if file.split('.')[1] == 'h' or file.split('.')[1] == 'c']

print(*result)

print(print())