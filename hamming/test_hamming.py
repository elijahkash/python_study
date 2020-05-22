from hamming import Solution

x = Solution()


def test_1():
    assert(x.hammingDistance(93, 73) == 2)


def test_2():
    assert(x.hammingDistance(4, 1) == 2)
