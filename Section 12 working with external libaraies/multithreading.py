# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor
# def func(seconds):
#     print(f"Sleeping for {seconds} second")
#     time.sleep(seconds)
#
# # time1 = time.perf_counter()
# # func(4)
# # func(2)
# # func(1)
# # time2 = time.perf_counter()
# # print(time2-time1)
#
# time1 = time.perf_counter()
# t1 = threading.Thread(target=func,args=[4])
# t2 = threading.Thread(target=func,args=[2])
# t3 = threading.Thread(target=func,args=[1])
#
# t1.start()
# t2.start()
# t3.start()
#
# time2 = time.perf_counter()
# print(time2-time1)

# Practice

import time
import threading

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# time1 = time.perf_counter()
# func(5)
# func(3)
# func(2)
# time2 = time.perf_counter()
# print(time2-time1)

t1 = threading.Thread(target=func,args=[5])
t2 = threading.Thread(target=func,args=[3])
t3 = threading.Thread(target=func,args=[2])

t1.start()
t2.start()
t3.start()