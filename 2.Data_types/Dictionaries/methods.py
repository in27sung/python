
# Key 리스트 만들기 - keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
print(type(a.keys()))

# dict_key 객체를 리스트로 변환
l = list(a.keys())
print(type(l))
print(l)

# Value 리스트 만들기 - values
print(a.values())
print(type(a.values()))

# Key, Values 쌍 얻기 - items
print(a.items())
# items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴한다.

# Key:Value 쌍 모두 지우기 - clear
a.clear()
print(a)

# Key로 Value 얻기 - get
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))
# print(a['nokey']) # KeyError: 'nokey'
print(a.get('nokey'))

# get(x,'default')
print(a.get('nokey', 'foo'))

# 해당 Key가 딕셔너리 안에 있는지 조사하기 - in
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print('name' in a)

print('email' in a)














