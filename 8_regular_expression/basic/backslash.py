import re
# Backslash

p = re.compile('\\section')

p = re.compile('\\\\section')

p = re.compile(r'\\section')

# 정규식 엔진은 위의 세 가지 표현을 모두 동일하게 처리한다.
# 하지만, 마지막 표현식이 가장 권장되는 방법이다.
# 왜냐하면, Raw String 규칙에 의해 백슬래시를 두 번 사용하지 않아도 된다.

# Raw String
# Raw String이란, 문자열 앞에 r이 붙어 있는 것을 말한다.
# 이는 백슬래시를 문자 그대로 사용하고 싶을 때 사용한다.
# 예를 들어, 정규식 엔진에 \\section이라는 문자열을 전달하고 싶다면, 다음과 같이 작성해야 한다.


