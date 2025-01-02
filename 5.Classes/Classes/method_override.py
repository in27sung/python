import constructor
# 메서드 오버라이딩(Method Override)
# 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것
# 오버라이딩 후에는 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출됨

# a = inheritance.FourCal(4, 0)
# a.div()
# Traceback (most recent call last):
#   File "/Users/Insung/PycharmProjects/pythonProject/5.Classes/Classes/method_override.py", line 7, in <module>
#     a.div()
#   File "/Users/Insung/PycharmProjects/pythonProject/5.Classes/Classes/inheritance.py", line 27, in div
#     result = self.first / self.second
#              ~~~~~~~~~~~^~~~~~~~~~~~~
# ZeroDivisionError: division by zero
# 메서드 오버라이딩으로 해결

class SafeFourCal(constructor.FourCal):
    def div(self):
        if self.second == 0: # 나누는 값이 0인 경우, 값을 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())

# 클래스 변수
# 객체 변수는 다른 객체들에 영향을 받지 않고 독립적으로 그 값을 유지함 (a.first, b.first)
# 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 서언하면 클래스 변수가 됨
# 해당 클래스를 바탕으로 인스턴스화된 객체들은 같은 값을 가진다.
class Family:
    lastname = "황"
#  클래스 변수 선언

print(Family.lastname)
# 클래스 변수는 클래스_이름.클래스 변수로 사용할 수 있음

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

a.lastname = "김"

print(a.lastname)
print(b.lastname)

print('-' * 80)
Family.lastname = "박"
print(a.lastname) # 박
print(b.lastname) # 박
# 같은 클래스 Family로 부터 만들어진 객체 a와 b의 lastname 값이 동시에 변경됨

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
# 3개의 값이 같다

print('-' * 80)

a.lastname = "김"

print(a.lastname);print(id(a.lastname))
print(b.lastname);print(id(b.lastname))
# a객체의 lastname의 값을 변경하면 id값이 변경

Family.lastname = "이"

print(a.lastname);print(id(a.lastname))
print(b.lastname);print(id(b.lastname))
print(Family.lastname);print(id(Family.lastname))
# 클래스변수의 값을 변경해도 이미 id값이 변경된 후 이므로 값이 같이 변경되지 않는다.



