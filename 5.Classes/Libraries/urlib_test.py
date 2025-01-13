# urllib
# urllib은 URL을 읽고 분석할 때 사용하는 모듈이다.
# ex
# https://wikidocs.net/페이지_번호(예: https://wikidocs.net/12)

import urllib.request
import ssl
import certifi

def get_wikidocs(resource_id):
    resource = f"https://wikidocs.net/{resource_id}"
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(resource, context=context) as s:
        with open('wikidocs_%s.html' % resource_id, 'wb') as f:
            f.write(s.read())

get_wikidocs(12)


# get_wikidocs(page)는 위키독스의 페이지 번호를 입력받아 해당 페이지의 리소스 내용을 파일로 저장하는 함수이다.
# 이 코드에서 보듯이 urllib.request.urlopen(resource)로 s 객체를 생성하고 s.read()로 리소스 내용 전체를
# 읽어 이를 저장할 수 있다. 예를 들어 get_wikidocs(12)라고 호출하면 https://wikidocs.net/12 웹 페이지를
# html 파일로 저장한다.

