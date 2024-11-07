# 정렬과 공백
test = "%10s" % "hi"
print(test)
#        hi: 총 10칸의 문자열 공간이 생겨나고 오른쪽 정렬로 앞의 공백 8칸 후에 hi 출력

test = "%-10s" % "hi"
print(test)

test = "%-10sjane." % "hi"
print(test)

# 소수점 표현하기
test = "%0.4f" % 3.42134234
print(test)

test = "%10.4f" % 3.42134234
print(test)
