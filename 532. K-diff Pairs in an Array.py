# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# Note:
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            count = 0
            nums_set = set(nums)
            for i in nums_set:
                for j in nums:
                    if i == j:
                        count = count+1
                        if count == 2:
                            break
            return count - len(nums_set)
        elif k > 0:
            return len(set(nums)&set(n+k for n in nums)) # 这个方法好，从讨论区看到的，非常简洁
        else:
            return 0

print(Solution().findPairs([-1,-2,-3], 1))
# 标准答案有问题
# 输入：[1,3,1,5,4,1,1]
# 答案输出：1
# 按照题目描述，应该输出2才对，有两个(1,1)