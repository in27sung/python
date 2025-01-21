
# 유니코드로 문자열 다루기
# 인코딩하기

a = 'Life is too short, You need Python'
b = a.encode('utf-8')
print(b)
print(type(b))

a = "한글"
b = a.encode('utf-8')
print(b)
print(b.decode('utf-8'))

b = a.encode('euc-kr')
print(b)

# 디코딩하기
b = a.encode('utf-8')
print(b)
print(b.decode('utf-8'))

b = a.encode('euc-kr')
print(b)
print(b.decode('euc-kr'))


