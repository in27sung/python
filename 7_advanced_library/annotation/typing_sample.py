
def add(a: int, b: int) -> int:
    return a + b

result = add(1, 2.14)
print(result)

# 타입 어노테이션은 변수의 타입을 지정하는 것으로 변수의 타입을 변경하지는 않습니다.
# 타입 어노테이션은 코드를 읽는 사람이 함수의 인자와 리턴값의 타입을 알 수 있게 도와줍니다.
# 타입 어노테이션은 코드를 실행할 때 타입을 검사하지 않습니다.

def add(a: int, b: int) -> int:
    return a + b

result = add(1, 2.14)
print(result)
