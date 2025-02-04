
# 제너레이터란?
# 제너레이터는 이터레이터를 생성해주는 함수입니다.
# 이터레이터는 클래스에 __iter__와 __next__ 메서드를 구현해야 하지만, 제너레이터는 함수 안에서 yield라는 키워드만 사용하면 끝입니다.

def mygen():
    yield 'a'
    yield 'b'
    yield 'c'

g = mygen()
print(type(g))
print(next(g))

# 제너레이터 객체를 생성하면서 mygen 함수를 호출하면 mygen 함수가 실행되지 않고 제너레이터 객체만 생성됩니다.

# 제너레이터 표현식
def mygen():
    for i in range(1, 10001):
        result = i * i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))

# 튜플 표현식으로 좀더 간단하게 만들 수 있다.
gen = (i * i for i in range(1, 1000))
print(next(gen))

# 제너레이터 표현식은 리스트 표현식과 비슷하지만, 리스트 표현식은 [ ]로 둘러싸지만 제너레이터 표현식은 ( )로 둘러싼다는 점이 다릅니다.

class MyIterator:
    def __init__(self, data):
        self.data = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.data * self.data
        self.data += 1
        if self.data >= 1000:
            raise StopIteration
        return result
