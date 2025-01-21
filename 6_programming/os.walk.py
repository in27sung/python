# 하위 디렉터리 검색을 쉽게 해 주는 os.walk

import os

for (path, dir, files) in os.walk("/Users/Insung/Documents/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))