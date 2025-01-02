def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
print(positive([1, -3, 2, 0, -5, 6])) # [1, 2, 6]
# positive는 리스트를 입력으로 받아 각각의 요소를 판별해서 양수 값만 리턴하는 함수이다.

# filter
# filter란 '무엇인가를 걸러 낸다'라는 뜻으로, filter 함수도 이와 비슷한 기능을 한다.
# filter(함수, 반복_가능한_데이터)

# filter 함수는 첫 번째 인수로 함수, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를
# 받는다. 그리고 반복 간능한 데이터의 요소 순서대로 함수를 호출했을 때 리턴값이 참인
# 것만 묶어서(걸러 내서)리턴한다.

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
# filter(positive, [1, -3, 2, 0, -5, 6]은 [1, -3, 2, 0, -5, 6]의 각 요솟값을 순서대로 positive
# 함수에 적용하여 리턴값이 참인 것만 묶어서 리턴한다.
# 즉 1, 2, 6 요소만 x > 0 문장에 참이 되므로 [1, 2, 6]이 라는 결괏값이 출력된다.

# lambda 사용
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))
