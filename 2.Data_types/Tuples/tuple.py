t1 = ()
t2 = (1,) #tuple은 뒤에 1하의 값만 넣을 때는 ',' 필수
print(type(t2))
t3 = (1, 2, 3)
t4 = 1, 2, 3
print(type(t4))
t5 = ('a', 'b', ('ab', 'cd'))

# 튜플 요소값을 삭제하려고 할 때
t1 = (1, 2, 'a', 'b')
# del t1[0] TypeError: 'tuple' object doesn't support item deletion
# t1[0] = 'c' TypeError: 'tuple' object does not support item assignment

# 인덱싱하기
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

# 슬라이싱하기
print(t1[1:])

# 튜플 더하기
t2 = (3, 4)
newt = t1 + t2
print(t1 + t2)
print(newt)

# 튜플 곱하기
t3 = t2 * 3
print(t3)

# 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
print(len(t1))

# (1, 2, 3)이라는 튜플에 값 4를 추가하여 (1, 2, 3, 4)라는 새로운 튜플을 출력해 보자
t1 = (1, 2, 3)
t1 += (4,)
print(f't1+(4,): {t1 + (4,)}')

print(t1)

