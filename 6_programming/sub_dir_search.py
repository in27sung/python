# 1. 다음과 같이 sub_dir_search.py 파일을 생성하고 다음과 같이 코드를 작성해 보세요.

def search(dirname):
    print(dirname)

search("/Users/Insung/PycharmProjects/python/6_programming")

# 2. 이제 이 함수를 사용하여 /Users/Insung/PycharmProjects/python/6_programming 디렉터리에 있는 파일들을 출력해 보세요.
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
search("/Users/Insung/PycharmProjects/python/6_programming")



