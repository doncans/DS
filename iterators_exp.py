class RemoteController:
    def __init__(self):
        self.channels = ["HBO", "cnn", "TV5", "MaaTv", "Gemini"]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index +=  1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

if __name__ == "__main__":
    r = RemoteController()
    itr = iter(r)
    print(next(itr)) 
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    #######output########
    # HBO
    # cnn
    # TV5
    # MaaTv
    # Gemini
    # Traceback (most recent call last):
    # File "d:/DJANGO/DS/iterators_exp.py", line 21, in <module>
    #     print(next(itr))
    # File "d:/DJANGO/DS/iterators_exp.py", line 10, in __next__
    #     raise StopIteration
    # StopIteration

