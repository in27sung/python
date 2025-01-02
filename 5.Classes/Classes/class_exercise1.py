# 1. 클래스, 객체, 인스턴스에 대해 설명해보세요.
# 클래스: In Python, a class is a blueprint for creating objects (a particular data structure),
# defining the properties (attributes) and behaviors (methods) that the objects created from the class will have.
# It is used to define the structure and behavior of a collection of similar objects,
# allowing for object-oriented programming (OOP).


# 2. 아무런 기능을 가지고 있지 않은 사람(Human) 클래스를 정의 해보세요.
class Human:
    pass

# 3. 사람(Human) 클래스의 인스턴스를 생성하고 객체 a를 생성하세요.
a = Human()


# 4. 사람(Human) 클래스에 "사람입니다."를 출력하는 생성자를 추가해보세요.
class Human:
    def __init__(self):
        print("사람입니다!")

a = Human()

# 5. 사람(Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하고,
# 이름: 강진석, 나이: 30, 성별: 남자의 값을 가지는 객체 a를 생성하세요.
# 그리고 이름을 출력하세요.
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

a = Human("황인성", 30, "남자")
print(a.name)

# 6. 객체 a를 사용하여 나이를 출력하세요.
print(a.age)

# 7. 사람(Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def who(self):
        print(f'이름: {self.name} 나이:{self.age} 성별:{self.gender}')

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def inputInfo(self):
         self.name = input("이름을 입력하세요:")
         self.age = int(input("나이를 입력하세요: "))
         self.gender = input("성별을 입력하세요: ")

a = Human("황인성", 30, "남자")
a.who()
a.setInfo("홍길동", 23, "남자")
a.who()

# 8. 사람(Human) 클래스에 (이름, 나이, 성별)을 입력 받는 setInfo 메소드를 추가하고
# 기존의 객체 a에 정의되어 있던 값을 본인의 정보로 변경하고 출력하세요.

# 9. 객체 a에 대해 "del a" 명령어를 입력하면 객체는 사라진다. 이를 '소멸자'라고 한다.
# 객체를 삭제할 때 출력하는 소멸자를 추가하세요.
# (생성자 __init__, 소멸자 __del__ )

class NewHuman(Human):
    def __del__(self):
        print("객체 제거")

a = NewHuman("제거남", 23, "남자")
a.who()
del a
# del a 명령어에 의해서 a 객체는 메모리 상에서 사라짐
# 따라서, a.who() 를 호출하면 에러가 발생!
