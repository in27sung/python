# while 조건문:
# 수행할 문장1
# 수행할 문장2
# 수행할 문장3
from email.headerregistry import Address
from tkinter import Listbox

# -> 조건문에 참일 동안 while문 아래의 문장이 반복해서 수행됨

treeHit = 0
while treeHit < 10:
        treeHit = treeHit + 1
        print(f'나무를 {treeHit}번 찍었습니다.')
        if(treeHit == 10):
            print("나무 넘어갑니다.")


prompt = """
1. Add
2. Del 
3. List
4. Quit 

Enter number: """

# number = 0
# while number != 4: # 입력받은 번호가 4가 아닌 동안 반복
#     print(prompt)
#     number = int(input())

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 팜내를 중지합니다")
        break

print("=" * 80)


a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a, end=" ")
print()
#   1부터 10까지의 숫자 중에서 3의 배수를 뺀 나머지 값을 출력

a = 0
while a <= 10:
    a = a + 1
    if a % 3 == 0: continue
    print(a, end=" ")


# 무한루프
while True:
    print("Ctrl + C를 눌러야 while 문을 빠져나갈 수 있습니다.")