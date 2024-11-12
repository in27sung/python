# 딕셔너리 연습문제

# 1. 별 표현식
# - 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 한다.
# - star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있다.

# a,b,c = (0,1,2,3,4,5)의 결과를 확인하세요.

a,b,*c = (0,1,2,3,4,5)
print(a)
print(b)
print(c)
print(type(c))

# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score
# 변수에 넣어 출력해보세요.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, rest_score1, rest_score2 = scores
print(valid_score)

# 2. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 넣어 출력해보세요.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
rest_score1, rest_score2, *valid_score = scores
print(valid_score)

# 3. 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 8개의 값을 valid_score 변수에 넣어 출력해보세요.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
rest_score1, *valid_score, rest_score2 = scores
print(valid_score)

# 4. temp 이름의 비어있는 딕셔너리를 만들어보세요.
temp = {}

# 5. 다음의 아이스크림 이름과 가격을 딕셔너리로 구성하세요.
#    메로나(1000), 폴라포(1200), 붕어싸만코(1800)
iceCreams = {'메로나': 1000, '폴라포': 1200, '붕어싸만코': 1800}
print(iceCreams)

# 6. 아이스크림 딕셔너리에 아래의 아이스크림 정보를 추가하세요.
#     죠스바 1200원, 월드콘 1500원
iceCreams['죠스바'] = 1200
iceCreams['월드콘'] = 1500
print(iceCreams)

# 7. 아이스크림 딕셔너리를 활용하여 아래와 같은 실행 결과를 표시하세요.
#    실행 예: "메로나의 가격은 1000원 입니다."
print(f'메로나의 가격은 {iceCreams.get("메로나")}원 입니다')
print('메로나의 가격은', iceCreams.get("메로나"), end='원 입니다\n')
print('메로나의 가격은 {0}원 입니다'.format(iceCreams['메로나']))
# 8. 아이스크림 딕셔너리에서 메로나의 가격을 1300으로 수정하세요.
iceCreams['메로나'] = 1300
print(f'메로나의 가격은 {iceCreams.get("메로나")}원 입니다')

# 9. 아이스크림 딕셔너리에서 메로나를 삭제하세요.
del iceCreams['메로나']

# 10. 딕셔너리에 없는 키를 사용해서 인덱싱을 하면 어떻게 될지 확인해보세요.
# iceCreams['메로나'] #KeyError: '메로나'

# 11. 아래의 아이스크림 관련 딕셔너리를 생성하세요. (아이스크림 이름을 키값으로 생성하세요.)
#     이름: 메로나, 비비빅, 죠스바
#     가격: 300, 400, 250
#      재고: 20, 3, 100
iceCreams = {'메로나':{'가격': 300,'재고': 20}, '비비빅': {'가격': 400,'재고': 3}, '죠스바': {'가격': 250,'재고': 100}}
print(iceCreams)

# 12. ice_cream 딕셔너리에서 메로나의 가격을 출력하세요.
print(iceCreams.get('메로나').get('가격'))

# 13. ice_cream 딕셔너리에서 비비빅의 남은 수량을 출력하세요.
print(iceCreams.get('비비빅').get('재고'))

# 14. 딕셔너리에 월드콘,500원,7개의 재고 내용을 추가하세요.
iceCreams['월드콘'] = {'가격': 500, '재고': 7}
print(iceCreams['월드콘'])

# 15. ice_cream 딕셔너리에서 key 값으로만 구성된 리스트를 생성하세요.
print(list(iceCreams.keys()))

# 16. ice_cream 딕셔너리에서 values 값으로만 구성된 리스트를 생성하세요.
ice_cream = list(iceCreams.values())
print(ice_cream)

# 17. ice_cream 딕셔너리에서 아이스크림을 하나씩 판매하면 총 얼마가 되는지 출력하세요.
#      ※ sum() 함수를 사용하세요.
ice_cream_price = [ice_cream[0]['가격'], ice_cream[1]['가격'], ice_cream[2]['가격'], ice_cream[3]['가격']]
print(sum(ice_cream_price))


# 18. new_product 딕셔너리를 ice_cream 딕셔너리에 추가하세요.
new_product = {'팥빙수':3000, '아이스티':2000}
#     ※ 힌트: .update() 를 사용하자.
iceCreams.update(new_product)
print(iceCreams)

# 19. 두 개의 튜플을 하나의 딕셔너리로 변환해보자. keys를 키로, vals를 값으로 정하고 딕셔너리 이름은
#     result 라고 정한다.
#     참고: zip(키,값) 함수를 통해 하나로 묶을 수 있으며 이를 dict()로 딕셔너리 변환할 수 있다.
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 20. 두 개의 리스트 close_table 이름의 딕셔너리로 생성하세요.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)




