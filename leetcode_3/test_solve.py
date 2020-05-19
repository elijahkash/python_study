from solve import Solution


def test_1():
    assert(Solution.lengthOfLongestSubstring(None, 'bbbb') == 1)


def test_2():
    assert(Solution.lengthOfLongestSubstring(None, 'wqwerq') == 4)


def test_3():
    assert(Solution.lengthOfLongestSubstring(None, '') == 0)


def test_4():
    assert(Solution.lengthOfLongestSubstring(None, 'abcabcbb') == 3)


def test_5():
    assert(Solution.lengthOfLongestSubstring(None, 'a') == 1)
