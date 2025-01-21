
# 게시판 페이징하기

def get_total_page(m, n): # m: 총 건수, n: 한 페이지에 보여줄 게시물 수
    if m % n == 0:
        return m // n
    else:
        return m // n + 1
