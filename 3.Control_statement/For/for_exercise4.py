# 1. for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하세요.
from math import floor

for x in range(100):
    print(x)

print('#' * 80)
# 2. 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하세요.
# ※ 참고 - range의 세 번째 파라미터는 증감폭을 결정합니다.
# print(list(range(0,10,2)))
# [0,2,4,6,8]

print(*list(range(2002, 2051, 4)))

print('#' * 80)
# 3. 1부터 30까지의 숫자 중 3의 배수를 출력하세요.

for x in range(3, 31, 3):
    print(x)

print('#' * 80)
# 4. 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하세요.
for x in range(99, -1, -1):
    print(x)

print('#' * 80)
# 5. for문을 사용해서 아래와 같이 출력하세요.
# 0.0
# 0.1
# 0.2
# ...
# 0.9
for x in range(10):
    print(x / 10)
    print("{:.1f}".format(x * 0.1)) # ㅅㅗ수점 첫 번째 자리까지 표시
    print(floor(x)/10)

print('#' * 80)
# 6. 구구단 3단을 출력하세요.
for x in range(1, 10):
    print(f'3 x {x} = {3 * x}')

print('#' * 80)
# 7. 구구단 3단을 출력하되 홀 수 번째만 출력하세요.
for x in range(1, 10, 2):
    print(f'3 x {x} = {3 * x}')

print('#' * 80)
# 8. 1부터 10까지 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for문을 사용하여 작성하세요.
sum = 0
for x in range(1, 11):
    sum += x
print(sum)

print('-' * 80)
# 9. 1부터 10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for문을 사용하여 작성하세요.
sum = 0
for x in range(1, 11, 2):
    sum += x
print(sum)

print('#' * 80)
# 10. 1부터 10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for문을 사용하여 작성하세요.
sum = 1
for x in range(1, 11):
    sum *= x
print(sum)