from solve import Solution

obj = Solution()


def test_1():
    assert(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
