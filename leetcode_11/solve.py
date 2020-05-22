from typing import List
# from itertools import combinations


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # hard Brute Force
        # res = 0
        # for pair in combinations(enumerate(height), 2):
        #     tmp = min(pair[0][1], pair[1][1]) * (pair[1][0] - pair[0][0])
        #     if tmp > res:
        #         res = tmp
        # return res
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                res = max(res, (right - left) * height[left])
                left += 1
            else:
                res = max(res, (right - left) * height[right])
                right -= 1
        return res
