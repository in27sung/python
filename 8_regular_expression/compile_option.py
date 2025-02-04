
# 컴파일 옵션
# re.compile() 함수는 정규 표현식을 컴파일할 때 다양한 옵션을 사용할 수 있다.

# DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
# MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
# VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)

# DOTALL, S
# . 메타 문자는 줄바꿈 문자(\n)를 제외한 모든 문자와 매치되는 규칙이 있다.
# 만약 \n 문자도 포함하여 매치하고 싶다면 re.DOTALL 또는 re.S 옵션을 사용해 정규식을 컴파일하면 된다.

import re

p = re.compile('a.b')
m = p.match('a\nb')
print(m) # None

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m) # <re.Match object; span=(0, 3), match='a\nb'>


# IGNORECASE, I
# re.IGNORECASE 또는 re.I 옵션은 대소문자 구별 없이 매치를 수행할 때 사용한다.

p = re.compile('[a-z]', re.I)
print(p.match('python')) # <re.Match object; span=(0, 1), match='p'>

print(p.match('Python')) # <re.Match object; span=(0, 1), match='P'>

print(p.match('PYTHON')) # <re.Match object; span=(0, 1), match='P'>

# MULTILINE, M
# re.MULTILINE 또는 re.M 옵션은 여러줄과 매치할 때 사용한다.
# ^는 문자열의 처음을 의미하고, $는 문자열의 마지막을 의미한다.
# 예를 들어 정규식이 ^python인 경우 문자열의 처음은 항상 python으로 시작해야 매치되고,
# 정규식이 python$인 경우 문자열의 마지막은 항상 python으로 끝나야 매치된다.

p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) # ['python one']e

p = re.compile("^python\s\w+", re.MULTILINE)
print(p.findall(data)) # ['python one', 'python two', 'python three']

# VERBOSE, X
# re.VERBOSE 또는 re.X 옵션은 정규식을 주석 또는 여러 줄로 작성할 수 있게 해준다.

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#]                # Start of a numeric entity reference
(
    0[0-7]+         # Octal form
    | [0-9]+        # Decimal form
    | x[0-9a-fA-F]+ # Hexadecimal form
)
;                   # Trailing semicolon
""", re.VERBOSE)
