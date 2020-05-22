from zigzag import Solution

obj = Solution()


def test_1():
    assert(obj.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')


def test_2():
    assert(obj.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')

# test_2()
