
# greedy와 non-greedy
import re

s = '<html><head><title>Title</title>'
print(len(s)) # 32

print(re.match('<.*>', s).span()) # (0, 32)

print(re.match('<.*>', s).group()) # <html><head><title>Title</title>

# <.*> 정규식은 < 문자가 나타날 때까지 < 문자를 포함하여 모든 문자를 매치한다.
# 따라서 <html> 문자열 전체가 매치된다.
# 하지만 이렇게 전체 문자열을 소비하는 것을 막기 위해서는 non-greedy 문자인 ?를 사용해야 한다.
print(re.match('<.*?>', s).group()) # <html>

# non-greedy 문자인 ?는 *?, +?, ??, {m,n}?와 같이 사용할 수 있다.
# *?, +?, ??, {m,n}?는 가능한 한 가장 최소한의 반복을 수행하도록 도와준다.
