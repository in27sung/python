
# Dictionary Syntax
# {key1:value1, key2:value2, key3:value3, ...}

dic = {'name':'pey', 'phone':'010123456678', 'birth':'1111'}

# 딕셔너리 생성 key로 정수값 1, value로 문자열ㅇ 'hi'를 사용
a = {1:'hi'}
print(a[1])

# value에 리스트를 넣을 수 있다.
a = {'a':[1, 2, 3]}
print(a['a'])

# 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제하기
del a[1]
print(a)

# 딕셔너리에서 Key를 사용해 Value 얻기
grade = {'pey': 10, 'juliet': 99}
print(grade['pey'])
print(grade['juliet'])

a = {1:'a', 2:'b'}
print(a[1])
print(a[2])

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# 딕셔너리 생성 시 주의 사항
a = {1:'a', 1:'b'}
print(a)
# -> 중복되는 key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨

# b = {[1, 2]: 'value'} TypeError: unhashable type: 'list'
# print(b)
# Key에 리스트를 쓸 수 없다.
# 딕셔너리의 Keyf로 쓸 수 있느냐 없느냐는 key가 변하는 값인지 변하지 않은지에 결정
b = {(1, 2): 'value'}
print(b)