
money = True
if money:
    print("택시")
else:
    print("걷기")

# 비교 연산자(<, >, ==, !=)
x = 3
y = 2
print(x > y)

print(x < y)

print(x == y)

print(x != y)

money = 2000

if money >= 3000:
    print("택시타기")
else:
    print("걸어가기")

# and, or, not
money = 2000
card = True
if money >= 3000 or card:
    print("택시타기")
else:
    print("걸어가기")

card = False
if not card:
    print("카드가 없음")
else:
    print("카드가 있음")

# =====================================================
# x in 리스트, x not in 리스트
# x in 튜플, x not in 튜플
# x in 문자열, x not in 문자열
# =====================================================

# 1이 [1, 2, 3]안에 있는가?
print(1 in [1, 2, 3])

# 1이 [1, 2, 3]안에 없는가?
print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'b'))

print('j' not in 'python')


pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시타기")
else:
    print("걸어가기")

# 1분코딩
# '주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고가기'라는 문장을 조건문으로 만들어 보자
if 'card' not in pocket:
    print("걸어가기")
else:
    print("버스타기")

# 주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내기
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내기")

print('=' * 80)

# else: if
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("돈으로 택시타기")
else:
    if card:
        print("카드로 택시타기")
    else:
        print("걸어가기")

# elif 사용
if 'money' in pocket:
    print("돈으로 택시타기")
elif card:
    print("카드로 택시타기")
else:
    print("걸어가기")


# if문을 한 줄로 작성하기
if 'money' in pocket: pass
else: print("카드 꺼내기")

# 조건부 표현식(conditional expression)
# 변수 = 조건문이_참인_경우 if 조건문 else 조건문이_거짓인_경우

score = 80

if score >= 60:
    message = "success"
else:
    message="failure"

print(message)

score = 30

message = "success" if score >= 60 else "failure"

print(message)

