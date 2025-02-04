
# 정규표현식 사용예제

# 전체 텍스트를 공백 문자로 나눈다(split)
# 나뉜 단어가 주민등록번호 형식인지 조사한다.
# 주민등록번호 형식이면, 주민등록번호 뒷자리를 *로 바꾼다.
# 모든 단어를 다시 조립한다.

data = """
park 800905-1049118
kim 700905-1059119
"""

for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    print(" ".join(word_result))

# 정규표현식을 사용하면 코드가 훨씬 간결해진다.

import re

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

# compile 함수를 사용하면 정규표현식을 여러 번 사용할 때 일정한 속도의 이점이 있다.
# ab*는 a 뒤에 b가 0개 이상 있는 문자열과 매치된다.
p = re.compile('ab*')

# [a-z]+는 소문자로 이루어진 단어와 매치된다.
p = re.compile('[a-z]+')

# match()는 문자열의 처음부터 정규식과 매치되는지 조사한다.
m = p.match("python")
print(m)
m = p.match("3 python")
print(m)

# search()는 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
m = p.search("python")
print(m)
m = p.search("3 python")
print(m)

# findall()는 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
result = p.findall("life is too short")
print(result)

# finditer()는 정규식과 매치되는 모든 문자열(substring)을 iterator 객체로 리턴한다.
result = p.finditer("life is too short")
print(result)
# <callable_iterator object at 0x102b6cc70>

for r in result: print(r)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>

