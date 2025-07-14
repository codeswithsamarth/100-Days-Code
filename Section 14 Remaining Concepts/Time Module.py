import time
i = 0
def while_loop():
    global i
    while(i<1000):
        print(i)
        i+=1


def for_loop():
    for j in range(1000):
        print(j)

# start1 = time.time()
# while_loop()
# end1 = time.time()
# start2 = time.time()
# for_loop()
# end2 = time.time()
#
# print(f"Total Time Used By while loop {end1-start1:.4f}")
# print(f"Total Time Used By For loop {end2-start2:.4f}")



t = time.localtime()
formatted = time.strftime("%Y-%M-%D %H:%M:%S",t)
print(formatted)