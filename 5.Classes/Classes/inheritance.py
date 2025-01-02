import constructor
# 상속(Inheritance)
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것
# 자바에서는 class [서브클래스명] extends [슈퍼클래스명]로 상속을 표현하지만
# 파이썬에서는 class 서브클래스명(슈퍼클래스명) 으로 상속을 표현
# 상속은 기본 클래스는 그대로 나둔 채 클래스의 기능을 확장시킬 때 주로 사용

# class class_name(상속할_클래스_이름)
class MoreFourCal(constructor.FourCal):
    pass

a = MoreFourCal(4, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로
# FourCal 클래스의 모든 기능을 사용할 수 있다.

# 상속 기능은 왜 쓰는 걸까?
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할때 사용한다.
# '클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지? 라는 의문이 들 수 있다.
# 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.

class MoreFourCal(constructor.FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow())







