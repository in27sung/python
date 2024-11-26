
# 집합 자료형 - 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형

# 집합 자료형은 set 키워드로 생성하며 괄호안에 리스트를 입력할 수 있다.
s1 = set([1, 2, 3])
print(s1)
print(type(s1))

# 괄호 안에 문자열도 입력 가능
s2 = set("Hello")
print(s2)

# 집합 자료형의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다. (Unordered)

# 집합 자료형(set)을 리스트로 변환
s1 = set([1, 2, 3])
l1 = list(s1)
l2 = [1, 2, 3, 4, 5]
print(l1)
print(type(l1))

# 집합 자료형(Set)을 튜플로 변환
t1 = tuple(s1)
print(t1)
print(type(t1))

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1&s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s2.union(s1))

# 차집합
print(s1 - s2)
print(s2 - s1)

print(s1.difference(s2))
print(s2.difference(s1))

# 값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1 = {1, 2, 3}
print(type(s1))
s1.add(4)
print(s1)

# 값 여러 개 추가하기(update)
s1 = {1, 2, 3}
s1.update({4,5,6})
print(s1)

# 특정 값 제거하기
s1 = set({1, 2, 3})
s1.remove(2)
print(s1)
print(type(s1))
