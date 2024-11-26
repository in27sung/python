# 1. "itwill" 문자열을 화면에 출력하는 print_name() 함수를 정의하세요.
def print_name():
    print("itwill")

print('-' * 80)
# 2. 1번에서 정의한 함수를 호출하는 방법을 제시하세요.
print_name()

print('-' * 80)
# 3. 1번에서 정의한 print_name() 함수를 100번 호출하세요.
for i in range(100):
    print_name()

print('-' * 80)
# 4. "itwill" 문자열을 화면에 100번 출력하는 print_names() 함수를 정의하세요.
def print_names():
    for i in range(100):
        print(f"{i} itwill")
print_names()

print('-' * 80)
# 5. 아래의 코드는 에러가 발생됩니다. 그 이유에 대해서 생각해보세요.
# hello()
# def hello():
#   print("Hi")

# -> 함수 실행문이 함수 생성되기 전에 실행 하도록 하였기 때문이다.

# 6. 아래 코드의 실행 결과를 예측해보세요.
def message():
  print("A")
  print("B")
message()
print("C")
message()

print('-' * 80)
# 7. 아래 코드의 실행 결과를 예측해보세요.
print("A")

def message():
  print("B")

print("C")
message()

print('-' * 80)
# 8. 아래 코드의 실행 결과를 예측해보세요.
print("A")
def message1():
  print("B")
print("C")
def message2():
  print("D")
message1()
print("E")
message2()

print('-' * 80)
# 9. 아래 코드의 실행 결과를 예측해보세요.
def message1():
  print("A")

def message2():
  print("B")
  message1()

message2()

print('-' * 80)
# 10. 아래 코드의 실행 결과를 예측해보세요.
def message1():
  print("A")

def message2():
  print("B")

def message3():
  for i in range(3):
    message2()
    print("C")
  message1()

message3()