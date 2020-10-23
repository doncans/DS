"""
Generator simply its creates iterable object
when function returns and destroys all its local variables
yield preserves the state of last execution [benifit of saving memory]
benifits of using generator over class iterator
1) you don't need to define iter() and next() methods
2) you don't need to raise stopinteration exception
"""
def remote_controller_next():
    yield "Hello"
    yield "siddhu"
    yield "how are you?"
for msg in remote_controller_next():
    print(msg)
############output##############
# Hello
# siddhu
# how are you?

itr = remote_controller_next()
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
##################output###########
# Hello
# siddhu
# how are you?
# Traceback (most recent call last):
#   File "d:/DJANGO/DS/generators_exp.py", line 16, in <module>
#     print(next(itr))
# StopIteration
#===================Fibonacci===============
