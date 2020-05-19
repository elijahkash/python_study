class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # v1: Hard Brute Force
        # for i in range(len(s), 0, -1):
        #     for j in range(len(s) - i + 1):
        #         flag = True
        #         test = set()
        #         for c in s[j: j + i]:
        #             if c in test:
        #                 flag = False
        #                 break
        #             else:
        #                 test.add(c)
        #         if flag:
        #             return i
        # return 1 if s else 0

        # Dynamic
        # if not s:
        #     return 0
        # res = 1
        # calc = [1] * len(s)
        # for i in range(1, len(s)):
        #     for j in range(i - 1, i - calc[i - 1] - 1, -1):
        #         if s[j] != s[i]:
        #             calc[i] += 1
        #         else:
        #             break
        #     if calc[i] > res:
        #         res += 1
        # return res

        # Slide window (hash)
        # if not s:
        #     return 0
        # res = 1
        # left = 0
        # right = 1
        # test = {s[0]: 0}
        # while len(s) - left > res and right != len(s):
        #     if s[right] in test:
        #         if right - left > res:
        #             res = right - left
        #         left = test[s[right]] + 1
        #         test = {s[i]: i for i in range(left, right)}
        #     else:
        #         test[s[right]] = right
        #         right += 1
        # if right - left > res:
        #     res = right - left
        # return res

        # Slice substr
        length = 0
        substr = ''
        for c in s:
            if c in substr:
                substr = substr[substr.index(c) + 1:]
            substr += c
            if len(substr) > length:
                length = len(substr)
        return length
