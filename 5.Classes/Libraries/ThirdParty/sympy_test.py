
# sympy
# sympy는 방정식 기호(symbol)를 사용 해 주는 외부 라이브러리이다.
# 터미널에서 pip install sympy 설치

# sympy 사용해보기
# 가진 돈의 2/5로 학용품을 샀다. 학용품을 사는데 쓴 돈이 1,760원이라면 남은돈은?

from fractions import Fraction
import sympy

# 가진 돈을 x라고 하고, sympy 모듈을 사용해서 표현
x = sympy.symbols("x")

# x,y 2개의 미지수가 필요하면 x, y = sympy.symbols('x y')로 표현 가능

# 가진 돈의 2/5는 1,760원이므로 방정식은 x * (2/5) = 1760이다.
# 이를 코드로 표현하면
f = sympy.Eq(x * Fraction('2/5'), 1760)

# f라는 방정식을 세웠으므로 sympy.sloce(f)로 x에 해당하는 값을 구할 수 있음
result = sympy.solve(f)

print(result)
# 2차방정식의 해는 여러 개일 수 있으므로 solve() 함수는 결과값으로 리스트 타입을 리턴
remains = result[0] - 1760
print(f'남은 돈은 {remains}원 입니다.')

# sympy 활용하기
# x^2 = 1과 같은 2차 방정식의 해를 구해 보자.
import sympy
x = sympy.symbols('x')
f = sympy.Eq(x**2, 1)
print(sympy.solve(f))


# 연립방정식의 해 구하기
# x + y = 10
# x - y = 4

import sympy
x, y = sympy.symbols('x y')
f1 = sympy.Eq(x + y, 10)
f2 = sympy.Eq(x - y, 4)
result = sympy.solve([f1, f2])
print(result)

# 미지수가 2개 이상이라면 결괏값이 리스트가 아닌 딕셔너리라는 것에 주의하자.