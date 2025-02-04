
# 제너레이터 활용하기
import time
def longtime_job():
    print("job start")
    time.sleep(1)
    print("job end")
    return "done"

# list_job = [longtime_job() for i in range(5)]
# 제너레이터 표현식으로 변경
list_job = (longtime_job() for i in range(5))

# print(list_job)
# 제너레이터 표현식으로 인해 longtime_job()함수가 실행되지 않고 제너레이터 객체만 생성됩니다.
# 제너레이터 객체는 next 함수를 호출할 때마다 함수를 실행합니다.
# lazy evaluation을 사용하여 필요할 때만 함수를 실행할 수 있습니다.
print(next(list_job))

# 제너레이터는 이터레이터를 생성해주는 함수입니다.