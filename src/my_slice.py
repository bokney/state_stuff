import itertools

iterator = itertools.islice("ABCDEFG", 4)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


class BungoSliceIterator:
    def __init__(self, lst, exclusive_stop):
        self.lst = lst
        self.exclusive_stop = exclusive_stop
        self.current_index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            if self.current_index == self.exclusive_stop:
                raise StopIteration
            current_item = self.lst[self.current_index]
            self.current_index += 1
            return current_item
        except StopIteration:
            pass

class BungoSliceIterable:
    def __init__(self, lst, exclusive_stop):
        self.lst = lst
        self.exclusive_stop = exclusive_stop

    def __iter__(self):
        return BungoSliceIterator(self.lst, self.exclusive_stop)
    

nums = [5, 6, 7, 8]

# my_iterator = BungoSliceIterator(nums, 3)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# print(next(my_iterator))
# print(next(my_iterator))

bungo = BungoSliceIterable(nums, 7)

for i in bungo:
    print(i)

# for j in bungo:
#     print(j)