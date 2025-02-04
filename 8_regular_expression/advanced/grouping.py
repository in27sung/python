
# 그루핑
import re

p = re.compile('(ABC)+') # ABC 문자열이 계속해서 반복되는지 조사
m = p.search('ABCABCABC OK?')

print(m) # <re.Match object; span=(0, 9), match='ABCABCABC'>

print(m.group()) # ABCABCABC

# 그루핑된 문자열에 이름 붙이기
p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')

print(m.group('name')) # park
print(m.group(1)) # park
print(m.group(2)) # 010-1234-1234
print(m.group(3)) # 010

# 그루핑된 문자열 재참조(Backreferences)
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
m = p.search('Paris in the the spring')
print(m.group()) # the the

# 전방 탐색(Lookahead Assertions)
p = re.compile('.+:')
m = p.search('http://google.com')
print(m.group()) # http:

# 긍정형 전방 탐색(?=...): ...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# 긍정형 전방 탐색(Possitive Lookahead Assertions)
p = re.compile('.+(?=:)')
m = p.search('http://google.com')
print(m.group()) # http

# 부정형 전방 탐색(?!...): ...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# 부정형 전방 탐색(Negative Lookahead Assertions)

# foo.bar, autoexec.bat, sendmail.cf 파일 매치

# .*[.].*$ : 파일 이름 + . + 확장자

# .*[.]([^b]..|.[^a].|..[^t])$ : bat가 아닌 파일

# .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$

# .*[.](?!bat$).*$
p = re.compile('.*[.](?!bat$).*$')
m = p.search('autoexec.bat')
print(m) # None

m = p.search('autoexec.exe')
print(m) # <re.Match object; span=(0, 12), match='autoexec.exe'>

p = re.compile('.*[.](?!bat$|exe$).*$')
m = p.search('autoexec.exe')
print(m)

