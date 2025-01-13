# json
# json은 JSON 데이터를 쉽게 처리하고자 사용하는 모듈

import json

with open('myinfo.json') as f:
    data = json.load(f)

print(type(data))

print(data)


# JSON 파일을 읽을 때는 이 예처럼 json.load(파일_객체)를 사용한다. 이렇게 load() 함수는 읽은 데이터를
# 딕셔너리 자료형으로 리턴한다. 이와 반대로 딕셔너리 자료형을 JSON 파일로 생성할 때는 다음처럼
# json.dump(딕셔너리, 파일_객체)를 사용한다.

import json

data = {'name': '홍길동', 'birth': '0525', 'age': 30}
with open('myinfo.json', 'w') as f:
    json.dump(data, f)


d = {'name': '홍길동', 'birth': '0525', 'age': 30}
json_data = json.dumps(d)
print(json_data)




