# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

class Solution:
    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 1.相同值的index放在同一个列表中
        s = {}
        for i in range(len(nums)):
            if s.get(nums[i]) == None:
                s[nums[i]] = []
            s[nums[i]].append(i)
        # 2. 列表牌序，查找每个列表，是否存在相邻index小于k的
        for key,value in s.items():
            value.sort()
            for i in range(len(value)-1):
                if value[i+1] - value[i] <= k:
                    return True
        return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {} # 字典记录检查过的值
        for idx, num in enumerate(nums):
            if num in seen and idx - seen[num] <= k:# 如果有字典中的值（与当前值相等），且index之差小于k
                return True
            seen[num] = idx # 记录到字典
        # 因为时按照idx顺序检查的，所以每次找到相同值都会覆盖掉更小的那个idx
        return False
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3],2))