from solve import Solution

test_obj = Solution()


def test_1():
    assert(test_obj.countSquares([
                                 [0, 1, 1, 1],
                                 [1, 1, 1, 1],
                                 [0, 1, 1, 1]]) == 15)


def test_2():
    assert(test_obj.countSquares([
                                 [1, 0, 1],
                                 [1, 1, 0],
                                 [1, 1, 0]]) == 7)


def test_3():
    assert(test_obj.countSquares([[1]]) == 1)
