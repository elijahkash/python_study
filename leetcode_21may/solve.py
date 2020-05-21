from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i, line in enumerate(matrix):
            for j, x in enumerate(line):
                if not x:
                    continue
                if i > 0 and j > 0:
                    line[j] = min(line[j - 1],
                                  matrix[i - 1][j - 1],
                                  matrix[i - 1][j]) + 1
                    res += line[j]
                else:
                    res += 1
        return res
