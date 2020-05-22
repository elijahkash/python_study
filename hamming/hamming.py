from typing import List
from itertools import combinations


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while x:
            y += x & 1
            x >>= 1
        return y

    def totalHammingDistance(self, nums: List[int]) -> int:
        # res = 0
        # for pair in combinations(nums, 2):
        #     res += self.hammingDistance(*pair)
        # return res

        bits = [0] * 32
        for x in nums:
            for i in range(32):
                bits[i] += x & 1
                x >>= 1
                if not x:
                    break
        return sum([x * (len(nums) - x) for x in bits])
