from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
            l1, l2 = l2, l1
        nums1.append(nums1[-1])
        nums2.append(nums2[-1])
        y = l2
        x = (l1 - l2) // 2
        while True:
            if nums1[x] <= nums2[y + 1] and nums2[y] <= nums1[x + 1]:
                break
            y -= 1
            x += 1
        return x, y
