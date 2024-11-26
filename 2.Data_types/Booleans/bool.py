
# True, False는 파이썬의 예약어로 첫 글자는 대문자로 사용해야 한다.
a = True;
b = False;

print(type(a))
print(type(b))

num = 1
print(type(num))

print(1 == 1)

print(2 > 1)

print(2 < 1)

# 자료형 참과 거짓
# 거짓 - string(""), list[], tuple(), number 0

# 참과 거짓 활용(while)
a = [1, 2, 3, 4]
while a: # a가 참인동안(리스트 내부에 값이 있으면 참)
    print(a.pop()) #pop() 함수는 마지막 요소를 순차적으로 꺼냄, 리스트에서는 삭제

if []: #False
    print('True')
else:
    print("False")

if [1, 2, 3]:
    print("True")
else:
    print("False")

# 불 연산
print(bool('Python')) # 빈 문자가 아니므로 True
print('')
print(bool(''))
print(bool([1, 2, 3]))
print('-' * 80)

print(bool([]))
print(bool(0))
print(bool(3))