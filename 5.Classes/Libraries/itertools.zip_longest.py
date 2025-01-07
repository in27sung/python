# itertools.zip_longest
# itertools.zip_longest(*iterable, fillvalue=None) 함수는 같은 개수의
# 자료형을 묶는 파이썬 내장 함수인 zip 함수와 똑같이 동작함
# 하지만 itertolls.zip_logest() 함수는 전달한 반복 가능 객체(*iterable)의 길이가
# 서로 다르다면 긴 객체의 길에 맞춰 fillvalue에 설정한 값을 짧은 객체에 채울 수 있다.

# 유치원 5명에게 간식을 나누어 주는 파이썬 코드를 작성
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

result = zip(students, snacks)
print(list(result))
# [('한민서', '사탕'), ('황지민', '초콜릿'), ('이영철', '젤리')]
# students와 snacks 요소 개수가 다르므로 더 작은 snacks의 개수만큼 zip()으로 묶게 된다.

# students의 요소 개수가 snacks 보다 많을 때 그 만큼을 '새우깡'으로 채우려면
# 요소 개수가 많은 것을 기준으로 자료형을 묶는 itertools.zip_longest()를 사용하면 된다.
# 부족한 항목은 None으로 채우는데 fillvalue로 값을 지정하면 None 대신 다른 값으로 채울 수 있다.

import itertools
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))

# itertolls.permutation
# itertools.permutation(iterable, r)은 반복 가능한 객체 중에서 r개를 선택한 순열을
# 이터레이터로 리턴하는 함수

result = list(itertools.permutations(['1', '2', '3'], 2))
print(result)
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

for a,b in itertools.permutations(['1', '2', '3'], 2):
    print(a + b)

# itertools.combination
# itertools.combination(iterable, r)은 반복 가능 객체 중에서
# r 개를 선택한 조합을 이터레이터로 리턴하는 함수
it = itertools.combinations(range(1, 7), 6)
# 1 ~ 45의 숫자 중에서 6개를 뽑는 경우의 수를 이터레이터로 리턴한다.
print(it)

for num in it:
    print(num)

print(len(list(itertools.combinations(range(1,46), 6))))
# 8145060
# 순환하여 출력하지 않고 이터레이터의 개수만 출력

# 중복 조합을 사용하는 함수
print(len(list(itertools.combinations_with_replacement(range(1, 46), 6 ))))# 15890700

