
# Variables are containers for storing data values.

# 변수 생성
a = 1
b = 'python'
c = [1, 2, 3]

a = [1, 2, 3]

# 객체의 주소 값
print(id(a))

# 리스트를 복사할 때
b = a
print(id(b))

# a 와 b가 가리키는 객체가 같은가? True
print(a is b)

# a 와 b 는 같은 주소를 참조하므로 같은 결과가 출력
a[1] = 4
print(a)
print(b)

# 다른 주소를 참조하게 하는 방법
# 방법1 - [:] 이용하기
a = [1, 2, 3]
b = a[:] # 리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
a[1] = 4
print(id(a))
print(id(b))

print(a)
print(b)

# 방법2 - copy 모듈 이용하기

# copy 모듈에 있는 copy 함수 import
from copy import copy
a = [1, 2, 3]
b = copy(a)
b = a.copy()

# False
print(b is a)

# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
(a,b) = 'python', 'life'

#  리스트로 변수를 만들수 있음
[a, b] = ['python', 'life']


# 여래 개의 변수에 같은 값을 대입 가능
a = b = 'python'

print(a)

# 두 변수의 값 바꾸기
a = 3
b = 5
a, b = b, a
print(a)
print(b)

# 1분 코딩
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
# a와 b는 서로 다른 메모리를 가리킴 