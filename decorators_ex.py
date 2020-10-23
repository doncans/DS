import time
"""
1> Decorators allows you to wrap your function in another function
2> Decorators solve code duplication and cluttering main logic with additional functionality
"""
# def cal_sqr(numbers):
#     start = time.time()
#     result = []
#     for number in numbers:
#         result.append(number*number)
#     end = time.time()
#     print("cal sqr took : " + str((end-start)*1000) + "mil sec")
#     return result
# def cal_cube(numbers):
#     start = time.time()
#     result = []
#     for number in numbers:
#         result.append(number*number*number)
#     end = time.time()
#     print("cal cube took : " + str((end-start)*1000) + " mil sec")
#     return result

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__+" took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper
@time_it
def cal_sqr(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result
@time_it
def cal_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

if __name__=="__main__":
    cal_sqr(range(1,100000))
    cal_cube(range(1,100000))
    #normal functions 
    # cal sqr took : 12.93325424194336mil sec
    # cal cube took : 19.97852325439453 mil sec
    #After decorator
    # cal_sqr took 16.924142837524414 mil sec
    # cal_cube took 19.947528839111328 mil sec
    # ==========================================Use Cases==============
    #Logging
    #Timing