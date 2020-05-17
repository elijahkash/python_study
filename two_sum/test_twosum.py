from solution import Solution

def test_1():
	assert Solution.twoSum(None, [1, 3, 5, -1], 8) == [1, 2]

def test_2():
	assert Solution.twoSum(None, [1, 3, 5, 15], 20) == [2, 3]

def test_3():
	assert Solution.twoSum(None, [1, 3], 4) == [0, 1]

def test_4():
	assert Solution.twoSum(None, [1, 3, 13, -2, 8, -4, 10], 21) == [2, 4]
