print('=' * 80)
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a. setdata(4, 2)
print(a.add())
# -> add 메서드의 self 매개변수에 a가 자동으로 입력됨

# 곱하기, 빼기, 곱하기, 나누기 기능 추가
class FourCal:
    def setdata(self, first, second):
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

a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

# a = FourCal()
# a.add()
# 오류 발생! AttrirbuteError: 'FourCal' object has no attribute 'first'