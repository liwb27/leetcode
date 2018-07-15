# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        degree = 0
        for key,value in dic.items():
            current_degree = len(value)
            current_len = value[-1] - value[0] + 1
            if degree < current_degree:
                degree = current_degree
                min_len = current_len
            if degree == current_degree and min_len > current_len:
                min_len = current_len
        return min_len


import random
n = 50
l = [random.randint(1,n) for _ in range(n)]
print(l)
print(Solution().findShortestSubArray(l))