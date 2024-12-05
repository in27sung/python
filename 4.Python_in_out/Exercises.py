from idlelib.replace import replace


# Q1 홀수, 짝수 판별하기
# 주어진 자연수가 호수인지, 짝수인지 판별해 주는 히ㅏㅁ수 is_odd를 작성해 보자. is_odd 함수는 홀수이면 True,
# 짝수이면 False를 리턴해야 한다.

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
print(is_odd(3))

# Q2모든 입력의 평균값 구하기
# 입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. 단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return print(result / len(args))

avg_numbers(1, 2)
avg_numbers(1, 2, 3, 4, 5)

# Q3 프로그램 오류 수정하기 1
# 다음은 2개의 숫자를 입력받아 더한 후에 리턴하는 프로그램이다.

input1 = input("첫 번째 숫자를 입력하세요: ")
input2 = input("두 번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %s입니다." % total)

# Q4 출력 결과가 다른 것은?
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

# Q5 프로그램 오류 수정하기 2
# 다음은 파일(test.txt)에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어 출력하는 프로그램이다.

f1 = open("test.txt", 'w')
f1.write("Life is too short \n")
f1.close()

f2 = open("test.txt", 'r')
read = f2.read()
print(read)
f2.close()

# with 문
with open("test.txt", 'w') as f1:
    f1.write("Life is too short")
with open("test.txt", 'r') as f2:
    print(f2.read())

# Q6 사용자 입력 저장하기
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. 단, 프로그램을 다시 실행하더라도
# 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.
user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()

# Q7 파일의 문자열 바꾸기
# 다음과 같은 내용을 지닌 test.txt가 있다. 이 파일의 내용중 "java"라는 문자열을 "python"으로 바꾸어 저장해 보자.

f = open('test.txt', 'r')
body = "Life is too short\nyou need java\n"
f.close()
body = body.replace('java', 'python')
f = open('test.txt', 'w')
f.write(body)
f.close()



