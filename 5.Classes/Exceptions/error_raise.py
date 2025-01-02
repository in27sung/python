# 오류 일부러 발생시키기
# 파이썬은 raise 명령어를 사용하여 오류를 강제로 발생시킬 수 있다.
from PIL.IcnsImagePlugin import enable_jpeg2k


class Bird:
    def fly(self):
        raise NotImplementedError

# NotImplementedError는 파이썬 내장 오류로
# 꼭 작성해야 하는 부분이 구형되지 않앗을 경우 일부러 오류를 발생

class Eagle(Bird):
    pass


eagle = Eagle()
eagle.fly()
# eagle 객체는 Eagle 클래스의 인스턴스이고, Eagle 클래스는 Bird 클래스를 상속받음.
# eagle.fly() 메서드 호출 시 Eagle에는 정의되어 있지 않으므로 슈퍼클래스인 Bird에서
# 정의 된 fly메서드를 호출하게 된다.
# Bird 클래스의 fly() 메서드는 오류를 발생시키는 raise 설정이 되어 있어 결국 오류가 발생
# - 이를 해결하려면 Eagle 클래스에서 fly 메서드를 오버라이딩 해야 한다.

class Eagle(Bird):
    def fly(selfse):
        print("Very fase")

eagle = Eagle()
eagle.fly()
# 메서드 오버라이딩을 하여 fly() 메서드 호출 시 자신의 오버라이딩 된 fly() 메서드가 호출됨

