# 1. 개인정보를 저장하는 private_info 클래스를 정의해 보세요.
# 클래스는 속성과 매서드를 갖고 있지 않습니다.
class private_info:
    pass

# 2. private_info 클래스의 객체가 생성될 때
#    이름과 전화번호를 받을 수 있도록 생성자를 정의해보세요.
class private_info:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

# 3. 객체에 이름을 입력할 수 있는 set_name 메서드를 추가해 보세요.
class private_info:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def set_name(self, name):
        self.name = name

# 4. 객체에 전화번호를 입력할 수 있는 set_tel 메서드를 추가해보세요.
class private_info:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def set_name(self, name):
        self.name = name

    def set_tel(self, tel):
        self.tel = tel
# 5. 이름과 전화번호를 리턴하는 get_name, get_tel 메서드를 추가하세요.
#    해당 메서드를 사용하여 이름과 전화번호를 얻고 이를 출력해보세요.
class private_info:
    def __init__(self, name, tel):
        self.name = name
        self.tel = tel

    def set_name(self, name):
        self.name = name

    def set_tel(self, tel):
        self.tel = tel

    def get_name(self):
        return self.name

    def get_tel(self):
        return self.tel

# 6. 생성자에서 이름, 전화번호, 지역, 나이를 입력받을 수 있도록 생성자를 수정하세요.
class more_private_info(private_info):
    def __init__(self, name, tel, address, age):
        self.name = name
        self.tel = tel
        self.address = address
        self.age = age

    def set_address(self, address):
            self.address = address

    def set_age(self, age):
            self.age = age

# 7. 6번에서 정의한 생성자를 통해 본인의 정보를 갖는 객체를 생성해보세요.
person = more_private_info("인성", "010-1111-2222", "판교", 27)

# 8. 나이와 주민번호를 변경할 수 있는 set_address와 set_age 메서드를 추가하세요.
class more_private_info(private_info):
    def __init__(self, name, tel, address, age):
        self.name = name
        self.tel = tel
        self.address = address
        self.age = age
    def set_address(self, address):
        self.address = address
    def set_age(self, age):
        self.age = age

# 9. 7번에서 생성한 객체에 set_age 메서드를 호출하여 만 나이로 수정해보세요.
person.set_age(25)

# 10. private_info 클래스를 활용하여 가족 구성원의 정보를 생성하고
#    이를 파이썬 리스트에 저장해보세요.
#    파이썬 리스트에 저장된 각 항목에 대해 for 루프를 통해 전화번호와 지역을 출력해보세요.
son = more_private_info("아들", "010-1111-1111", "서울", "1")
mum = more_private_info("엄마", "010-2222-2222", "경기도", "2")
dad = more_private_info("아빠", "010-3333-3333", "판교", "3")
sis = more_private_info("여동생", "010-4444-4444", "분당", "4")
bro = more_private_info("형", "010-5555-5555", "부산", "5")

family_list = []

family_list.append(son)
family_list.append(mum)
family_list.append(dad)
family_list.append(sis)
family_list.append(bro)

# family_list = [son, mum, dad, sis, bro]

for info in family_list:
    print(info.tel, info.address)
