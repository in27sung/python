# 클로저란?
# 클로저는 함수 안에 내부 함수(inner function)를 구현하고 그 내부 함수를 리턴하는 함수이다.
# 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수를 뜻한다.
# 클로저는 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용한다.


def mul3(n):
    return n * 3

class Mul:
    def __init__(self, m):
        self.m = m

    def mul(self, n):
        return self.m * n

if __name__ == '__main__':
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3.mul(10))
    print(mul5.mul(10))


# 클래스를 이용해 특정 값을 미리 설정하고 그다음부터 mul() 메서드를 사용하면 원하는 형태로 호출할 수 있다.
# __call__ 메서드를 사용하면 객체를 함수처럼 호출할 수 있다.

class Mul:
    def __init__(self, m):
        self.m = m

    def __call__(self, n):
        return self.m * n

if __name__ == '__main__':
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10))
    print(mul5(10))

# 람다(lambda) 함수를 사용하면 더 간단하게 클로저를 만들 수 있다.

mul3 = lambda n: 3 * n
mul5 = lambda n: 5 * n

print(mul3(10))
print(mul5(10))
