#  Given an array A, we may rotate it by a non-negative integer K so that the array becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].  Afterward, any entries that are less than or equal to their index are worth 1 point. 

# For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].  This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

# Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  If there are multiple answers, return the smallest such index K.

# Example 1:
# Input: [2, 3, 1, 4, 0]
# Output: 3
# Explanation:  
# Scores for each K are listed below: 
# K = 0,  A = [2,3,1,4,0],    score 2
# K = 1,  A = [3,1,4,0,2],    score 3
# K = 2,  A = [1,4,0,2,3],    score 3
# K = 3,  A = [4,0,2,3,1],    score 4
# K = 4,  A = [0,2,3,1,4],    score 3
# So we should choose K = 3, which has the highest score.

 

# Example 2:
# Input: [1, 3, 0, 2, 4]
# Output: 0
# Explanation:  A will always have 3 points no matter how it shifts.
# So we will choose the smallest K, which is 0.
# Note:

# A will have length at most 20000.
# A[i] will be in the range [0, A.length].

class Solution:
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 思路
        # 每个A[i]在移位后都会有一段连续的得分区间，这个区间可能是跨边界的
        # 计算出每个A[i]在移位后会产生得分变化的位置，
        # 记录每个位置的得分变化值，假设A[i]的得分区间是k=(m,n)，那么记录diff[m]++，diff[n]--
        # 有可能A[i]的得分区间是k=(0,m),(n,end)
        # 最后对diff做累加，可以得出最大的k出现在哪里
        # 另外，题目规定了A[i]< len(A)
        length = len(A)
        diff = [0] * length
        save = {}
        for i in range(length):
            if A[i] - i <= 0: # 0~min, max~len-1
                diff[(i-A[i]+1) % length] -= 1
                diff[(i+1) % length] += 1
            else:# min~max
                diff[(i-A[i]+1) % length] -= 1
                diff[(i+1) % length] += 1
                diff[0] -= 1

        accumulate = 0
        best = -9999999
        for i in range(length):
            accumulate += diff[i]
            if accumulate > best:
                best = accumulate
                ans = i
        return ans

    def bestRotation2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 全遍历，时间超时
        length = len(A)
        max_score = -1
        for k in range(0, length):
            score = 0
            for i in range(length):
                if A[(i+k) % length] <= i:
                    score += 1
            if score > max_score:
                max_score = score
                max_index = k
        return max_index

print(Solution().bestRotation([2,3,1,4,0]))