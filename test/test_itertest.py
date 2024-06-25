import pytest
from src.itertest import DungoRepeater

# attributes
# times defualted to None
# when invoked with iter, returns self
# repeats multiple times
# errors when times is reached

@pytest.mark.it("Class has correct attributes")
def test_repeat_has_attributes():
    test_list = ['a', 'b', 'c', 'd']
    instance = DungoRepeater(test_list, 3)
    assert hasattr(instance, 'item')
    assert hasattr(instance, 'times')
    assert instance.item == ['a', 'b', 'c', 'd']
    assert instance.times == 3

@pytest.mark.it("When passed no times argument defaults to None")
def test_repeat_has_default_times():
    instance = DungoRepeater(5)
    assert instance.times is None

@pytest.mark.it("When invoked with iter returns itself")
def test_repeat_returns_itself_when_iter_invoked():
    test_repeat = DungoRepeater(5, times=3)
    assert iter(test_repeat) is test_repeat

@pytest.mark.it("Whe limit is not set next can be called infefinitely")
def test_repeat_returns_object_indefinitely():
    test_repeat = DungoRepeater(5)
    for i in range(100):
        assert next(test_repeat) == 5

@pytest.mark.it("When no of times is reached raise StopIteration exceptopn")
def test_repeat_with_times_raiseing_exception():
    test_repeat = DungoRepeater(5, times=2)
    next(test_repeat)
    next(test_repeat)

    with pytest.raises(StopIteration):
        next(test_repeat)