from find_median import Solution


def test_1():
	assert(Solution.findMedianSortedArrays(None, [1, 3], [2]) == 2)


def test_2():
	assert(Solution.findMedianSortedArrays(None, [1, 2], [3, 4]) == 2.5)


def test_3():
	assert(Solution.findMedianSortedArrays(None, [1, 3, 9], [0]) == 3)
