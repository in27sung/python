import random
def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)
# 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 리턴한다.
# 선택된 값은 pop 메서드에 의해 사라짐

# random_pop2 함수는 random 모듈의 choice 함수를 사용해 좀더 직관적으로 만들 수 있다.
def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))
# random_pop 함수는 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음
# 그 값을 리턴한다. 물론 꺼낸 요소는 pop 메서드에 의해 사라진다.


# random.choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴한다.


# 리스트 항목을 무작위로 섞고 싶을 때는 random.sample 함수를 사용하면 됨
    data = [1, 2, 3, 4, 5]
    print(random.sample(data, len(data)))
# 두 번째 인수 len(data)는 무작위로 추출할 원소의 개수를 의미한다.
# 만약 random.smaple(data, 3)과 같이 사용한다면 data 리스트에서 무작위로
# 3개를 추출하여 리턴함
# if문에 의해 random_pop.py를 직접 실행하면 sample 함수가 동작하고
# standard_lib.py(다른 파일)에서 import를 통해 실행하면 동작하지 않는다.


def lotto():
    return sorted(random.sample(range(1, 46), 6))
lotto_numbers = lotto()
print(lotto_numbers)