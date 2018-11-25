# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:

# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # 主要思想：以t+1为桶的大小，那么差值<t的两个元素比如符合以下情况
        # (1) 在同一个桶里
        # (2) 在相邻的两个桶里
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w #桶编号
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            
            if i >= k: del d[nums[i - k] // w] #移除k超界的值对应的桶
        return False


    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        data = []
        for idx,val in enumerate(nums):
            data.append((idx,val))
        data.sort(key=lambda s: s[1]) # 排序

        for i in range(len(data)-1): # 遍历所有
            j = 1
            while data[i+j][1] -data[i][1] <= t: # 只检查差值小于t的
                if abs(data[i+j][0] -data[i][0]) <= k: # 检查idx间距是否满足要求
                    return True
                j += 1
                if i+j >= len(data):
                    break
        return False


def test(nums, k, t, answer):
    if Solution().containsNearbyAlmostDuplicate(nums, k, t) == answer:
        print('correct!')
    else:
        print('wrong')

test([1,2,3,1],3,0,True)
test([1,0,1,1],1,2,True)
test([1,5,9,1,5,9],2,3,False)
test([1,5,9,1,5,9],2,3, False)
test([2,2],3,0,True)

test([7,2,8],2,1,True)
