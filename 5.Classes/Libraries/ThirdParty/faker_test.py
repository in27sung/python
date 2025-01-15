# Faker
# Faker는 테스트용 가짜 데이터를 생성할 때 사용하는 라이브러리이다.

# 왼쪽 항목에서 >_ 터미널 실행(⌥+F12)
# pip install Faker

# Faker 사용해 보기
# Faker를 사용해 테스트 데이터를 만들기

from faker import Faker
fake = Faker()
fake_name = fake.name() # 무작위 이름 리턴
print(fake_name)

# 한글 이름이 필요하면 ko-KR 전달
fake = Faker('ko-KR')
fake_name_kr = fake.name()
print(fake_name_kr)

print('-' * 80)

print(fake.address()) # 무작위로 생성한 한국 주소를 리턴

print('-' * 80)

# 이름과 주소를 쌍으로 하는 30건의 테스트 데이터 생성
test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)

# Faker 활용하기
# fake.name(): 이름
# fake.address(): 주소
# fake.postcode(): 우편번호
# fake.country(): 국가명
# fake.company(): 회사명
# fake.job(): 직업명
# fake.phone_number: 휴대폰 번호
# fake.email(): 이메일 주소
# fake.user_name(): 사용자명
# fake.pyint(min_value=0, max_value=100): 0부터 100 사이의 임의의 숫자
# fake.ipv4_priavet(): ip주소
# fake.text(): 임의의 문장(한글 임의의 문장은 fake.catch_phrase() 사용)
