import multiprocessing
import time
cube_result = []
sqr_result = []
def cal_sqr(arr):
    # global sqr_result

    for i in arr:
        time.sleep(0.5)
        sqr_result.append(i*i)
    print(sqr_result)
def cal_cube(arr):
    for i in arr:
        time.sleep(0.5)
        cube_result.append(i*i*i)
    print(cube_result)

if __name__ == "__main__":
    arr = range(1, 30, 3)
    # t = time.time()
    # cal_sqr(arr)
    # cal_cube(arr)
    # print("done in : ", time.time()-t)
    tt = time.time()
    p1 = multiprocessing.Process(target=cal_sqr, args=(arr,))
    p2 = multiprocessing.Process(target=cal_cube, args=(arr,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("processs done in :", time.time()-tt)