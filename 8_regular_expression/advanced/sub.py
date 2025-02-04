# 문자열 바꾸기(sub)

import re

p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes')) # colour socks and colour shoes
# sub 메서드의 첫 번째 매개변수는 "바꿀 문자열(replacement)"이 되고, 두 번째 매개변수는 "대상 문자열"이 된다.

print(p.sub('colour', 'blue socks and red shoes', count=1)) # colour socks and red shoes
# count 매개변수를 사용하면 바꿀 횟수를 지정할 수 있다.

# subn
# subn은 sub와 동일한 기능을 하지만 반환 결과를 튜플로 리턴한다.

p = re.compile('(blue|white|red)')
print(p.subn('colour', 'blue socks and red shoes')) # ('colour socks and colour shoes', 2)

# sub 메서드 사용 시 참조 구문 사용하기

p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')

# \g<그룹이름>을 사용하면 정규식의 그룹 이름을 참조할 수 있다.
print(p.sub('\g<phone> \g<name>', 'park 010-1234-1234')) # 010-1234-1234 park

# \g<그룹이름> 대신 \g<그룹번호>를 사용해도 된다.
print(p.sub('\g<2> \g<1>', 'park 010-1234-1234')) # 010-1234-1234 park

# sub 메서드의 입력 인수로 함수 넣기

def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')) # Call 0xffd2 for printing, 0xc000 for user code.



