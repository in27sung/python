import functools

# functools.reduct(function, iterable)은 함수(function)를 반복 간으한 객체(iterable)의
# 요소에 차례대로(왼쪽에서 오른쪽으로)누적 적용하여 이 객체를 하나의 값으로 줄이는 함수이다.

def add(data):
    result = 0
    for i in data:
        result += i
        return result

data = [1, 2, 3, 4, 5]
result = add(data)
print(result)

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result) # 15
# reduce()에 선언한 람다 함수를 data 요소에 차례대로 누적 적용하여
# ((((1 + 2) + 3) + 4) + 5)

# functools.reduce()로 최댓값 구하기

num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)
# [3, 2, 8, 1, 6, 7] 요소를 차례대로 reduce()의 람다 함수로 전달하여 두 값 중 큰 값을 선택하고 마지막에 남은
# 최댓값을 리턴한다.



