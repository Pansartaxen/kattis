# import time
# start = time.time()
# for i in range(200000):
#     print(i)
# end = time.time()
# print(end-start)
# import random

# for i in range(1,10000):
#     print(i)

import time
import threading as th

def calc_one():
    for n in range(0,50000):
        print(1+n*4)

def calc_two():
    for n in range(0,50000):
        print(2+n*4)

def calc_three():
    for n in range(0,50000):
        print(3+n*4)

def calc_four():
    for n in range(0,50000):
        print(4+n*4)

t = time.time()

t1 = th.Thread(target=calc_one)
t2 = th.Thread(target=calc_two)
t3 = th.Thread(target=calc_three)
t4 = th.Thread(target=calc_four)


t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
print("done in:",time.time()-t)