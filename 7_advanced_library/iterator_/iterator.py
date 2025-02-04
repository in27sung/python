
# Iterator
# 이터레이터는 next 메서드를 호출할 때마다 차례대로 다음 요소를 반환하고, 더 이상 반환할 요소가 없을 때 StopIteration 예외를 발생시킨다.

a = [1, 2, 3, 4]
# next(a)
# Traceback (most recent call last):
#   File "/Users/Insung/PycharmProjects/python/7_advanced_library/iterator_/iterator.py", line 7, in <module>
#     next(a)
# TypeError: 'list' object is not an iterator

ia = iter(a)
print(type(ia)) # <class 'list_iterator'>

print(next(ia))
print(next(ia))
print(next(ia))
print(next(ia))
# print(next(ia))
# next 함수를 호출할 때마다 이터레이터 객체의 요소를 차례대로 리턴하는 것을 확인할 수 있다.
# 이터레이터 객체의 요소를 모두 리턴하고 나면 StopIteration 예외가 발생한다.

a = [1, 2, 3]

ia = iter(a)

# 이터레이터 객체를 for 문에 사용하면 요소를 차례대로 꺼내서 사용할 수 있다.
for i in ia:
    print(i)

# for 문을 이용하면 자동으로 값을 호출하므로 next 함수를 사용하지 않아도 되고 StopIteration 예외도 발생하지 않는다.
# 이터레이터 객체는 한 번 사용하면 다시 사용할 수 없다.
for i in ia:
    print(i)


print('-' * 50)
# 이터레이터 만들기
# 이터레이터는 __iter__ 메서드와 __next__ 메서드를 구현한 객체이다.
# __iter__ 메서드는 이터레이터 객체 자신을 반환하고, __next__ 메서드는 다음 요소를 반환한다.

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        result = self.data[self.index]
        self.index += 1
        return result

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    ia = MyIterator(a)

    for i in ia:
        print(i)
# 이터레이터는 값을 차례대로 꺼내서 사용할 수 있으므로 리스트와 같은 시퀀스 자료형보다 메모리를 효율적으로 사용할 수 있다.
# 이터레이터는 값을 차례대로 꺼낼 수 있으므로 데이터의 양이 많을 때 유용하다.
