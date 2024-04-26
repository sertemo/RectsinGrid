from rectgrid.counter import RectCounter

def test_counter_add_1():
    counter = RectCounter()
    counter.add()
    assert counter.count == 1


def test_counter_add_3():
    counter = RectCounter()
    counter.add()
    counter.add()
    counter.add()
    assert counter.count == 3