# 1. for문의 실행결과를 예측하세요.
fruit = ["사과", "귤", "수박"]
for i in fruit:
  print(i)

# 2. for문의 실행결과를 예측하세요.
fruit = ["사과", "귤", "수박"]
for i in fruit:
  print("#####")

# 3. 다음 for문과 동일한 기능을 수행하는 코드를 작성하세요.
# for 변수 in ["A", "B", "C"]:
#   print(변수)
변수 = ["A", "B", "C"]

print(변수)

# 4. for문을 풀어서 동일한 동작을 하는 코드를 작성하세요.
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환",b)

변수 = ['A', 'B', 'C']
print(변수[0].lower())
print(변수[1].lower())
print(변수[2].lower())


# 5. 다음 코드를 for문으로 작성하세요.
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)

for num in ['10', '20', '30']:
    print(num)

# 6. 다음 코드를 for문으로 작성하세요.
# print(10)
# print(20)
# print(30)
for num in [10, 20 ,30]:
    print(num)

# 7. 다음 코드를 for문으로 작성하세요.
# print(10)
# print("----------")
# print(20)
# print("----------")
# print(30)
# print("----------")

for num in [10, 20, 30]:
    print(num)
    print("-" * 10)

# 8. 다음 코드를 for문으로 작성하세요.
# print("++++")
# print(10)
# print(20)
# print(30)

for j in ["++++", 10, 20 , 30]:
    print(j)


# 9. 다음 코드를 for문으로 작성하세요.
# print("----------")
# print("----------")
# print("----------")
# print("----------")

for i in range(1, 5):
    print("----------")