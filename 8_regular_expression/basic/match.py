# match 객체의 메서드
# group() 매치된 문자열을 리턴한다.
# start() 매치된 문자열의 시작 위치를 리턴한다.
# end() 매치된 문자열의 끝 위치를 리턴한다.
# span() 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.

import re

p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())

print(m.start()) # 0

print(m.end()) # 6

print(m.span()) # (0, 6)

p = re.compile('[a-z]+')
m = p.match("python")

m = re.match('[a-z]+', "python")

m = p.search("3 python")

print(m.group())

print(m.start()) # 2

print(m.end()) # 8

print(m.span()) # (2, 8)

