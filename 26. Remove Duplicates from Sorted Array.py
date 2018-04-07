# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        swap_index = 1 #指向应该交换的位置
        for index in range(1, len(nums)):
            if nums[index] != nums[index-1]:
                #swap
                nums[swap_index] = nums[index] #覆盖即可，重复数字不用保存
                swap_index = swap_index+1 #更新下一个应交换的位置
        return swap_index

    
print(Solution().removeDuplicates([1,1,1,2,2,3,5]))

# 直接用set不行，测试程序只会读取原内存