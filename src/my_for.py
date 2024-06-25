

def my_for(iterable, action_func):
    iterator = iter(iterable)
    try:
        item = next(iterator)
        action_func(item)
        my_for(iterator, action_func)
    except StopIteration:
        pass


nums = [5, 6, 7, 8]

def double_print(num):
    print(num * 2)


my_for(nums, double_print)