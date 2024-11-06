from pstats import Stats
from unittest.util import three_way_cmp

print("Hello world")

print('Python is fun')

print("""Life is too short, you need python""")

print('''Life is too short, you need python''')
print("-" * 50)
food = "Python's favorite food is perl"

print(food)

say = '"Python is very easy." he said.'

print(say)
print("-" * 50)
food = 'Python\'s favorite food is perl'

print(food)

say = "\"Python is very easy.\" he said."

print(say)
print("-" * 50)
multiline = "Life is too short\nYou need python"

print(multiline)
print("-" * 50)
multiline = '''
life is too short
you need python
'''

multiline = """
life is too short
you need python
"""

print(multiline)

print("-" * 50)
# 문자열 더해서 연산하기(Concatenation)
head = "Python"
tail = " is fun!"
concat = head + tail
print(concat)

# 문자열 곱하기
a = "Python"
multiplyString = a * 2
print(multiplyString)

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short"
print(len(a))

print("-" * 50)
#String indexing


a = "Life is too short, You need Python"
print("a[3] =", a[3])
print("a[0] =",a[0])
print("a[12] =",a[12])
print("a[-1] =",a[-1])


print("-" * 50)
#String slicing
b = a[0] + a[1] + a[2] + a[3]
print(b)

b = a[0:4]
print(b)
b = a[5:7]
print(b)

b = a[12:17]
print(b)

b = a[19:]
print(b)

b = a[:17]
print(b)

b = a[:]
print(b)

b = a[19:7]
print(b)

# 슬라이싱으로 문자열 나누기
a = "20241031Rainy"
date = a[0:8]
print(date)
weather = a[8:]
print(weather)
year = a[:4]
print(year)

day = a[4:8]
print(day)


a = "Pithon"
print(a[1])
# TypeError: 'str' object does not support item assignment
# a[1] = 'y'

print(a[:1] + 'y' + a[2:])

# 문자열 포매팅
test = "I eat %d apples." % 3
print(test)


test = "I eat %s apples." % "five"
print(test)

number = 3
test = "I eat %d apples." % number
print(test)

# 문자열 포매팅 - 2개 이상의 값 넣기
number = 10
day = "three"
test = "I ate %d apples. So I was sick for %s days." % (number, day)
print(test)

# 문자열 포맷 코드
# %s - 문자열(string)
# %c - 문자(character)
# %d - 정수(integer)
# %f - 부동 소수(floating-point)
# %o - 8진수
# %x - 16진수
# %% - Liter %(문자 '%' 자체)

# %s 포맷 코드에는 어떤 형태의 값이든 변환해 넣을 수 있음
test = "I have %s apples." % 3
print(test)

test = "rate is %s" % 3.234
print(test)


# format 함수를 사용한 포매팅 - 숫자 바로 대입
test = "I eat {0} apples.".format(3)
print(test)

# format 함수를 사용한 포매팅 - 문자열 바로 대입
test = "I eat {0} apples.".format("five")
print(test)

# format 함수를 사용한 포매팅 - 숫자값을 가진 변수로 대입
number = 3
str_format = "I eat {0} apples.".format(number)
print(str_format)

# format 함수를 사용한 포매팅 - 2개 이상의 값 넣기
number = 10
day = "three"
str_format = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(str_format)

# format 함수를 사용한 포매팅 - 이름으로 넣기
str_format = "I ate {number} apples. so I was sick for {day} days.".format(number = 5, day = 3)
print(str_format)

# format 함수를 사용한 포매팅 - 인덱스와 혼용해서 넣기
str_format = "I ate {0} apples. I was sick for {day} days".format(10, day = "three")
print(str_format)

# 왼쪽 정렬
str_format = "{0:<10}".format("hi")
print(str_format)
print(str_format, end="hi\n")

# 오른쪽 정렬
str_format = "{0:>10}".format("hi")
print(str_format)
print(str_format, end="hi\n")

# 가운데 정렬
str_format = "{0:^10}".format("hi")
print(str_format, end="hi\n")

# 공백 채우기
str_format = "{0:!^10}".format("hi")
print(str_format)

# 소수점 표현하기
y = 13.42134234
print("{0:.4f}".format(y))
y = 12.12345678
# 소수점 표현하기 - 자릿수 10으로 설정
print("{0:10.4f}".format(y))

# {또는} 문자 표현하기
str_format = "{{and}}".format()
print(str_format)

