# f문자열 포매팅(3.6 버전부터)
name = ("홍길동")
age = 30
str_format = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

# f문자열 표현식 지원
str_format = f'나는 내년이면 {age + 1}살이 된다'
print(str_format)

# 딕셔너리 f 문자열 포매팅 사용
d = {'name':'홍길동', 'age':30}
print(type(d))
str_format= f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}'
print(str_format)

# f문자열 정렬 - 왼쪽 정렬
str_format = f'{"hi":<10}'
print(str_format)

str_format = f'{"hi":<10}'
print(str_format)

# 오른쪽 정렬
str_format = f'{"hi":>10}'
print(str_format)

# 가운데정렬
str_format = f'{"hi":^10}'
print(str_format)

# 공백을 '='로 채움
str_format = f'{"hi":=^10}'
print(str_format)

# 공백을 '!'로 채움
str_format = f'{"hi":!^10}'
print(str_format)

y= 1.12345
str_format = f'{y:0.4f}'
print(str_format)

str_format = f'{y:10.4f}'
print(str_format)

str_format = f'{{and}}'
print(str_format)

str_format = f'{"python":!^12}'
print(str_format)