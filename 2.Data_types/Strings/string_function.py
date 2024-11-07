
# 문자열 관련 함수들 p.72

a = "hobby"
# hobby에 포함된 b의 개수
print(a.count('b'))

# 위치(index) 알려 주기1 - find
a = "Python is the best choice"
print("b의 위치: %d" %a.find('b'))
print('t의 위치: {0}'.format(a.find('t')))
print(f'k의 위치: {a.find("k")}')

# 위치 알려 주기2 - index
a = "Life is too short"
print("t의 위치: %d" % a.index('t'))
# print(a.index('k')) ValueError: substring not found

# 문자열 삽입(join)
print(",".join('abcd'))
print(",".join(['a','b','c','d']))

# 소문자를 대문자로 바꾸기 - upper
a ="Hi my name is Insung"
print(a.upper())

# 대문자를 소문자로 바꾸기 - lower
a="Hi my name is Insung"
print(a.lower())

# 왼쪽 공백 지우기 - lstrip
a = "  hi  "
print(a.lstrip())

# 오른쪽 공백 지우기 - rstrip
print(a.rstrip())

# 양쪽 공백 지우기 - strip
print(a.strip())

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기 - split
print(a.split())
print(a.split()[0])
b = "a:b:c:d"
print(b.split(":"))
