
# wrapper

def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

if __name__ == '__main__':
    mul3 = mul(3)
    mul5 = mul(5)

    print(mul3(10))
    print(mul(3)(10))
    print(mul5(10))

# 외부 함수 mul안에 내부 함수 wrapper를 만들고 wrapper를 리턴한다.

