from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:

		# Brute Forse
		# for i, x in enumerate(nums):
		# 	for j, y in enumerate(nums[i+1:]):
		# 		if (x + y) == target:
		# 			return [i, i + 1 + j]

		# Hash Table (v.1)
		hash_table = {}
		for i, x in enumerate(nums):
			tmp = hash_table.get(x)
			if tmp != None:
				return sorted([i, tmp])
			else:
				hash_table[target - x] = i

		# left/right - pointers
		# nums = sorted(enumerate(nums), key = lambda x: x[1])
		# l = 0
		# r = len(nums) - 1
		# while l < r:
		# 	tmp =  nums[l][1] + nums[r][1]
		# 	if tmp > target:
		# 		r -= 1
		# 	elif tmp < target:
		# 		l += 1
		# 	else:
		# 		return sorted([nums[l][0], nums[r][0]])
