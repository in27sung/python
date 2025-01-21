
# 데코레이터란?
# 데코레이터는 함수를 입력으로 받아 함수를 반환하는 함수이다.

import time

from sympy import resultant


def myfunc():
    stat = time.time()
    print("start")
    end = time.time()
    print("time:", end - stat)

myfunc()

import time

def elapsed(original_func):
    def wrapper():
        stat = time.time()
        end = time.time()
        print("time: %f초" % (end - stat))
        return original_func()
    return wrapper
def myfunc():
    print("함수가 실행됩니다.")

decorated_myfunc = elapsed(myfunc)
decorated_myfunc()

# elapsed() 함수와 같은 클로저를 데코레이터라고 한다.

import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func()
        end = time.time()
        print("time: %f초" % (end - start))
        return result
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

myfunc()


@elapsed
def myfunc(msg):
    print("'%s'을 출력합니다." % msg)

myfunc("You need python")

# myfunc 함수는 입력 인수가 필요하지만, elapsed 함수 안의 wrapper 함수는 전달받은 myfunc 함수를 입력
# 인수 없이 호출해 오류가 발생하는 것이다. 그러므로 데코레이터 함수는 기존 함수의 입력 인수에 상관없이
# 동작하도록 만들어야 한다.
