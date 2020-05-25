from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if l2 > l1:
            nums1, nums2 = nums2, nums1
            l1, l2 = l2, l1
        if l2 == 0:
            if l1 % 2:
                return nums1[l1 // 2]
            else:
                return (nums1[l1 // 2] + nums1[l1 // 2 - 1]) / 2
        d = (l1 - l2) // 2
        isOdd = bool((l1 + l2) % 2)
        # y == 0
        if nums1[l1 - d - 1 - (1 if isOdd else 0)] <= nums2[0]:
            if l1 == l2:
                return ((nums1[-1] + nums2[0]) / 2)
            elif isOdd:
                return min(nums1[l1 - d - 1], nums2[0])
            else:
                return ((nums1[l1 - d - 1] + min(nums2[0], nums1[l1 - d])) / 2)
        # y = l2
        elif nums1[d] >= nums2[-1]:
            if l1 == l2:
                return ((nums2[-1] + nums1[0]) / 2)
            elif isOdd:
                return nums1[d]
            else:
                return ((nums1[d] + max(nums2[-1], nums1[d - 1])) / 2)
        # x = [d + 1: l1 - 1]; y = [1: l2 - 1]
        else:
            x = l1 - d
            if isOdd:
                x -= 1
            for y in range(1, l2):
                x -= 1
                rval = min(nums1[x], nums2[y])
                lval = max(nums1[x - 1], nums2[y - 1])
                if isOdd:
                    if rval >= lval:
                        return rval
                    else:
                        continue
                else:
                    if rval >= lval:
                        return (rval + lval) / 2
                    else:
                        continue

        raise NameError('Shit!')
