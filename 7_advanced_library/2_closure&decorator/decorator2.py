import time

# def elapsed(original_func):
#     def wrapper():
#         start = time.time()
#         result = original_func()
#         end = time.time()
#         print("time: %f초" % (end - start))
#         return result
#     return wrapper
#
#
# @elapsed
# def myfunc(msg):
#     print("'%s'을 출력합니다." % msg)
#
# myfunc("You need python")

# myfunc 함수는 입력 인수가 필요하지만, elapsed 함수 안의 wrapper 함수는 전달받은 myfunc 함수를 입력
# 인수 없이 호출해 오류가 발생하는 것이다. 그러므로 데코레이터 함수는 기존 함수의 입력 인수에 상관없이
# 동작하도록 만들어야 한다.


def elapsed(original_func):                         # 기존 함수를 인수로 받는다.
    def wrapper(*args, **kwargs):                   # *args, **kwargs로 입력 인수를 받는다.
        start = time.time()
        result = original_func(*args, **kwargs)     # 입력 인수를 그대로 전달한다.
        end = time.time()
        print("time: %f초" % (end - start))
        return result
    return wrapper


@elapsed
def myfunc(msg):
    print("'%s'을 출력합니다." % msg)

myfunc("You need python")

# *args와 **kwargs
# *args는 여러 개의 입력 인수를 튜플 형태로 받는다.
# **kwargs는 여러 개의 키워드 인수를 딕셔너리 형태로 받는다.

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, name='foo', age=3)

# 이처럼 func 함수에 *args, **kwargs를 사용하면 입력 인수를 자유롭게 받을 수 있다.