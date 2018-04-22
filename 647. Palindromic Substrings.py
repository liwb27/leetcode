# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 1:
            return 1
        palindromic = [] #[i][j] 从第j个字符开始长度为i的回文，长度i=0，1认为是回文，
        for i in range(length+1):
            if i == 0 or i == 1:
                val = 1
            else:
                val = 0
            palindromic.append([val for j in range(length - i + 1)])
        count = length
        for i in range(2, length+1):
            for j in range(length - i + 1):
                # 待检测字符串分解为 x,xxxxxxx,x 形式
                # 只有头尾相同，且中间部分为回文时，才为回文
                # 中间部分结果从palindromic中读取
                if palindromic[i-2][j+1] == 1 and s[j] == s[j+i-1]:
                    palindromic[i][j] = 1 #记录结果
                    count +=1 #计数
        return count

if __name__ == '__main__':
    Solution().countSubstrings('aaa')