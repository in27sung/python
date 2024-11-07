#1. letters 변수에 아래와 같은 값이 설정(바인딩) 되어 있다. 첫번째와 세번째 문자를 출력하세요.

letters = 'python'
# 실행 예: p t
print(letters[0], letters[2])

#2. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "18주 1827"
print(license_plate[4:])
print(license_plate[-4:])

#3. 아래의 문자열에서 '홀'만 출력하세요. 인덱싱 끝에: 숫자를 넣어서 증가값을 줄 수 있습니다.
# (예: 2 2칸씩 이동하면서)
str = "홀짝홀짝홀짝"
print(str[0::2])
print(str[::2])

#4. 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
print(string[::-1])
print(string[:4:-1]) # NOHT


#5. 아래의 코드의 실행 결과를 예상해보세요.
lang = "python"
# lang[0] = 'P'
# TypeError: 'str' object does not support item assignment
print(lang)

# 6. 5번의 결과를 본 후 첫 글자가 대문자 'P'가 되도록 출력해보세요
print('P'+ lang[1:])


# 7. 아래의 변수에 각각 값이 저장되어 있을 때 print() 함수의 결과를 예상해보세요.
# a = '3'
# b = '4'
# print(a+b)
# 34

# 8. 아래의 결과를 만들어 보세요.
print("Hi" * 3)

# 9. 화면에 하이픈('-')을 80개 출력하세요.
print('-' * 80)

# 10. 아래의 변수와 문자열 곱하기를 활용하여 아래의 실행화면을 출력하세요.
t1 = 'python'
t2 = 'java'
# 실행 예: python java python java python java python java
print((t1 +' ' + t2 + ' ') * 4)
