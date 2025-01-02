# 1. 초기값으로 종류, 바퀴수를 가지는 "transportation(교통수단)" 클래스를 정의하세요.
class transportation:
    def __init__(self, type, wheel):
        self.type = type
        self.wheel = wheel

# 2. transportation 클래스를 상속받은 bicycle 클래스를 정의하세요.
class bicycle(transportation):
    pass

print('-' * 80)
# 3. 다음 코드가 동작하도록 bicycle 클래스를 정의하세요.
#    이때 bicycle 클래스는 transportation 클래스를 상속받습니다.
#    print(bicycle1.type) # 이륜 자전거
#    print(bicycle1.wheel) # 2

bicycle1 = bicycle("이륜자전거", 2)
print(bicycle1.type)
print(bicycle1.wheel)

print('-' * 80)
# 4. 다음 코드가 동작하도록 bicycle 클래스를 정의하세요.
#    이때 bicycle 클래스는 transportation 클래스를 상속받습니다.
#    bicycle2 = bicycle("이륜자전거", 2, 1000)
#    print(bicycle.value)

class bicycle(transportation):
    def __init__(self, type, wheel, value):
        super().__init__(type, wheel)
        # self.type = type
        # self.wheel = wheel
        self.value = value

bicycle2 = bicycle("이륜자전거", 2, 1000)

print(bicycle2.value)

# super(): 자식 클래스에서 부모 클래스의 내용을 사용하고 싶을 경우에 사용.
class father():
  def handsome(self):
      print("잘생겼다.")

# -> 아무런 내용이 출력되지 않는다.

# 위의 코드를 아래와 같이 수정해보자.
class child(father):
  def handsome(self):
      '''물려받았어요'''
      super().handsome()

child = child()
child.handsome()

# 5. 다음 코드가 동작하도록 car 클래스를 정의하세요.
#    이때 car 클래스는 transportation 클래스를 상속받습니다.
#    morning = car("소형차", 4)
#    morning.info()
#    타입: 소형차
#    바퀴 수: 4

class car(transportation):
    def __init__(self, type, wheel):
        super().__init__(type, wheel)

    def info(self):
        print(f'타입: {self.type}')
        print(f'바퀴 수: {self.wheel}')


morning = car("소형차", 4)
morning.info()

# 6. bicycle 클래스의 info() 메서드로 value 정보까지 출력하도록 수정해보세요.
# 이 때, 상속받은 transportation의 info() 메서드를 오버라이딩 합니다.
# bicycle1 = cicycle("이륜 자전거", 2, 1000)
# bicycle.info()
# 타입: 이륜 자전거
# 바퀴 수: 2
# 가격: 1000

class bicycle(transportation):
    def __init__(self, type, wheel, value):
        super().__init__(type, wheel)
        self.value = value

    def info(self):
        # print("타입: ", self.type)
        # print("바퀴 수: ", self.wheel)
        super().info()
        print("가격: ", self.value)

bicycle1 = bicycle("이륜자전거", 2, 1000)
bicycle1.info()

print('-' * 80)
# 7. 다음 코드의 실행 결과를 예상해보세요.

class parents:
    def call(self):
        print("부모호출")

class child(parents):
    def call(self):
        print("자식호출")

me = child()
me.call()
# 메서드를 오버라이딩하면 자식 클래스에서 오버라이딩한 내용이 출력

# 8. 다음 코드의 실행결과를 예상해보세요.

class parents:
    def __init__(self):
        print("부모 초기화")

    class child(parents):
        def __init__(self):
            print("자식 초기화")
            super().__init__()

    me = child()