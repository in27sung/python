# 파이썬의 생성자(Constructor)
# 객체가 생성될 때 자동으로 호출되는 메서드
# 자바에서는 [접근제한자] [클래스명]으로 만드는 반면, 파이썬에서는 이름이 정해져 있으며
# "__init__"을 사용한다.
# 메서드 이름을 __init__으로 설정하면 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출

# 생성자 존재하는 계산기 클래스
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

# a = FourCal()
# TypeError: FourCal.__init__() missing 2 required positional arguments: 'first' and 'second'
# 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문이다.

a = FourCal(4, 2)
b = FourCal(7, 3)
# -> self: 생성되는 객체(a), first: 4, second: 2
print(a.first)
print(b.first)
# __init__ 메서드가 자동 호출되면 setdata 메서드를 호출했을 때와
# 마찬가지로 first와 second 라는 객체가 생성됨

print(a.add())
print(a.div())


