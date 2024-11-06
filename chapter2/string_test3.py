# 1. 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 %formatting을 사용해서 출력
# [변수]
name1 = "홍길동"
age1 = 20
name2 = ("이순신")
age2 = 44

# [실행 예]
#  이름: 홍길동 나이: 20
# 문자열 포맷팅
print(("이름: %s 나이: %d") % (name1, age1))
print(("이름: %s 나이: %d") % (name2, age2))

# format함수
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

# f문자열 포매팅
print("이름: {0} 나이: {1}".format(name1, age1))
print("이름: {0} 나이: {1}".format(name2, age2))