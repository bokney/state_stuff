
# class DungoStateIterable:

#     def __init__(self, func) -> None:
#         self.func = func

class DungoRepeater:

    def __init__(self, item, times=None):
        self._count = 0
        self.item = item
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self._count == self.times:
            raise StopIteration
        self._count += 1
        return self.item


# def repeat(object, times=None):
#     # repeat(10, 3) -> 10 10 10
#     if times is None:
#         while True:
#             yield object
#     else:
#         for i in range(times):
#             yield object

