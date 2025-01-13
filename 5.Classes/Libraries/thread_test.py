# threading
# 컴퓨터에서 동작하는 있는 프로그램을 프로세스라고한다. 보통 1개의 프로세스는 1가지 일만 하지만,
# 스레드를 사용하면 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.

# import time

# def long_task():             # 1초의 시간이 걸리는 함수
#     for i in range(5):
#         time.sleep(1)        # 1초 대기
#         print("working:%s\n" % i)
# print("Start")
#
# for i in range(5):
#     long_task()
#
# print("End")

# long_task는 수행하는 데 5초의 시간이 걸리는 함수이다.위 프로그램은 이 함수를 총 5번 반복해서
# 수행하는 프로그램이다. 이 프로그램은 5초가 5번 반복되므로 총 25초의 시간이 걸린다.

# 하지만 앞에서 설명했듯이 스레드를 사용하면 5초의 시간이 걸리는 long_task 함수를 동시에
# 실행할 수 있으므로 시간을 줄일 수 있다.

# import time
# import threading
#
# def long_task():             # 1초의 시간이 걸리는 함수
#     for i in range(5):
#         time.sleep(1)        # 1초 대기
#         print("working:%s\n" % i)
#         print("-" * 80)
#
# print("Start")
#
# threads = []
# for i in range(5):
#     # long_task()
#     t = threading.Thread(target=long_task) # 스레드를 생성
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# print("End")




import time
import threading

def long_task():             # 1초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)        # 1초 대기
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    # long_task()
    t = threading.Thread(target=long_task) # 스레드를 생성
    threads.append(t)

for t in threads: # 스레드를 실행
    t.start()

for t in threads: # join으로 스레드가 종료될 때 까지 대기
    t.join()

print("End")

