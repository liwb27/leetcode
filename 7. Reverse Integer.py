# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output:  321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == '-':
            start = 1
            s_reverse = '-' + s[:0:-1] # 反序，除了第一个元素
        else:
            start = 0
            s_reverse = s[::-1] # 反序
        ii = int(s_reverse)
        if ii > 2147483647 or ii < -2147483648: # 题目要求int32，超出则返回0，python里不会溢出的，其实没有必要
            return 0
        else:
            return ii

print(Solution().reverse(508))