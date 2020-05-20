from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        # mins = [A[-1]] * (len(A))
        # for i in range(len(A) - 2, -1, -1):
        #     mins[i] = A[i] if A[i] < mins[i + 1] else mins[i + 1]
        # cur_max = A[0]
        # for i in range(len(A) - 1):
        #     cur_max = A[i] if A[i] > cur_max else cur_max
        #     if cur_max <= mins[i + 1]:
        #         return i + 1
        # return 0
        left = 0
        l_max = A[0]
        cur_max = A[0]
        for i in range(len(A)):
            cur_max = cur_max if cur_max > A[i] else A[i]
            if A[i] < l_max:
                left = i
                l_max = cur_max
        return left + 1


'''
C-code: 8-x speed, 2.5-x mem

int partitionDisjoint(int* A, int ASize){
    int left = 0;
    int l_max = A[0];
    int cur_max = A[0];
    int i = 0;
    while (i < ASize)
    {
        cur_max = (cur_max > A[i]) ? cur_max : A[i];
        if (A[i] < l_max)
        {
            left = i;
            l_max = cur_max;
        }
        i++;
    }
    return (left + 1);
}
'''
