from find_median import Solution



def test_1():
	assert(Solution.findMedianSortedArrays(None, [], [4]) == 4)
def test_2():
	assert(Solution.findMedianSortedArrays(None, [], [-1, 2]) == 0.5)
def test_3():
	assert(Solution.findMedianSortedArrays(None, [1, 3, 6], []) == 3)
def test_4():
	assert(Solution.findMedianSortedArrays(None, [1, 3, 6, 9], []) == 4.5)
def test_5():
	assert(Solution.findMedianSortedArrays(None, [3], [2]) == 2.5)
def test_6():
	assert(Solution.findMedianSortedArrays(None, [2], [5]) == 3.5)
def test_7():
	assert(Solution.findMedianSortedArrays(None, [3, 4], [2]) == 3)
def test_8():
	assert(Solution.findMedianSortedArrays(None, [3, 5], [7]) == 5)
def test_9():
	assert(Solution.findMedianSortedArrays(None, [3, 7], [4]) == 4)
def test_10():
	assert(Solution.findMedianSortedArrays(None, [3, 5, 7], [2]) == 4)
def test_11():
	assert(Solution.findMedianSortedArrays(None, [3, 4, 6], [9]) == 5)
def test_12():
	assert(Solution.findMedianSortedArrays(None, [4, 6, 9], [7]) == 6.5)
def test_13():
	assert(Solution.findMedianSortedArrays(None, [1, 7, 8], [3]) == 5)


def test_14():
	assert(Solution.findMedianSortedArrays(None, [1, 2], [3, 4]) == 2.5)
def test_15():
	assert(Solution.findMedianSortedArrays(None, [5, 7], [3, 4]) == 4.5)
def test_16():
	assert(Solution.findMedianSortedArrays(None, [1, 3], [2, 4]) == 2.5)
def test_17():
	assert(Solution.findMedianSortedArrays(None, [5, 7], [1, 6]) == 5.5)
def test_18():
	assert(Solution.findMedianSortedArrays(None, [1, 5, 7], [0, 4, 9]) == 4.5)

def test_20():
	assert(Solution.findMedianSortedArrays(None, [1, 3, 9], [-1, 0]) == 1)
def test_21():
	assert(Solution.findMedianSortedArrays(None, [1, 3, 5], [7, 9]) == 5)
def test_22():
	assert(Solution.findMedianSortedArrays(None, [1, 3, 9], [2, 6]) == 3)

def test_23():
	assert(Solution.findMedianSortedArrays(None, [1, 3, 5, 8, 9, 11, 13], [-1, 4, 7, 12]) == 7)
def test_24():
	assert(Solution.findMedianSortedArrays(None, [1, 3, 5, 8, 9, 11], [4, 7, 12]) == 7)
def test_25():
	assert(Solution.findMedianSortedArrays(None, [1, 3, 7, 8, 9, 11], [4, 5, 12]) == 7)
def test_92():
	assert(Solution.findMedianSortedArrays(None, [3, 5, 7, 9], [6]) == 6)

# test_11()
