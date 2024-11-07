
# 튜플 자료형 연습문제

# 1. movie_list 이름의 비어있는 튜플을 만드세요
movie_list = ()

# 2. movie_list 튜플에 '싱크홀', '인질', '모가디슈'를 저장하세요
movie_list += ('싱크홀', '인질', '모가디슈')
print(movie_list)

# 3. 숫자 1이 저장된 my_tuple을 생성하세요
my_tuple = (1,)

# 4. 아래의 코드를 보고 오류가 발생하는 원인을 생각해보세요.
t = (1, 2, 3)
# t[0] = 'a'
# 튜블을 재 정의하지 않는 이상 저장되어 있는 값을 변경할 수 없습니다.

# 5. 아래와 같이 t를 정의하면 t는 무슨 타입인가?
t = 1, 2, 3, 4
print(type(t))
# tuple

# 6. 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t의 값이('A', 'b', 'c')가 되도록 수정하세요.
t = ('a', 'b', 'c')
t = (t[0].upper(),) + t[1:]
print(t)

# 7. 다음 튜플을 리스트로 변환하세요.(list() 를 사용하세요.)
a = ('itwill', 'busan', 'class4')
a = list(a)
print(a)

# 8. 아래의 리스트를 튜플로 변경하세요.(tuple() 사용)
a = tuple(a)
print(a)

# 9. 아래 코드의 실행 결과를 생각해보세요.(튜플 언팩킹)
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 10. 1 부터 99까지 정수 중 짝수만 저장된 튜플을 생성하세요.
even = tuple(range(2,99,2) )
print(even)

