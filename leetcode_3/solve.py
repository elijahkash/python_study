class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # v1: Hard Brute Force
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i):
                flag = True
                test = set()
                for c in s[j: j + i]:
                    if c in test:
                        flag = False
                        break
                    else:
                        test.add(c)
                if flag:
                    return i
        return 1 if s else 0
