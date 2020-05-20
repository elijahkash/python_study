class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Hardest Brute Force
        # res = ''
        # for i in range(len(s), 0, -1):
        #     for j in range(0, len(s) - i + 1):
        #         if s[j:j + i] == s[j:j + i][::-1]:
        #             return s[j:j + i]
        # return res

        # Centers expand
        # resl = 0
        # resr = 0
        # for i in range(len(s)):
        #     # odd
        #     left = i - 1
        #     right = i + 1
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     if right - left - 1 > resr - resl:
        #         resl = left + 1
        #         resr = right
        #     # even
        #     left = i
        #     right = i + 1
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     if right - left - 1 > resr - resl:
        #         resl = left + 1
        #         resr = right
        # return s[resl: resr]

        # Manacher's algo (shit)
        # maximum = 0
        # maximum_pos = 0
        # maximum_type = 'odd'
        # left = 0
        # right = -1

        # def native_search(s: str, pos: int, start_range: int,
        #                   pal_type: str) -> int:
        #     nonlocal maximum, maximum_pos, maximum_type, left, right
        #     if pal_type not in ('odd', 'even'):
        #         raise ValueError("type: must be one of {'odd', 'even'}.")
        #     cur_range = start_range
        #     if pal_type == 'odd':
        #         left = pos - start_range
        #         right = pos + start_range
        #     else:
        #         left = pos - start_range
        #         right = pos + 1 + start_range
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #         cur_range += 1
        #     if cur_range > maximum or (cur_range == maximum
        #                                and pal_type == 'even'
        #                                and maximum_type == 'odd'):
        #         maximum = cur_range
        #         maximum_pos = pos
        #         maximum_type = pal_type
        #     left += 1
        #     right -= 1
        #     return cur_range

        # d_odd = [1] * len(s)
        # i = 0
        # while i < len(s):
        #     if i > right:
        #         d_odd[i] = native_search(s, i, 1, 'odd')
        #     elif d_odd[(right - i) + left] + i - 1 < right:
        #         d_odd[i] = d_odd[(right - i) + left]
        #     else:
        #         d_odd[i] = right - i + 1
        #         d_odd[i] = native_search(s, i, d_odd[i], 'odd')
        #     i += 1

        # left = 0
        # right = -1
        # d_even = [0] * len(s)
        # i = 0
        # while i < len(s):
        #     if i > right:
        #         d_even[i] = native_search(s, i, 0, 'even')
        #     elif d_odd[(right - i) + left] + i - 1 < right:  # !!!!!!
        #         d_even[i] = d_even[(right - i) + left]
        #     else:
        #         d_even[i] = right - i
        #         d_even[i] = native_search(s, i, d_even[i], 'even')
        #     i += 1

        # if maximum_type == 'odd':
        #     return s[maximum_pos - maximum + 1: maximum_pos + maximum]
        # else:
        #     return s[maximum_pos - maximum + 1: maximum_pos + maximum + 1]

        # Manacher's algo
        if not s:
            return ''
        odd_left = 0
        odd_right = -1
        odd_arr = [0] * len(s)
        odd_max = 0
        odd_max_pos = 0
        even_left = 0
        even_right = -1
        even_arr = [0] * len(s)
        even_max = 0
        even_max_pos = 0
        i = 0
        for i in range(len(s)):
            # odd
            if i <= odd_right:
                odd_arr[i] = min((odd_right - i,
                                  odd_arr[odd_right - i + odd_left]))
            while (i + odd_arr[i] + 1 < len(s)
                   and i - odd_arr[i] - 1 >= 0
                   and s[i + odd_arr[i] + 1] == s[i - odd_arr[i] - 1]):
                odd_arr[i] += 1
            if odd_arr[i] > odd_max:
                odd_max = odd_arr[i]
                odd_max_pos = i
            if i + odd_arr[i] > odd_right:
                odd_left = i - odd_arr[i]
                odd_right = i + odd_arr[i]
            # even
            if i <= even_right:
                even_arr[i] = min((even_right - i + 1,
                                   even_arr[even_right - i + even_left + 1]))
            while (i + even_arr[i] < len(s)
                   and i - even_arr[i] - 1 >= 0
                   and s[i + even_arr[i]] == s[i - even_arr[i] - 1]):
                even_arr[i] += 1
            if even_arr[i] > even_max:
                even_max = even_arr[i]
                even_max_pos = i
            if i + even_arr[i] - 1 > even_right:
                even_left = i - even_arr[i]
                even_right = i + even_arr[i] - 1
        if even_max > odd_max:
            return s[even_max_pos - even_max: even_max_pos + even_max]
        else:
            return s[odd_max_pos - odd_max: odd_max_pos + odd_max + 1]
