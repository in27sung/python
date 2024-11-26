from operator import concat

# Q1 평균 점수 구하기
korean = 80
english = 75
maths = 55
total_score = korean + english + maths
print(total_score / 3)

# Q2 홀수, 짝수 판별하기

number = 13
if number % 2 == 0:
    print('짝수')
elif number % 2 == 1:
    print('홀수')

# Q3 주민등록번호 나누기
pin = "881120-1068234"
yyymmdd = pin[:6]
num = pin[:6] + pin[7:]
print(yyymmdd)
print(num)

# Q4 주민등록번호 인덱싱
print(pin[7])

# Q5 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

# Q6 리스트 역순 정렬하기
a = [1, 3, 5, 4 , 2]
a.sort()
print(a)
a.reverse()
print(a)

# Q7 리스트를 문자열로 만들기
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# Q8 튜플 더하기
a = (1, 2, 3)
a = a + (4,)
print(a)

# Q9 딕셔너리의 키
a = dict()
# 오류 발생
# a[[1]] = 'python' # key와 value 값으로 이루어진 dictionary는 key로 변하는(mutable) 값을 사용할 수 없다.
# [1]은 list형으로 값이 변할 수 있는 자료형이다

a[('a',)] = 'python'
print(a)


# Q10 딕셔너리 값 추출하기
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# Q11 리스트에서 중복 제거하기
a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# Q12 파이썬 변수
a = b = [1, 2, 3]
a[1] = 4
print(b)

# a의 두 번째 요솟값을 변경하면 b값도 같이 변경된다. 왜냐하면, 두 변수가 동일한 주소값을 가지기 때문