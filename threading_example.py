import threading
import time
cube_result = []
sqr_result = []
def cal_sqr(arr):
    # global sqr_result
    time.sleep(0.2)
    for i in arr:
        sqr_result.append(i*i)
    print(sqr_result)
def cal_cube(arr):
    time.sleep(0.2)
    for i in arr:
        cube_result.append(i*i*i)
    print(cube_result)

if __name__ == "__main__":
    arr = range(1, 100, 3)
    # t = time.time()
    # cal_sqr(arr)
    # cal_cube(arr)
    # print("done in : ", time.time()-t)
    tt = time.time()
    t1 = threading.Thread(target=cal_sqr, args=(arr,))
    t2 = threading.Thread(target=cal_cube, args=(arr,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Threads done in :", time.time()-tt)