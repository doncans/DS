"""
Resouces can not be accessed at the same time by two people(example restroom)
"""
import time
import multiprocessing

def deposit(bal, lock):
    for _ in range(100):
        time.sleep(0.01)
        lock.acquire()
        bal.value = bal.value + 1
        lock.release()
def withdraw(bal, lock):
    for _ in range(30):
        time.sleep(0.01)
        lock.acquire()
        bal.value = bal.value - 1
        lock.release()

if __name__ == "__main__":
    bal = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(bal,lock))
    w = multiprocessing.Process(target=withdraw, args=(bal,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(bal.value)