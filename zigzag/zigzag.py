class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ''
        for i in range(numRows):
            for j in range(i, len(s), (numRows - 1) * 2):
                res += s[j]
                tmp = j + (numRows - 1 - i) * 2
                if 0 < i < numRows - 1 and tmp < len(s):
                    res += s[tmp]
        return res
