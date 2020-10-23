"""
Parallel processing
Divide input(Map) and aggregate(Reduce) output
"""
from multiprocessing import Pool
import time
# def fun(n):
#     return n*n

def fun(n):
    sum = 0
    for i in range(n):
        sum  += i*i
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p = Pool(processes=2)
    # p.map(fun, arr)
    result = p.map(fun, range(10000))
    p.close()
    p.join()
    # result = []
    # for n in arr:
    #     result.append(fun(n))
    print("Pool took : ", time.time()-t1)
    t2 = time.time()
    for i in range(10000):
        result.append(fun(i))
    print("serial processing took: ", time.time()-t2)

    #output
    # Pool took :  2.0030744075775146
    # serial processing took:  5.65215802192688

    # if take processes=3 in Pool
    # Pool took :  2.8116846084594727
    # serial processing took:  5.556454420089722
  

    #if i take processes = 2
    #Pool took :  3.380298376083374
    # serial processing took:  5.721689462661743
