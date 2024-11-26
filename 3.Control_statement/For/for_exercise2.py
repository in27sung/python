# 1. 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 출력하세요. 부가세는 가격의 10%가 책정됩니다.
from audioop import reverse

list1 = [100, 200, 300]

result = [num + (num / 10) for num in list1]

for value in result:
    print(f'부가세가 포함된 가격은 {round(value)}원 입니다')

# 2. for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하세요.
list2 = ["김밥", "라면", "튀김"]
# 오늘의 메뉴: 김밥
# 오늘의 메뉴: 라면
# 오늘의 메뉴: 튀김

result = [print(f'오늘의 메뉴: {menu}') for menu in list2]

# 3. list = ["아이티윌", "부산", "IT교육센터"]
# list에 저장된 문자열의 길이를 다음과 같이 출력하세요.
# 4
# 2
# 6
list3 = ["아이티윌", "부산", "IT교육센터"]
for i in list3:
    print(len(i))

# 4. 리스트에는 동물 이름이 문자열로 저장돼 있습니다.
# list = ['dog', 'cat', 'parrot']
# 동물 이름과 글자수를 다음과 같이 출력하세요.
# dog 3
# cat 3
# parrot 6

list4 = ['dog', 'cat', 'parrot']
for animal in list4:
    print(f'{animal} {len(animal)}')

# 5. 리스트에 동물 이름이 저장돼 있습니다.
# list = ['dog', 'cat', 'parrot']
# for문을 사용해서 동물 이름의 첫 글자만 출력하세요.
# d
# c
# p
list5 = ['dog', 'cat', 'parrot']

result = [print(f'동물 이름의 첫글자: {i[:1]}') for i in list5]


# 6. 리스트에는 세 개의 숫자가 바인딩돼 있습니다.
# list = [1, 2, 3]
# for문을 사용해서 다음과 같이 출력하세요.
# 3 x 1
# 3 x 2
# 3 x 3

list6 = [1, 2, 3]
for i in list6:
    print(f'3 x {i}')

# 7. 리스트에는 세 개의 숫자가 바인딩돼 있습니다.
# list = [1,2,3]
# for문을 사용해서 다음과 같이 출력하세요.
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

list7 = [1,2,3]
for i in list7:
    print(f'3 x {i} = {3 * i}')

# 8. 리스트에는 네 개의 문자열이 바인딩돼 있습니다.
# list = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하세요.
# 나
# 다
# 라
list8 = ["가", "나", "다", "라"]
count = 0
for hangul in list8:
    count = count + 1
    if count > 1:
        print(hangul)

for hangul in list[1:]:
    print(hangul)

print('=' * 80)
# 9. 리스트에는 네 개의 문자열이 바인딩돼 있습니다.
# list = ["가", "나", "다", "라"]
# for 문을 사용해서 다음고 같이 출력하세요.
# 가
# 다
list9 = ["가", "나", "다", "라"]

for hangul in list9[::2]:
    print(hangul)

# 10. 리스트에는 네 개의 문자열이 바인딩돼 있습니다.
# list = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하세요.
# 라
# 다
# 나
# 가

list10 = ["가", "나", "다", "라"]

for hangul in list10[::-1]:
    print(hangul)

# print(list10.sort(reverse=True))