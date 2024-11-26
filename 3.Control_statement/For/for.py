
# for 변수 In list(또는 튜플, 문자열):
#   수행할 문장1
#   수행할 문장2
#   ...

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

print('=' * 80)

# marks1.py
marks = [90, 25, 67, 45, 80] # 학생의 시험 점수 리스트
number = 0 # 학생에게 붙여 줄 번호
for mark in marks: # 90 25 67 45 80
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

# marks2.py
marks = [90, 25, 67, 45, 80] # 학생의 시험 점수 리스트
number = 0 # 학생에게 붙여 줄 번호
for mark in marks: # 90 25 67 45 80 을 순서대로 mark에 대입
    number = number + 1
    if mark >= 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)

print('=' * 80)

a = range(10)
print(a)
# -> range(0, 10)
# -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

a = range(1, 11)
print(a)
# -> range(1, 11)
# -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

add = 0
for i in range(1, 11):
    add = add + i
print(add)

print('=' * 80)

# marks3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %(number + 1))

# for 문과 range 함수를 사용하여 1부터 100까지 더해 보자.

total = 0
for number in range(1, 101):
    total = total + number
print(total)

print('=' * 80)

for i in range(2, 10): # 2 ~ 9
    for j in range(1, 10): # 1 ~ 9
        print(i * j, end = " ")

    print()

print('=' * 80)
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)

# 위의 코드를 리스트 comprehension(리스트 내포)을 적용
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# [1, 2, 3, 4] 중에서 짝수만 3을 곱하여 담고 싶다면
# list comprehension 안에 If 조건을 사용할 수 있음
# [표현식 for 항목 in 반복 가능 객체 if 조건]
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# [표현식 for 항목1 in 반복 가능한 객체1 if 조건1
#       for 항목2 in 반복 가능한 객체2 if 조건2
#       ...
#       for 항목n in 반복 가능한 객체3 if 조건n

result = [x * y for x in range(2, 10)
                for y in range(1, 10)]




