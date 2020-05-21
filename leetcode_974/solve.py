from typing import List, Dict


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        tmp: int = 0
        counts: Dict[int, int] = {0: 1}
        for i in range(len(A)):
            tmp = tmp + A[i]
            counts[tmp % K] = counts.get(tmp % K, 0) + 1

        return sum([x * (x - 1) // 2 for x in counts.values()])
