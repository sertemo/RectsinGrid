from rectgrid.counter import Counter

def test_counter_add():
    counter = Counter()
    counter.add()
    assert counter.count == 2