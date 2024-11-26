# Q1 - 조건문의 참과 거짓
# 다음 코드의 결괏값은 무엇일까?
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# Q2 - 3의 배수의 합 구하기
# while 문을 사용해서 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

# Q3 - 별 표시하기

i = 0
while True:
    i += 1
    if i > 5:break
    print('*' * i)

# Q4 - 1부터 100까지 출력하기
# for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

for i in range(1, 101):
    print(i)

print('#' * 80)
# Q5 -평균 점수 구하기
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

print('#' * 80)
# Q6 - 리스트 컴프리헨션 사용하기
# 다음 소스 코드는 리스트의 요수 중에서 홀수만 골라 2를 곱한 값을 Result 리스트에 담는 예제이다.

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
print(result)

result = [n * 2 for n in numbers if n % 2 == 1]
print(*result)

