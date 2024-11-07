
# 리스트명 = [요소1, 요소2, 요소3, ...]
odd = [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['life', 'is']] # e[2][0]

# 리스트의 인덱스
a = [1, 2, 3]
print(a)

print(a[0])

print(a[0], a[2])

print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(f'a[0]: {a[0]}')
print(f'a[-1]: {a[-1]}')
print(f'a[3]: {a[3]}')
print(f'a[-1][0]: {a[-1][0]}')
print(f'a[-1][1]: {a[-1][1]}')
print(f'a[-1][2]: {a[-1][2]}')

# 리스트의 슬라이싱
myList = [1, 2, 3, 4, 5]
print(f'myList[0:2]: {myList[0:2]}')
a = "12345"
print(f'a[0:2]: {a[0:2]}')

print(f'myList[:2]: {myList[:2]}')

print(f'myList[2:]: {myList[2:]}')

# a = [1, 2, 3, 4, 5] 리스트에서 슬라이싱 기법을 사용하여 리스트 [2, 3]을 만들어 보자.
a = [1, 2, 3, 4, 5]
print(f'a[1:3]: {a[1:3]}')

# 리스트 연산하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(f'a+b: {a+b}')

# 리스트 반복하기(*)
print(f'a * 3 {a * 3}')

# 리스트 길이 구하기
print(len(a))

# 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

# del 함수를 사용해 리스트 요소 삭제하기
# del 객체(객체: 파이썬에서 사용되는 모든 자료형을 말한다)
del a[1]
print(a)
print(a[1])

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

# 리스트 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5,6])
print(a)

# 리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

# 리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 위치 반환(index)
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
# print(a.index(0)) ValueError: 0 is not in list

# 리스트 요소 삽입(insert) insert(a, b)
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3,5)
print(a)

# 리스트 요소 제거(remove) - 첫 번째 요소 삭제
a = [1, 2, 3, 1, 2, 3]
print(a)
print(f'a.index(3): {a.index(3)}')
print(f'a.remove(value): {a.remove(3)}')
print(a)
print(f'a.index(3): {a.index(3)}')
a.remove(3)
print(a)

# 리스트 요소 꺼내기(pop) - 마지막 요소를 돌려주고 요소 삭제
a = [1, 2, 3]
print(a.pop())
print(a)

# 리스트의 x번째 요소를 돌려주고 그 요소는 삭제
a = [1, 2, 3]
print(f'a.pop(index): {a.pop(1)}')
print(a)

# 리스트에 포함된 요소 xdml 개수 세기(count)
a = [1, 2, 3, 1]
print(a.count(1))

# 리스트 확장 - extend
a = [1, 2, 3]
print(f'a.extend(list): ')
a.extend([4,5])
print(a)

b = [6, 7, [1, 2, 3]]
# a += b
a.extend(b)
print(a)