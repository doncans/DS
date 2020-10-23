import multiprocessing

# result = []
def cal_sqr(numbers, q):
    # global result
    for i in numbers:
        # result.append(i*i)
        q.put(i*i)
    # print("inside process : "+str(result))


if __name__=="__main__":
    numbers = range(10)
    q = multiprocessing.Queue()
    # p = multiprocessing.Process(target=cal_sqr, args=(numbers,))
    p = multiprocessing.Process(target=cal_sqr, args=(numbers,q))
    p.start()
    p.join()
    # print("outside process"+str(result))
    #before sharing 
    # inside process : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    # outside process[]
    while q.empty() is False:
        print(q.get())

"""
multiprocessing Queue lives in shared memory
used to share data b/w processes
-----------
Queue Module
lives in in-process memory
used to share data b/w threads
"""