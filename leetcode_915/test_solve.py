from solve import Solution


def test_1():
    assert(Solution.partitionDisjoint(None, [5, 0, 3, 8, 6]) == 3)


def test_2():
    assert(Solution.partitionDisjoint(None, [1, 1, 1, 0, 6, 12]) == 4)


def test_3():
    assert(Solution.partitionDisjoint(None, [1, 5]) == 1)


def test_4():
    assert(Solution.partitionDisjoint(None, [29, 33, 6, 4, 42, 0, 10, 22, 62, 16, 46, 75, 100, 67, 70, 74, 87, 69, 73, 88]) == 11)


def test_5():
    assert(Solution.partitionDisjoint(None, [1, 1]) == 1)
