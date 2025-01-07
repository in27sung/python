# operator.itemgetter
# operator.itemgetter는 주로 sorted와 같은 함수의 key 매개변수에 적용하여
# 다양한 기준으로 정렬할 수 있도록 도와주는 모듈

# 예를 들어 학생의 이름, 나이, 성적 등의 정보를 저장한 students 리스트가 있다고 가정하면
# students 리스트에 3개의 튜플이 있으며 각 튜플은 순서대로 이름, 나이, 성적에 해당하는
# 데이터로 이루어졌다.
# 이 리스트를 나이순은로 정렬할 때 operator.itemgetter를 활용할 수 있음
from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result = sorted(students, key=itemgetter(1))
print(result)
# [('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]
# itemgetter(1)은 students의 아이템인 튜플의 두 번째 요소를 기준으로 정렬
# itemgetter(2)를 사용하면 성적순으로 정렬한다.

# ---------------------------------------------------------------------
# students 요소가 딕셔너리일 때

students = [
    {"name":"jane", "age":22, "grade": 'A'},
    {"name":"dave", "age":32, "grade": 'B'},
    {"name":"sally", "age":17, "grade": 'B'},
]

result = sorted(students, key=itemgetter('age'))
print(result)
# [{'name': 'sally', 'age': 17, 'grade': 'B'}, {'name': 'jane', 'age': 22, 'grade': 'A'}, {'name': 'dave', 'age': 32, 'grade': 'B'}]
# age 순으로 정렬된다.

# operator.attrgetter()
# students 리스트의 요소가 튜플이 아닌 Student 클래스의 객체라면 다음처럼 attrgetter()를 적용하여
# 정렬해야 한다.

from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B'),
]

result = sorted(students, key=attrgetter('age'))
print(result)

sort_list = []
for s in result:
    sort_list.append(s.name)
print(sort_list)

print("나이가 적은 순서대로 출력하면: ")
for name in sort_list:
    print(f'{name} 순서이다.')

sort_list2 = [s.name for s in result]
print(sort_list2)

# 나이가 적은 순서대로 이름을 출력
print("나이가 적은 순서대로 출력하면: " + ", ".join(sort_list2) + " 순서이다.")
