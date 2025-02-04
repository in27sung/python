
# 문자열 소비가 없는 메타 문자
# ^ : 문자열의 시작
# $ : 문자열의 끝
# \b : 단어 경계
# \B : non-word boundary
# (?=...) : 긍정형 전방 탐색
# (?!...) : 부정형 전방 탐색
# (?<=...) : 긍정형 후방 탐색
# (?<!...) : 부정형 후방 탐색
# (?P<name>...) : 그룹 이름 지정
# (?P=name) : 그룹 이름 참조
# (?(id/name)yes|no) : 조건부 그룹

# | : or
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m) # <re.Match object; span=(0, 4), match='Crow'>

# ^ : 문자열의 시작
print(re.search('^Life', 'Life is too short')) # <re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life')) # None

# $ : 문자열의 끝
print(re.search('short$', 'Life is too short')) # <re.Match object; span=(12, 17), match='short'>
print(re.search('short$', 'Life is too short, you need python')) # None

# \A : 문자열의 처음
print(re.search('\ALife', 'Life is too short')) # <re.Match object; span=(0, 4), match='Life'>
print(re.search('\ALife', 'My Life')) # None

# \Z : 문자열의 끝
print(re.search('short\Z', 'Life is too short')) # <re.Match object; span=(12, 17), match='short'>
print(re.search('short\Z', 'Life is too short, you need python')) # None

# \b : 단어 경계(Word boundary)
p = re.compile(r'\bclass\b')
print(p.search('no class at all')) # <re.Match object; span=(3, 8), match='class'>
print(p.search('the declassified algorithm')) # None
print(p.search('one subclass is')) # None

# \B : non-word boundary
p = re.compile(r'\Bclass\B')
print(p.search('no class at all')) # None

print(p.search('the declassified algorithm')) # <re.Match object; span=(6, 11), match='class'>r
print(p.search('one subclass is')) # None